"""Generate a discovery catalog mapping data tables to visualizations.

For every spec in ``moderne_visualizations_misc/specs/*.yml`` this collects the
data needed to answer "I have this data table on disk, which visualization
renders it, and how do I run it?":

  * the OpenRewrite ``dataTable`` id (and any ``additionalDataTables``) that
    feed the visualization -- this is the semantic key that links a CSV on
    disk to a notebook;
  * the notebook and spec paths;
  * the sample CSV shipped in ``samples/`` (preferred: ``samples/v2/<id>.csv``,
    which is named after the data table id) and its column schema, so a raw
    CSV can be matched by column signature when its id is unknown;
  * the recipe that produces the data table, plus display metadata.

Outputs two relational CSVs at the repo root, so agents can query them with the
same ``duckdb``/``sqlite`` workflow used for the sample data tables, and GitHub
renders them as sortable tables for humans:

  * ``catalog.csv`` -- one row per visualization (name, notebook, spec, recipe,
    primary data table, sample CSV, and any additional data tables);
  * ``catalog_columns.csv`` -- long form, one row per ``(dataTable, column)``
    across every referenced data table. Matching a raw CSV's header to a
    visualization is then a join: find the data table(s) whose columns match,
    then join ``catalog.csv`` on ``dataTable`` to get the notebook.

Run with ``--check`` to verify the committed files are up to date (used by
``poe check-catalog`` in CI); it exits non-zero and prints a diff hint when they
are stale.

This script depends only on the standard library plus PyYAML (already used by
the other validation scripts), so it needs neither pandas nor papermill.
"""

from __future__ import annotations

import argparse
import csv
import glob
import io
import json
import os
import re
import sys

import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PKG_DIR = os.path.join(REPO_ROOT, "moderne_visualizations_misc")
SPECS_DIR = os.path.join(PKG_DIR, "specs")
SAMPLES_DIR = os.path.join(REPO_ROOT, "samples")

CATALOG_PATH = os.path.join(REPO_ROOT, "catalog.csv")
COLUMNS_PATH = os.path.join(REPO_ROOT, "catalog_columns.csv")

# Matches uncommented `read_csv(...)` / `read_data_table(...)` / `read_optional_csv(...)`
# calls that take a string literal path, used as a fallback to locate the sample
# CSV for data tables that predate the samples/v2 naming convention.
_READ_CALL = re.compile(
    r"""read_(?:csv|data_table|optional_csv)\(\s*["']([^"']+\.csv)["']"""
)


def _rel(path: str) -> str:
    """Repo-root-relative POSIX path for stable, portable output."""
    return os.path.relpath(path, REPO_ROOT).replace(os.sep, "/")


def _collapse(text: object) -> str:
    if not isinstance(text, str):
        return ""
    return " ".join(text.split())


def _recipe_id(recipe: object) -> str:
    """Recipe specs are either a bare id string or a `{id: {options}}` mapping."""
    if isinstance(recipe, str):
        return recipe
    if isinstance(recipe, dict) and recipe:
        return next(iter(recipe))
    return ""


def _notebook_read_paths(notebook_path: str) -> list[str]:
    """Uncommented sample CSV literals referenced by a notebook, in order."""
    try:
        with open(notebook_path, encoding="utf-8") as fh:
            nb = json.load(fh)
    except (OSError, ValueError):
        return []
    paths: list[str] = []
    for cell in nb.get("cells", []):
        if cell.get("cell_type") != "code":
            continue
        for line in "".join(cell.get("source", [])).splitlines():
            if line.lstrip().startswith("#"):
                continue
            paths.extend(_READ_CALL.findall(line))
    return paths


def _resolve_sample(data_table: str, notebook_path: str) -> str | None:
    """Locate the sample CSV for a data table.

    Prefers ``samples/v2/<data_table>.csv`` (named after the id); otherwise
    falls back to the first sample path the notebook actually reads.
    """
    v2 = os.path.join(SAMPLES_DIR, "v2", f"{data_table}.csv")
    if os.path.isfile(v2):
        return v2
    for ref in _notebook_read_paths(notebook_path):
        # Notebook paths are relative to the package dir (e.g. "../samples/x.csv").
        candidate = os.path.normpath(os.path.join(PKG_DIR, ref))
        if os.path.isfile(candidate):
            return candidate
    return None


def _columns(sample_path: str | None) -> list[str]:
    """Header columns of a sample CSV, skipping `#`-prefixed preamble lines."""
    if not sample_path:
        return []
    try:
        with open(sample_path, encoding="utf-8", newline="") as fh:
            rows = csv.reader(
                line
                for line in fh
                if line.strip() and not line.lstrip().startswith("#")
            )
            return next(rows, [])
    except (OSError, ValueError):
        return []


def build_catalog() -> list[dict]:
    entries: list[dict] = []
    for spec_path in sorted(glob.glob(os.path.join(SPECS_DIR, "*.yml"))):
        base = os.path.basename(spec_path)[:-4]
        notebook_path = os.path.join(PKG_DIR, f"{base}.ipynb")
        with open(spec_path, encoding="utf-8") as fh:
            spec = yaml.safe_load(fh) or {}

        data_table = spec.get("dataTable", "")
        sample = _resolve_sample(data_table, notebook_path)

        additional = []
        for param, table_id in (spec.get("additionalDataTables") or {}).items():
            add_sample = _resolve_sample(table_id, notebook_path)
            additional.append(
                {
                    "parameter": param,
                    "dataTable": table_id,
                    "sample": _rel(add_sample) if add_sample else None,
                    "columns": _columns(add_sample),
                }
            )

        entries.append(
            {
                "name": spec.get("name", ""),
                "displayName": spec.get("displayName", ""),
                "description": _collapse(spec.get("description")),
                "notebook": _rel(notebook_path),
                "spec": _rel(spec_path),
                "recipe": _recipe_id(spec.get("recipe")),
                "dataTable": data_table,
                "sample": _rel(sample) if sample else None,
                "columns": _columns(sample),
                "additionalDataTables": additional,
            }
        )
    entries.sort(key=lambda e: e["displayName"].lower())
    return entries


def _write_csv(header: list[str], rows: list[list]) -> str:
    """Serialize rows to a deterministic CSV string (LF line endings)."""
    buffer = io.StringIO()
    writer = csv.writer(buffer, lineterminator="\n")
    writer.writerow(header)
    writer.writerows(rows)
    return buffer.getvalue()


def render_catalog_csv(entries: list[dict]) -> str:
    """One row per visualization; additional tables as `param=id` pairs."""
    header = [
        "displayName",
        "name",
        "notebook",
        "spec",
        "recipe",
        "dataTable",
        "sample",
        "additionalDataTables",
        "description",
    ]
    rows = []
    for e in entries:
        additional = "; ".join(
            f"{a['parameter']}={a['dataTable']}" for a in e["additionalDataTables"]
        )
        rows.append(
            [
                e["displayName"],
                e["name"],
                e["notebook"],
                e["spec"],
                e["recipe"],
                e["dataTable"],
                e["sample"] or "",
                additional,
                e["description"],
            ]
        )
    return _write_csv(header, rows)


def render_columns_csv(entries: list[dict]) -> str:
    """Long form: one row per (dataTable, columnIndex, column).

    Keyed by data table (columns belong to the table, not the visualization),
    covering both primary and additional tables, deduplicated across the
    visualizations that share a data table.
    """
    # dataTable id -> (sample, columns), first occurrence wins (same file).
    tables: dict[str, tuple[str, list[str]]] = {}
    for e in entries:
        for table_id, sample, columns in [
            (e["dataTable"], e["sample"], e["columns"]),
            *[
                (a["dataTable"], a["sample"], a["columns"])
                for a in e["additionalDataTables"]
            ],
        ]:
            if table_id and table_id not in tables:
                tables[table_id] = (sample or "", columns)

    rows = []
    for table_id in sorted(tables):
        sample, columns = tables[table_id]
        for index, column in enumerate(columns):
            rows.append([table_id, sample, index, column])
    return _write_csv(["dataTable", "sample", "columnIndex", "column"], rows)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="Verify catalog.csv/catalog_columns.csv are up to date; exit 1 if stale.",
    )
    args = parser.parse_args()

    entries = build_catalog()
    outputs = {
        CATALOG_PATH: render_catalog_csv(entries),
        COLUMNS_PATH: render_columns_csv(entries),
    }

    if args.check:
        stale = []
        for path, content in outputs.items():
            existing = ""
            if os.path.isfile(path):
                with open(path, encoding="utf-8") as fh:
                    existing = fh.read()
            if existing != content:
                stale.append(_rel(path))
        if stale:
            print("❌ Catalog is out of date: " + ", ".join(stale))
            print("   Run `poe generate-catalog` and commit the result.")
            return 1
        print(f"✅ Catalog is up to date ({len(entries)} visualizations)")
        return 0

    for path, content in outputs.items():
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(content)
        print(f"Wrote {_rel(path)}")
    print(f"Cataloged {len(entries)} visualizations")
    return 0


if __name__ == "__main__":
    sys.exit(main())
