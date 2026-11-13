import re
from collections.abc import Iterable

# code_data_science.versions.index recurses without bound when two versions share
# a numeric prefix longer than its regex captures (e.g. 2.0.0-20210101.123456-1
# vs 2.0.0-20210102.000000-2, or anything with seven or more numeric parts).
_NUMERIC_PREFIX = re.compile(r"\d+(?:[.\-]\d+)*")


def _sort_key(version: str) -> tuple:
    match = _NUMERIC_PREFIX.match(version)
    if match is None:
        return (0, (), version, version)
    numbers = [int(part) for part in re.split(r"[.\-]", match.group())]
    while len(numbers) > 1 and numbers[-1] == 0:
        numbers.pop()
    return (1, tuple(numbers), version[match.end() :], version)


def index_versions(versions: Iterable[str]) -> dict[str, int]:
    """Map each distinct version to its rank, oldest first; unparseable versions sort first."""
    return {v: i for i, v in enumerate(sorted(set(versions), key=_sort_key))}
