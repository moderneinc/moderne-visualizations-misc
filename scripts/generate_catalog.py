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

Outputs ``catalog.json`` (machine-readable) and ``CATALOG.md`` (human-readable)
at the repo root. Run with ``--check`` to verify the committed files are up to
date (used by ``poe check-catalog`` in CI); it exits non-zero and prints a diff
hint when they are stale.

This script depends only on the standard library plus PyYAML (already used by
the other validation scripts), so it needs neither pandas nor papermill.
"""

from __future__ import annotations

import argparse
import csv
import glob
import json
import os
import re
import sys

import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PKG_DIR = os.path.join(REPO_ROOT, "moderne_visualizations_misc")
SPECS_DIR = os.path.join(PKG_DIR, "specs")
SAMPLES_DIR = os.path.join(REPO_ROOT, "samples")

JSON_PATH = os.path.join(REPO_ROOT, "catalog.json")
MD_PATH = os.path.join(REPO_ROOT, "CATALOG.md")

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


def render_json(entries: list[dict]) -> str:
    return json.dumps(entries, indent=2, ensure_ascii=False) + "\n"


def render_markdown(entries: list[dict]) -> str:
    lines = [
        "<!-- Generated by scripts/generate_catalog.py. Do not edit by hand. -->",
        "<!-- Run `poe generate-catalog` to regenerate after changing specs. -->",
        "",
        "# Visualization catalog",
        "",
        "Every visualization in this package, keyed by the OpenRewrite **data "
        "table** that feeds it. Use this to go from a data table on disk to a "
        "rendered visualization:",
        "",
        "1. **Know the data table id?** Find its row in the _Data table_ column.",
        "2. **Only have a raw CSV?** Match its header against the sample CSV's "
        "columns (see `catalog.json` for the full column list per entry). Sample "
        "files under `samples/v2/` are named after their data table id.",
        "3. **Render it** via papermill (see "
        "[CLAUDE.md](CLAUDE.md#from-a-data-table-to-a-visualization)):",
        "",
        "   ```bash",
        '   NB_DATA_TABLE="samples/v2/<data-table-id>.csv" \\',
        "     uv run papermill <notebook> /tmp/out.ipynb",
        "   uv run jupyter nbconvert --to html /tmp/out.ipynb --output /tmp/out.html",
        "   ```",
        "",
        f"{len(entries)} visualizations. Regenerate with `poe generate-catalog`.",
        "",
        "| Visualization | Notebook | Data table | Sample CSV | Key columns |",
        "| --- | --- | --- | --- | --- |",
    ]
    for e in entries:
        notebook = os.path.basename(e["notebook"])
        sample = os.path.basename(e["sample"]) if e["sample"] else "—"
        cols = e["columns"][:6]
        cols_txt = ", ".join(f"`{c}`" for c in cols) if cols else "—"
        if len(e["columns"]) > 6:
            cols_txt += ", …"
        add = ""
        if e["additionalDataTables"]:
            ids = ", ".join(f"`{a['dataTable']}`" for a in e["additionalDataTables"])
            add = f"<br>+ {ids}"
        lines.append(
            f"| {e['displayName']} "
            f"| [`{notebook}`]({e['notebook']}) "
            f"| `{e['dataTable']}`{add} "
            f"| {sample} "
            f"| {cols_txt} |"
        )
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="Verify catalog.json/CATALOG.md are up to date; exit 1 if stale.",
    )
    args = parser.parse_args()

    entries = build_catalog()
    outputs = {JSON_PATH: render_json(entries), MD_PATH: render_markdown(entries)}

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
