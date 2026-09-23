"""Verify each plotly visualization names its downloaded PNG after its spec.

Plotly's "Download plot as png" toolbar button defaults to ``newplot.png``, so a
folder of downloaded charts is indistinguishable. Every plotly ``show()`` call
therefore passes::

    fig.show(config={"toImageButtonOptions": {"filename": "<dataTable>-<name>"}})

where the filename joins the last dotted segment of the spec's ``dataTable`` and
``name`` (e.g. ``TestGaps-TestGapRiskHeatmap``). That value is a pure function of
the spec, so this script recomputes it and enforces two things per spec:

  * **coverage** -- a notebook that reaches a plotly ``show()`` must contain its
    expected filename, so new visualizations cannot ship as ``newplot.png``;
  * **correctness** -- any ``toImageButtonOptions`` filename in the notebook must
    equal the expected value, so renaming a spec cannot silently leave the old
    name behind.

Notebooks that only call ``plt.show()`` (matplotlib), render a tree data grid, or
emit PlantUML have no download button and are skipped.

Filenames are checked as literals in the notebook rather than centralized in a
helper: the value stays readable next to the chart it names, and this check is
what makes it drift-proof. Notebooks that delegate rendering to a ``reusable/``
module (e.g. ``violin_nodejs``) pass their filename in, so the literal is still
in the notebook.

Run via ``poe check-png-filenames``; exits non-zero and names each mismatch.
"""

from __future__ import annotations

import glob
import json
import os
import re
import sys

import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PKG_DIR = os.path.join(REPO_ROOT, "moderne_visualizations_misc")
SPECS_DIR = os.path.join(PKG_DIR, "specs")
REUSABLE_DIR = os.path.join(PKG_DIR, "reusable")

# `<receiver>.show(` -- receiver distinguishes plotly figures from `plt.show()`.
_SHOW_CALL = re.compile(r"(\w+)\.show\(")

# The filename plotly uses for the toolbar download button.
_TOIMAGE_FILENAME = re.compile(
    r"""toImageButtonOptions["']?\s*:\s*\{\s*["']filename["']\s*:\s*["']([^"']+)["']"""
)


def _code(notebook_path: str) -> str:
    """Uncommented code-cell source of a notebook, newline joined."""
    try:
        with open(notebook_path, encoding="utf-8") as fh:
            nb = json.load(fh)
    except (OSError, ValueError):
        return ""
    lines: list[str] = []
    for cell in nb.get("cells", []):
        if cell.get("cell_type") != "code":
            continue
        for line in "".join(cell.get("source", [])).splitlines():
            if not line.lstrip().startswith("#"):
                lines.append(line)
    return "\n".join(lines)


def _reusable_sources(notebook_code: str) -> str:
    """Source of the `reusable/` modules a notebook references by name."""
    sources = []
    for path in sorted(glob.glob(os.path.join(REUSABLE_DIR, "*.py"))):
        module = os.path.basename(path)[:-3]
        if module == "__init__" or not re.search(rf"\b{re.escape(module)}\b", notebook_code):
            continue
        try:
            with open(path, encoding="utf-8") as fh:
                sources.append(fh.read())
        except OSError:
            continue
    return "\n".join(sources)


def _has_plotly_show(code: str) -> bool:
    """True if any `show()` call is on something other than matplotlib's `plt`."""
    return any(receiver != "plt" for receiver in _SHOW_CALL.findall(code))


def check(spec_path: str) -> tuple[bool, str]:
    """Check one spec's notebook. Returns (ok, message)."""
    base = os.path.basename(spec_path)[:-4]
    notebook_path = os.path.join(PKG_DIR, f"{base}.ipynb")
    if not os.path.isfile(notebook_path):
        return False, f"{base}.ipynb is missing"

    with open(spec_path, encoding="utf-8") as fh:
        spec = yaml.safe_load(fh) or {}
    data_table = spec.get("dataTable", "")
    name = spec.get("name", "")
    if not data_table or not name:
        return True, f"{base}.ipynb (skipped: spec has no dataTable/name)"
    expected = f"{data_table.split('.')[-1]}-{name.split('.')[-1]}"

    code = _code(notebook_path)
    # A notebook may render via a reusable module, so look there for the show()
    # call -- but require the filename literal in the notebook, which passes it in.
    if not _has_plotly_show(code + "\n" + _reusable_sources(code)):
        return True, f"{base}.ipynb (skipped: no plotly figure)"

    wrong = {f for f in _TOIMAGE_FILENAME.findall(code) if f != expected}
    if wrong:
        return False, f"{base}.ipynb has filename {sorted(wrong)}, expected '{expected}'"
    if expected not in code:
        return False, f"{base}.ipynb is missing filename '{expected}'"
    return True, f"{base}.ipynb"


def main() -> int:
    print("\nCheck downloaded PNG filenames match the spec dataTable and name")
    print("-----------------------------------------------------------------------------")

    exit_code = 0
    for spec_path in sorted(glob.glob(os.path.join(SPECS_DIR, "*.yml"))):
        ok, message = check(spec_path)
        print(f"{'✅' if ok else '❌'} {message}")
        if not ok:
            exit_code = 1
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
