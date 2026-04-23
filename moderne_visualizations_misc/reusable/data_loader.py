"""Load Moderne data tables in a way that accepts v1 or v2 CSV output.

v1 CSVs had `scmType` and `repositoryLink` columns after `repositoryBranch` and
up to four `org*` columns. v2 CSVs drop `scmType`/`repositoryLink`, keep only
`org1`/`org2`, prepend three `# @...` header lines, and may add new columns
(e.g. `fromSourceSet`, `returnType`, `resolutionFailure`).

`code_data_science.data_table.read_csv` already strips `#`-prefixed lines, so
the preamble needs no special handling here. This module only normalizes the
column set so existing notebooks keep working against both formats.
"""

from __future__ import annotations

import pandas as pd
from code_data_science import data_table as dt

_SCM_TYPE_BY_ORIGIN_SUBSTR = (
    ("github", "GITHUB"),
    ("gitlab", "GITLAB"),
    ("bitbucket", "BITBUCKET"),
    ("dev.azure", "AZURE_DEVOPS"),
    ("visualstudio.com", "AZURE_DEVOPS"),
)


def _infer_scm_type(origin: object) -> str:
    if not isinstance(origin, str):
        return ""
    o = origin.lower()
    for needle, scm in _SCM_TYPE_BY_ORIGIN_SUBSTR:
        if needle in o:
            return scm
    return ""


def _build_repository_link(origin: object, path: object) -> str:
    if not isinstance(origin, str) or not isinstance(path, str):
        return ""
    if not origin or not path:
        return ""
    return f"https://{origin.rstrip('/')}/{path.lstrip('/')}"


def read_data_table(sample, *args, **kwargs) -> pd.DataFrame:
    """Read a data table CSV that may be v1 or v2 format.

    Drop-in replacement for `dt.read_csv`. Back-fills `scmType` and
    `repositoryLink` when missing so notebooks that reference them keep
    working on v2 output.
    """
    df = dt.read_csv(sample, *args, **kwargs)

    has_origin = "repositoryOrigin" in df.columns
    has_path = "repositoryPath" in df.columns

    if "scmType" not in df.columns:
        df["scmType"] = df["repositoryOrigin"].map(_infer_scm_type) if has_origin else ""

    if "repositoryLink" not in df.columns:
        if has_origin and has_path:
            df["repositoryLink"] = [
                _build_repository_link(o, p)
                for o, p in zip(df["repositoryOrigin"], df["repositoryPath"])
            ]
        else:
            df["repositoryLink"] = ""

    return df
