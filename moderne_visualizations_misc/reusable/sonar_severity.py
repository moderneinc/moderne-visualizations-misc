"""Count and chart the outcome of a Sonar recipe run: its Sonar issues, by severity.

Every Sonar recipe composes one recipe per Sonar severity, named
``<library>.sonar.Blocker`` through ``<library>.sonar.Info``, and each of those
composes the rules of that severity. In ``org.openrewrite.table.SourcesFileResults``
a rule's row names its severity recipe as ``parentRecipe``, so one row whose
``parentRecipe`` ends in ``.sonar.<Severity>`` is one issue: one file changed by
one Sonar rule.

A data table can hold the same row more than once, so each issue is counted
once per repository, branch, file, severity and rule.

Rows further down the stack (the recipes a rule itself composes) and the rows of
the severity recipes themselves are left out, so a rule counts once per file
however it is built. The severity recipes of every library match, so the
chart works for each library's ``SonarRules`` and for a recipe that composes
several of them.

A rule a library lists under two severities counts under whichever severity
changed the file, so its bar in the rule view can be split between them.

A run of one severity recipe on its own, such as ``<library>.sonar.Major``,
shows no issues. The table leaves out a run's top-level recipe and records its
direct children with no ``parentRecipe``, so in such a run the rules' rows name
no severity. (In a ``SonarRules`` run that is what keeps the severity recipes'
own rows out of the count.) Point a spec at a ``SonarRules`` recipe, or at a
recipe that composes one, not at a single severity recipe.
"""

from __future__ import annotations

import re

import pandas as pd
import plotly.graph_objects as go

from moderne_visualizations_misc.reusable import quality_utils as qu

SEVERITY_ORDER = ["Blocker", "Critical", "Major", "Minor", "Info"]

# One blue ramp, darkest for the most severe. Checked for color vision
# deficiency separation and contrast on a white surface.
SEVERITY_COLORS = {
    "Blocker": "#104281",
    "Critical": "#1c5cab",
    "Major": "#2a78d6",
    "Minor": "#5598e7",
    "Info": "#86b6ef",
}

VIEWS = ("severity", "repository", "rule")

_SEVERITY_PARENT = re.compile(r"\.sonar\.(Blocker|Critical|Major|Minor|Info)$")

_INK = "#1f2937"
_MUTED_INK = "#6b7280"
_GRID = "#e5e7eb"


def sonar_issues(df: pd.DataFrame) -> pd.DataFrame:
    """One row per Sonar issue: repository, severity and rule.

    Returns an empty frame with the same columns when ``df`` holds no rows of
    a Sonar severity recipe, as for a run of a recipe that is not a Sonar one.
    """
    columns = ["repository", "severity", "rule", "ruleId"]
    if df.empty or "parentRecipe" not in df.columns or "recipe" not in df.columns:
        return pd.DataFrame(columns=columns)

    severity = (
        df["parentRecipe"].astype("string").str.extract(_SEVERITY_PARENT, expand=False)
    )
    rows = df[severity.notna()].copy()
    if rows.empty:
        return pd.DataFrame(columns=columns)

    rows["severity"] = severity[severity.notna()]
    rows["ruleId"] = rows["recipe"].astype(str)
    rows["rule"] = _rule_labels(rows["ruleId"])
    rows["repository"] = _repository_labels(rows)
    key = [
        c
        for c in (
            "repositoryOrigin",
            "repositoryPath",
            "repositoryBranch",
            "sourcePath",
        )
        if c in rows.columns
    ]
    rows = rows.drop_duplicates(subset=key + ["severity", "ruleId"])
    return rows[columns].reset_index(drop=True)


def _rule_labels(rule_ids: pd.Series) -> pd.Series:
    """A rule's simple name, or its full id where two rules share the simple name."""
    short = rule_ids.map(qu.short_class)
    ids_per_short = (
        pd.DataFrame({"short": short, "id": rule_ids})
        .groupby("short")["id"]
        .transform("nunique")
    )
    return short.where(ids_per_short <= 1, rule_ids)


def _repository_labels(rows: pd.DataFrame) -> pd.Series:
    """A repository's path, with its branch when the run covered several branches of it."""
    if "repositoryPath" not in rows.columns:
        return pd.Series("", index=rows.index)
    path = rows["repositoryPath"].astype(str)
    if "repositoryBranch" not in rows.columns:
        return path
    branch = rows["repositoryBranch"].astype(str)
    branches_per_path = (
        pd.DataFrame({"path": path, "branch": branch})
        .groupby("path")["branch"]
        .transform("nunique")
    )
    return path.where(branches_per_path <= 1, path + "/" + branch)


def figure(
    df: pd.DataFrame,
    view: str = "severity",
    top_n: int | str = 20,
    repository_filter: list[str] | None = None,
) -> go.Figure:
    """The chart for ``view``: severity (default), repository or rule.

    A view that is none of those shows the severity view.
    """
    df = qu.filter_repos(df, repository_filter or [])
    issues = sonar_issues(df)
    if issues.empty:
        return qu.empty_figure("No Sonar issues in this run for the selected filters.")

    view = (view or "severity").strip().lower()
    view = {
        "severities": "severity",
        "repositories": "repository",
        "rules": "rule",
    }.get(view, view)
    n = _top_n(top_n)
    if view == "repository":
        return repository_figure(issues, n)
    if view == "rule":
        return rule_figure(issues, n)
    return severity_figure(issues)


def _top_n(top_n: int | str) -> int:
    try:
        n = int(str(top_n).strip())
    except ValueError:
        n = 20
    return max(n, 1)


def _title(issues: pd.DataFrame, detail: str) -> dict:
    total = len(issues)
    repositories = issues["repository"].nunique()
    noun = "issue" if total == 1 else "issues"
    repo_noun = "repository" if repositories == 1 else "repositories"
    return dict(
        text=f"{total:,} Sonar {noun} in {repositories:,} {repo_noun}"
        f"<br><sup style='color:{_MUTED_INK}'>{detail}</sup>",
        x=0,
        xanchor="left",
        font=dict(color=_INK),
    )


def _layout(fig: go.Figure, title: dict, height: int, legend: bool) -> go.Figure:
    fig.update_layout(
        title=title,
        template="plotly_white",
        height=height,
        margin=dict(l=20, r=40, t=90, b=50),
        barcornerradius=4,
        bargap=0.35,
        showlegend=legend,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.0,
            xanchor="left",
            x=0,
            traceorder="normal",
            title=None,
        ),
        hoverlabel=dict(bgcolor="white", font=dict(color=_INK)),
        font=dict(color=_INK),
    )
    fig.update_xaxes(
        title="Issues",
        gridcolor=_GRID,
        zeroline=False,
        tickformat=",d",
        rangemode="tozero",
    )
    fig.update_yaxes(
        title=None, showgrid=False, automargin=True, ticks="", ticklabelstandoff=8
    )
    return fig


def severity_figure(issues: pd.DataFrame) -> go.Figure:
    """One bar per severity, most severe on top, every severity shown even at zero."""
    total = len(issues)
    counts = issues.groupby("severity").size().reindex(SEVERITY_ORDER, fill_value=0)
    repos = (
        issues.groupby("severity")["repository"]
        .nunique()
        .reindex(SEVERITY_ORDER, fill_value=0)
    )
    rules = (
        issues.groupby("severity")["ruleId"]
        .nunique()
        .reindex(SEVERITY_ORDER, fill_value=0)
    )

    fig = go.Figure(
        go.Bar(
            y=SEVERITY_ORDER,
            x=counts.values,
            orientation="h",
            marker=dict(color=[SEVERITY_COLORS[s] for s in SEVERITY_ORDER]),
            text=[f"{c:,}" for c in counts.values],
            textposition="outside",
            textfont=dict(color=_INK),
            cliponaxis=False,
            customdata=[
                [c / total if total else 0, r, k]
                for c, r, k in zip(counts.values, repos.values, rules.values)
            ],
            hovertemplate="<b>%{y}</b><br>%{x:,} issues (%{customdata[0]:.1%})"
            "<br>%{customdata[1]:,} repositories<br>%{customdata[2]:,} rules<extra></extra>",
        )
    )
    fig.update_yaxes(
        categoryorder="array", categoryarray=SEVERITY_ORDER, autorange="reversed"
    )
    return _layout(
        fig,
        _title(issues, "Each issue is one file changed by one Sonar rule"),
        380,
        legend=False,
    )


def _stacked(
    issues: pd.DataFrame,
    group: str,
    top_n: int,
    label: str,
    full_names: dict[str, str] | None = None,
) -> go.Figure:
    """Bars for the ``top_n`` largest values of ``group``, stacked by severity.

    ``full_names`` maps a bar's label to the name the hover shows under it.
    """
    totals = issues.groupby(group).size().sort_values(ascending=False)
    shown = totals.head(top_n)
    order = shown.index.tolist()
    counts = (
        issues[issues[group].isin(order)]
        .groupby([group, "severity"])
        .size()
        .unstack(fill_value=0)
    )
    counts = counts.reindex(index=order, columns=SEVERITY_ORDER, fill_value=0)

    hover_names = [(full_names or {}).get(name, "") for name in order]
    full_line = "<br>%{customdata}" if full_names else ""

    fig = go.Figure()
    for severity in SEVERITY_ORDER:
        values = counts[severity]
        if values.sum() == 0:
            continue
        fig.add_trace(
            go.Bar(
                y=order,
                x=values.values,
                name=severity,
                orientation="h",
                marker=dict(
                    color=SEVERITY_COLORS[severity], line=dict(color="white", width=2)
                ),
                customdata=hover_names,
                hovertemplate=f"<b>%{{y}}</b>{full_line}<br>{severity}: %{{x:,}} issues<extra></extra>",
            )
        )
    for name, value in shown.items():
        fig.add_annotation(
            x=value,
            y=name,
            text=f"{value:,}",
            showarrow=False,
            xanchor="left",
            xshift=6,
            font=dict(color=_INK),
        )
    fig.update_layout(barmode="stack")
    fig.update_yaxes(categoryorder="array", categoryarray=order, autorange="reversed")
    rest = len(totals) - len(shown)
    detail = f"Top {len(shown):,} {label} by issues" + (
        f", {rest:,} more not shown" if rest > 0 else ""
    )
    height = max(400, len(order) * 28 + 160)
    return _layout(fig, _title(issues, detail), height, legend=True)


def repository_figure(issues: pd.DataFrame, top_n: int = 20) -> go.Figure:
    """The repositories with the most issues, each bar split by severity."""
    return _stacked(issues, "repository", top_n, "repositories")


def rule_figure(issues: pd.DataFrame, top_n: int = 20) -> go.Figure:
    """The rules with the most issues, each bar split by severity.

    A rule normally sits under one severity, so its bar is a single color. A
    rule its library lists under two severities shows both. The hover shows each
    rule's full recipe id.
    """
    full_names = dict(zip(issues["rule"], issues["ruleId"]))
    return _stacked(issues, "rule", top_n, "rules", full_names)
