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
    # Empty check: read_optional_csv returns a column-less frame for missing tables.
    if not repository_filter or df.empty:
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


def short_class(class_name) -> str:
    """Extract simple class name from FQN."""
    if not isinstance(class_name, str):
        return str(class_name)
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
        df["classShort"] = df["className"].apply(short_class)
        df["package"] = df["className"].apply(extract_package)
    return df


_LABEL_OFFSETS = [
    (ring, dx * r, dy * r)
    for ring, r in enumerate((40, 70, 110))
    for dx, dy in (
        (1, -0.6),
        (-1, -0.6),
        (1, 0.6),
        (-1, 0.6),
        (1.2, 0),
        (-1.2, 0),
        (0, -0.8),
        (0, 0.8),
    )
]


def add_point_labels(
    fig: go.Figure,
    x: pd.Series,
    y: pd.Series,
    sizes: pd.Series,
    labels: pd.Series,
    plot_width: float,
    plot_height: float,
) -> None:
    """Label selected scatter points on the chart itself, so they survive static exports.

    `x`, `y` and `sizes` cover every plotted point; `labels` is indexed by the rows to
    label, highest priority first. Pins both axis ranges so bubble and label positions can
    be computed in pixels. Each label takes the leader-line offset that stays inside the
    plot and clear of labels already placed, trading bubbles covered against leader length.
    """
    pad = sizes.max() / 2 + 10
    x_span = (x.max() - x.min()) or 1
    y_span = (y.max() - y.min()) or 1
    x_pad = x_span * pad / (plot_width - 2 * pad)
    y_pad = y_span * pad / (plot_height - 2 * pad)
    fig.update_xaxes(range=[x.min() - x_pad, x.max() + x_pad])
    fig.update_yaxes(range=[y.min() - y_pad, y.max() + y_pad])
    px = pad + (x - x.min()) / x_span * (plot_width - 2 * pad)
    py = plot_height - pad - (y - y.min()) / y_span * (plot_height - 2 * pad)
    radius = sizes / 2

    placed: list[tuple[float, float, float, float]] = []
    for i, text in labels.items():
        half_w, half_h = 3.4 * len(text) + 4, 9
        best: tuple[int, tuple[float, float]] | None = None
        for ring, dx, dy in _LABEL_OFFSETS:
            cx, cy = px[i] + dx, py[i] + dy
            box = (cx - half_w, cy - half_h, cx + half_w, cy + half_h)
            if box[0] < 0 or box[1] < 0 or box[2] > plot_width or box[3] > plot_height:
                continue
            if any(
                box[0] < p[2] and p[0] < box[2] and box[1] < p[3] and p[1] < box[3]
                for p in placed
            ):
                continue
            score = 2 * ring + int(
                (
                    (px + radius > box[0])
                    & (px - radius < box[2])
                    & (py + radius > box[1])
                    & (py - radius < box[3])
                ).sum()
            )
            if best is None or score < best[0]:
                best = (score, (dx, dy))
        dx, dy = best[1] if best else _LABEL_OFFSETS[0][1:]
        placed.append(
            (
                px[i] + dx - half_w,
                py[i] + dy - half_h,
                px[i] + dx + half_w,
                py[i] + dy + half_h,
            )
        )
        fig.add_annotation(
            x=x[i],
            y=y[i],
            text=text,
            ax=dx,
            ay=dy,
            showarrow=True,
            arrowhead=0,
            arrowwidth=1,
            arrowcolor="#666",
            standoff=radius[i],
            font=dict(size=11, color="#2a3f5f"),
            bgcolor="rgba(255,255,255,0.85)",
            borderpad=2,
        )
