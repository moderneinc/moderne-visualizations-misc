"""Shared utilities for code quality metric visualizations."""

import pandas as pd
import plotly.graph_objects as go

# Standard color scales
HEALTH_COLORSCALE = ["#EF5350", "#FF8A65", "#FFE082", "#A5D6A7", "#4CAF50"]  # red to green
SEVERITY_COLORS = {
    "CRITICAL": "#EF5350",
    "HIGH": "#FF8A65",
    "MEDIUM": "#FFE082",
    "LOW": "#A5D6A7",
}
SEVERITY_ORDER = ["LOW", "MEDIUM", "HIGH", "CRITICAL"]


def filter_repos(df: pd.DataFrame, repository_filter: list[str]) -> pd.DataFrame:
    """Filter DataFrame by repository path, case insensitive."""
    if not repository_filter:
        return df
    pattern = "|".join(repository_filter)
    col = "repositoryPath" if "repositoryPath" in df.columns else df.columns[1]
    mask = df[col].str.contains(pattern, case=False, na=False)
    if "repositoryBranch" in df.columns:
        combined = df[col] + "/" + df["repositoryBranch"]
        mask = mask | combined.str.contains(pattern, case=False, na=False)
    return df[mask]


def empty_figure(message: str = "No data available for the selected filters.") -> go.Figure:
    """Create an empty figure with a centered message."""
    fig = go.Figure()
    fig.add_annotation(
        text=message,
        xref="paper",
        yref="paper",
        x=0.5,
        y=0.5,
        showarrow=False,
        font=dict(size=16, color="#666"),
    )
    fig.update_layout(
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        height=400,
    )
    return fig


def short_repo(repo_path) -> str:
    """Extract short repo name from full path."""
    if not isinstance(repo_path, str):
        return str(repo_path)
    return repo_path.split("/")[-1] if "/" in repo_path else repo_path


def short_class(class_name, source_path=None) -> str:
    """Extract simple class name from FQN, falling back to source file name."""
    if not isinstance(class_name, str) or class_name == "":
        if isinstance(source_path, str):
            return source_path.rsplit("/", 1)[-1]
        return str(class_name) if isinstance(class_name, str) else "(unknown)"
    return class_name.split(".")[-1] if "." in class_name else class_name


def extract_package(class_name) -> str:
    """Extract package name from fully qualified class name."""
    if not isinstance(class_name, str):
        return ""
    parts = class_name.rsplit(".", 1)
    return parts[0] if len(parts) > 1 else ""


def compute_debt_score(df: pd.DataFrame) -> pd.Series:
    """Compute composite debt score from method quality metrics.

    Weighted combination of normalized complexity, cognitive complexity,
    nesting depth, and estimated bugs.
    """
    cols = {
        "cyclomaticComplexity": 0.4,
        "cognitiveComplexity": 0.3,
        "maxNestingDepth": 0.2,
        "halsteadEstimatedBugs": 0.1,
    }
    score = pd.Series(0.0, index=df.index)
    for col, weight in cols.items():
        if col in df.columns:
            col_max = df[col].max()
            if col_max > 0:
                score += weight * (df[col] / col_max)
    return score


def format_metric(name: str, value, thresholds: dict | None = None) -> str:
    """Format a metric value with executive-friendly label.

    Args:
        name: Metric name (e.g., 'wmc', 'lcom4', 'cbo')
        value: The metric value
        thresholds: Optional dict with 'healthy' threshold for comparison
    """
    labels = {
        "wmc": f"Complexity score: {value}",
        "lcom4": f"Should be split into {value} classes" if value > 1 else "Well-cohesive class",
        "tcc": f"Cohesion: {value:.0%}" if isinstance(value, float) else f"Cohesion: {value}",
        "cbo": f"Coupled to {value} other components",
        "maintainabilityIndex": f"Maintainability: {value:.0f}/100",
        "cyclomaticComplexity": f"Complexity: {value} paths",
        "cognitiveComplexity": f"Cognitive load: {value}",
        "maxNestingDepth": f"Nesting: {value} levels deep",
        "riskScore": f"Risk score: {value}",
        "instability": f"Instability: {value:.0%}",
        "abstractness": f"Abstractness: {value:.0%}",
        "distanceFromMainSequence": f"Architecture gap: {value:.2f}",
    }
    base = labels.get(name, f"{name}: {value}")

    if thresholds and name in thresholds:
        threshold = thresholds[name]
        if isinstance(value, (int, float)) and value > threshold:
            ratio = value / threshold
            base += f" ({ratio:.1f}x above healthy)"

    return base


# Default thresholds for "healthy" values
HEALTHY_THRESHOLDS = {
    "wmc": 10,
    "lcom4": 1,
    "cbo": 10,
    "cyclomaticComplexity": 10,
    "cognitiveComplexity": 15,
    "maxNestingDepth": 3,
    "riskScore": 10,
}


def add_repo_short(df: pd.DataFrame) -> pd.DataFrame:
    """Add a 'repoShort' column derived from repositoryPath."""
    if "repositoryPath" in df.columns:
        df = df.copy()
        df["repoShort"] = df["repositoryPath"].apply(short_repo)
    return df


def add_class_short(df: pd.DataFrame) -> pd.DataFrame:
    """Add 'classShort' and 'package' columns derived from className."""
    if "className" in df.columns:
        df = df.copy()
        if "sourcePath" in df.columns:
            df["classShort"] = df.apply(
                lambda r: short_class(r["className"], r["sourcePath"]), axis=1
            )
        else:
            df["classShort"] = df["className"].apply(short_class)
        df["package"] = df["className"].apply(extract_package)
    return df
