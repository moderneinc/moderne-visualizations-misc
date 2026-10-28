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
    for ring, r in enumerate((40, 70, 110, 160, 220))
    for dx, dy in (
        (1, -0.6),
        (-1, -0.6),
        (1, 0.6),
        (-1, 0.6),
        (1.2, 0),
        (-1.2, 0),
        (0, -0.8),
        (0, 0.8),
        (0.5, -0.8),
        (-0.5, -0.8),
        (0.5, 0.8),
        (-0.5, 0.8),
    )
]


Box = tuple[float, float, float, float]
Segment = tuple[float, float, float, float]


def _boxes_overlap(a: Box, b: Box) -> bool:
    return a[0] < b[2] and b[0] < a[2] and a[1] < b[3] and b[1] < a[3]


def _segment_hits_box(seg: Segment, box: Box) -> bool:
    x0, y0, x1, y1 = seg
    return any(
        box[0] < x0 + (x1 - x0) * t < box[2] and box[1] < y0 + (y1 - y0) * t < box[3]
        for t in (0.15, 0.3, 0.45, 0.6, 0.75)
    )


def _segments_cross(a: Segment, b: Segment) -> bool:
    def side(ox: float, oy: float, ax: float, ay: float, bx: float, by: float) -> float:
        return (ax - ox) * (by - oy) - (ay - oy) * (bx - ox)

    d1 = side(b[0], b[1], b[2], b[3], a[0], a[1])
    d2 = side(b[0], b[1], b[2], b[3], a[2], a[3])
    d3 = side(a[0], a[1], a[2], a[3], b[0], b[1])
    d4 = side(a[0], a[1], a[2], a[3], b[2], b[3])
    return d1 * d2 < 0 and d3 * d4 < 0


def add_point_labels(
    fig: go.Figure,
    x: pd.Series,
    y: pd.Series,
    sizes: pd.Series,
    labels: pd.Series,
    captions: pd.Series,
    plot_width: float,
    plot_height: float,
    x_range: tuple[float, float] | None = None,
    y_range: tuple[float, float] | None = None,
    keep_clear: list[tuple[float, float, float, float]] | None = None,
) -> None:
    """Label selected scatter points on the chart itself, so they survive static exports.

    `x`, `y` and `sizes` cover every plotted point; `labels` is indexed by the rows to
    label, highest priority first, and `captions` adds a smaller second line. Pins both
    axis ranges (padded to fit the bubbles unless given) so bubble and label positions
    can be computed in pixels. `keep_clear` lists other in-plot text as
    `(x0, y0, x1, y1)` boxes in paper coordinates. Each label takes the leader-line
    offset that stays inside the plot and whose label and leader avoid labeled bubbles,
    `keep_clear` and labels already placed, trading other bubbles covered against
    leader length.
    """
    if x_range is None or y_range is None:
        pad = sizes.max() / 2 + 10
        x_span = (x.max() - x.min()) or 1
        y_span = (y.max() - y.min()) or 1
        x_pad = x_span * pad / (plot_width - 2 * pad)
        y_pad = y_span * pad / (plot_height - 2 * pad)
        x_range = x_range or (x.min() - x_pad, x.max() + x_pad)
        y_range = y_range or (y.min() - y_pad, y.max() + y_pad)
    fig.update_xaxes(range=list(x_range))
    fig.update_yaxes(range=list(y_range))
    px = (x - x_range[0]) / (x_range[1] - x_range[0]) * plot_width
    py = (y_range[1] - y) / (y_range[1] - y_range[0]) * plot_height
    radius = sizes / 2

    bubbles = {
        i: (px[i] - radius[i], py[i] - radius[i], px[i] + radius[i], py[i] + radius[i])
        for i in labels.index
    }
    reserved: list[Box] = [
        (
            x0 * plot_width,
            (1 - y1) * plot_height,
            x1 * plot_width,
            (1 - y0) * plot_height,
        )
        for x0, y0, x1, y1 in keep_clear or []
    ]
    half_sizes = {
        i: (max(3.4 * len(labels[i]), 3.1 * len(captions[i])) + 4, 18)
        for i in labels.index
    }
    offsets: dict = {}

    def label_box(i, dx: float, dy: float) -> Box:
        half_w, half_h = half_sizes[i]
        cx, cy = px[i] + dx, py[i] + dy
        return cx - half_w, cy - half_h, cx + half_w, cy + half_h

    def best_offset(i) -> tuple[float, float]:
        others = reserved + [b for j, b in bubbles.items() if j != i]
        others += [label_box(j, *o) for j, o in offsets.items() if j != i]
        leaders = [
            (px[j], py[j], px[j] + o[0], py[j] + o[1])
            for j, o in offsets.items()
            if j != i
        ]
        best: tuple[tuple[int, int], tuple[float, float]] | None = None
        for ring, dx, dy in _LABEL_OFFSETS:
            box = label_box(i, dx, dy)
            if box[0] < 0 or box[1] < 0 or box[2] > plot_width or box[3] > plot_height:
                continue
            leader = (px[i], py[i], px[i] + dx, py[i] + dy)
            clashes = (
                3 * _boxes_overlap(box, bubbles[i])
                + 3 * sum(_boxes_overlap(box, b) for b in others)
                + sum(_segment_hits_box(leader, b) for b in others)
                + sum(_segments_cross(leader, s) for s in leaders)
            )
            covered = int(
                (
                    (px + radius > box[0])
                    & (px - radius < box[2])
                    & (py + radius > box[1])
                    & (py - radius < box[3])
                ).sum()
            )
            score = (clashes, 8 * ring + covered)
            if best is None or score < best[0]:
                best = (score, (dx, dy))
        return best[1] if best else _LABEL_OFFSETS[0][1:]

    # A greedy first pass, then re-place each label knowing where all the others went.
    for _ in range(3):
        for i in labels.index:
            offsets[i] = best_offset(i)

    for i, label in labels.items():
        dx, dy = offsets[i]
        fig.add_annotation(
            x=x[i],
            y=y[i],
            text=f'{label}<br><span style="font-size:10px;color:#7f7f7f">{captions[i]}</span>',
            align="left" if dx > 0 else "right" if dx < 0 else "center",
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
