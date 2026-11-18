"""Read `LanguageCompositionPerFile` into per-group counts in bounded memory.

The table has one row per source file, so an organization of tens of thousands of
repositories gives a CSV of more than a gigabyte. Every language composition chart only
needs counts and line totals per (repository, language, file extension, source file type,
parse failure) group, so the table is read in chunks of the columns those groups need and
each chunk is aggregated before the next one is read. Memory then grows with the number of
groups rather than the number of files.
"""

from __future__ import annotations

import pandas as pd
from code_data_science import data_table as dt

_FILE_COLUMNS = {
    "repositoryOrigin",
    "repositoryPath",
    "repositoryBranch",
    "sourcePath",
    "language",
    "sourceFileType",
    # v1 tables named the source file type `parserClass`
    "parserClass",
    "linesOfText",
    "hasParseFailures",
}

_PLAIN_TEXT_LANGUAGE_BY_FILE_TYPE = {
    "ts": "Typescript",
    "tsx": "Typescript",
    "js": "Javascript",
    "jsx": "Javascript",
    "kts": "Kotlin",
}

DEFAULT_CHUNKSIZE = 250_000


def _group_columns(by_repository: bool) -> list[str]:
    keys = ["language", "fileType", "sourceFileType", "hasParseFailures"]
    return ["repository", *keys] if by_repository else keys


def _aggregate_chunk(chunk: pd.DataFrame, by_repository: bool) -> pd.DataFrame:
    if "sourceFileType" not in chunk.columns and "parserClass" in chunk.columns:
        chunk = chunk.rename(columns={"parserClass": "sourceFileType"})
    if "sourceFileType" not in chunk.columns:
        chunk["sourceFileType"] = pd.NA

    if by_repository:
        chunk["repository"] = (
            chunk["repositoryOrigin"]
            + ":"
            + chunk["repositoryPath"]
            + ":"
            + chunk["repositoryBranch"]
        )

    chunk["fileType"] = chunk["sourcePath"].str.split(".").str[-1]

    # A chunk with no failures reads as bool and one with a blank cell as object, so
    # normalize before chunks are combined. `== True` on the original column meant the same.
    chunk["hasParseFailures"] = chunk["hasParseFailures"].astype(str).str.lower() == "true"

    remapped = chunk["fileType"].map(_PLAIN_TEXT_LANGUAGE_BY_FILE_TYPE)
    plain_text = (chunk["language"] == "Plain text") & remapped.notna()
    chunk.loc[plain_text, "language"] = remapped[plain_text]

    chunk["files"] = 1
    chunk["linesOfText"] = pd.to_numeric(chunk["linesOfText"], errors="coerce")

    # dropna=False keeps rows with a blank key, so that totals still count every file.
    return chunk.groupby(_group_columns(by_repository), dropna=False, as_index=False)[
        ["files", "linesOfText"]
    ].sum()


def read_language_composition(
    sample, by_repository: bool = False, chunksize: int = DEFAULT_CHUNKSIZE
) -> pd.DataFrame:
    """Read a `LanguageCompositionPerFile` table as one row per group.

    Columns are the group keys (`repository` as `origin:path:branch` when
    `by_repository`, then `language`, `fileType`, `sourceFileType`,
    `hasParseFailures`) and the sums `files` and `linesOfText`. Keys may be NaN
    where the table left a cell blank; such rows count toward totals, and
    callers drop them before charting as `groupby` used to.
    """
    reader = dt.read_csv(
        sample,
        usecols=lambda column: column in _FILE_COLUMNS,
        chunksize=chunksize,
    )
    parts = [_aggregate_chunk(chunk, by_repository) for chunk in reader]
    columns = [*_group_columns(by_repository), "files", "linesOfText"]
    parts = [part for part in parts if len(part)]
    if not parts:
        return pd.DataFrame(columns=columns)
    return (
        pd.concat(parts, ignore_index=True)
        .groupby(_group_columns(by_repository), dropna=False, as_index=False)[
            ["files", "linesOfText"]
        ]
        .sum()[columns]
    )


def read_language_composition_by_folder(
    sample, chunksize: int = DEFAULT_CHUNKSIZE
) -> pd.DataFrame:
    """Read a `LanguageCompositionPerFolder` table as `fileCount` and `lineCount`
    summed per (`folderPath`, `language`), in chunks like `read_language_composition`.

    As `groupby` does by default, rows with a blank `folderPath` or `language`
    (the repository root reads as blank) are left out.
    """
    keys = ["folderPath", "language"]
    reader = dt.read_csv(
        sample,
        usecols=keys + ["fileCount", "lineCount"],
        chunksize=chunksize,
    )
    parts = [
        chunk.groupby(keys, as_index=False)[["fileCount", "lineCount"]].sum()
        for chunk in reader
    ]
    parts = [part for part in parts if len(part)]
    if not parts:
        return pd.DataFrame(columns=keys + ["fileCount", "lineCount"])
    return (
        pd.concat(parts, ignore_index=True)
        .groupby(keys, as_index=False)[["fileCount", "lineCount"]]
        .sum()
    )
