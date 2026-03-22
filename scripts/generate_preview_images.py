"""Generate 400x300 preview PNG images for the 12 code quality visualizations."""

import os
import sys
import warnings

warnings.simplefilter("ignore")

# Ensure we can import from the package
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from moderne_visualizations_misc.reusable import quality_utils as qu

SAMPLES = os.path.join(os.path.dirname(__file__), "..", "samples")
IMAGES = os.path.join(
    os.path.dirname(__file__), "..", "moderne_visualizations_misc", "images"
)
WIDTH = 400
HEIGHT = 300


def read_csv(name: str) -> pd.DataFrame:
    return pd.read_csv(os.path.join(SAMPLES, name))


def save(fig: go.Figure, name: str) -> None:
    path = os.path.join(IMAGES, f"{name}.300.png")
    fig.update_layout(
        margin=dict(l=30, r=15, t=35, b=30),
        font=dict(size=8),
        width=WIDTH,
        height=HEIGHT,
    )
    fig.write_image(path, width=WIDTH, height=HEIGHT, scale=2)
    print(f"  saved {path}")


# ---------------------------------------------------------------------------
# 1. Architectural Stability Scatter
# ---------------------------------------------------------------------------
def gen_architectural_stability_scatter() -> None:
    print("1. architectural_stability_scatter")
    df = read_csv("package_quality_metrics.csv")
    df = qu.add_repo_short(df)

    required = ["instability", "abstractness"]
    missing = [c for c in required if c not in df.columns]
    if missing or len(df) == 0:
        save(qu.empty_figure(), "architectural_stability_scatter")
        return

    df["inCycle"] = df.get("inCycle", pd.Series([False] * len(df)))
    marker_symbol = df["inCycle"].map({True: "star", False: "circle"}).fillna("circle")

    fig = go.Figure()
    # Main sequence line
    fig.add_trace(
        go.Scatter(
            x=[0, 1], y=[1, 0], mode="lines",
            line=dict(dash="dash", color="#999", width=1),
            showlegend=False,
        )
    )
    # Zone shading
    fig.add_shape(type="rect", x0=0, y0=0, x1=0.3, y1=0.3,
                  fillcolor="rgba(239,83,80,0.08)", line=dict(width=0))
    fig.add_shape(type="rect", x0=0.7, y0=0.7, x1=1, y1=1,
                  fillcolor="rgba(255,193,7,0.08)", line=dict(width=0))
    fig.add_trace(
        go.Scatter(
            x=df["instability"], y=df["abstractness"],
            mode="markers",
            marker=dict(
                size=6, color=df.get("distanceFromMainSequence", df["instability"]),
                colorscale="RdYlGn_r", showscale=False,
                symbol=marker_symbol, line=dict(width=0.5, color="#333"),
            ),
            showlegend=False,
        )
    )
    fig.update_layout(
        title="Package Stability vs Abstractness",
        xaxis_title="Instability", yaxis_title="Abstractness",
        xaxis=dict(range=[-0.05, 1.05]), yaxis=dict(range=[-0.05, 1.05]),
        plot_bgcolor="white",
    )
    # Zone labels
    fig.add_annotation(x=0.15, y=0.15, text="Zone of<br>Pain", showarrow=False,
                       font=dict(size=7, color="#999"))
    fig.add_annotation(x=0.85, y=0.85, text="Zone of<br>Uselessness", showarrow=False,
                       font=dict(size=7, color="#999"))
    save(fig, "architectural_stability_scatter")


# ---------------------------------------------------------------------------
# 2. Code Quality Data Grid
# ---------------------------------------------------------------------------
def gen_code_quality_data_grid() -> None:
    print("2. code_quality_data_grid")
    df = read_csv("method_quality_metrics.csv")
    df = qu.add_repo_short(df)
    df = qu.add_class_short(df)

    # Show a representative table preview
    cols = ["classShort", "methodName", "cyclomaticComplexity", "cognitiveComplexity",
            "lineCount", "parameterCount"]
    available = [c for c in cols if c in df.columns]
    preview = df[available].head(8)

    headers = ["Class", "Method", "Cyclo", "Cogn", "Lines", "Params"]
    headers = headers[: len(available)]

    fig = go.Figure(
        data=[
            go.Table(
                header=dict(
                    values=headers,
                    fill_color="#4a90d9",
                    font=dict(color="white", size=9),
                    align="left",
                    height=22,
                ),
                cells=dict(
                    values=[preview[c].tolist() for c in available],
                    fill_color=[["white", "#f5f5f5"] * 4],
                    font=dict(size=8),
                    align="left",
                    height=20,
                ),
            )
        ]
    )
    fig.update_layout(title="Code Quality Metrics Data Grid")
    save(fig, "code_quality_data_grid")


# ---------------------------------------------------------------------------
# 3. Code Quality Executive Dashboard
# ---------------------------------------------------------------------------
def gen_code_quality_executive_dashboard() -> None:
    print("3. code_quality_executive_dashboard")
    df = read_csv("class_quality_metrics.csv")
    df = qu.add_repo_short(df)

    if len(df) == 0 or "maintainabilityIndex" not in df.columns:
        save(qu.empty_figure(), "code_quality_executive_dashboard")
        return

    repo_health = (
        df.groupby("repoShort")["maintainabilityIndex"]
        .mean()
        .sort_values()
        .tail(10)
    )

    colors = [
        "#EF5350" if v < 30 else "#FF8A65" if v < 50 else "#A5D6A7" if v < 70 else "#4CAF50"
        for v in repo_health.values
    ]

    fig = go.Figure()
    fig.add_trace(
        go.Bar(x=repo_health.index, y=repo_health.values,
               marker_color=colors, showlegend=False)
    )
    # Add a health score annotation
    avg_health = df["maintainabilityIndex"].mean()
    health_color = "#EF5350" if avg_health < 30 else "#FF8A65" if avg_health < 50 else "#4CAF50"
    fig.add_annotation(
        x=0.98, y=0.95, xref="paper", yref="paper",
        text=f"<b>Portfolio Health: {avg_health:.0f}</b>",
        showarrow=False, font=dict(size=10, color=health_color),
        bgcolor="white", bordercolor=health_color, borderwidth=1,
        xanchor="right",
    )
    fig.update_layout(
        title="Executive Dashboard",
        yaxis_title="Maintainability Index",
        plot_bgcolor="white",
        xaxis=dict(tickangle=-35, tickfont=dict(size=7)),
    )
    save(fig, "code_quality_executive_dashboard")


# ---------------------------------------------------------------------------
# 4. Code Smell Severity Stacked Bar
# ---------------------------------------------------------------------------
def gen_code_smell_severity_stacked_bar() -> None:
    print("4. code_smell_severity_stacked_bar")
    df = read_csv("code_smells.csv")
    df = qu.add_repo_short(df)

    if len(df) == 0 or "severity" not in df.columns:
        save(qu.empty_figure(), "code_smell_severity_stacked_bar")
        return

    severity_colors = {"critical": "#D32F2F", "high": "#EF5350", "medium": "#FFB74D", "low": "#A5D6A7"}
    severity_order = ["critical", "high", "medium", "low"]
    df["severity"] = df["severity"].str.lower()

    pivot = df.groupby(["repoShort", "severity"]).size().unstack(fill_value=0)
    pivot = pivot.reindex(columns=[s for s in severity_order if s in pivot.columns])
    pivot = pivot.loc[pivot.sum(axis=1).nlargest(12).index]

    fig = go.Figure()
    for sev in pivot.columns:
        fig.add_trace(
            go.Bar(y=pivot.index, x=pivot[sev], name=sev.title(),
                   orientation="h", marker_color=severity_colors.get(sev, "#999"))
        )
    fig.update_layout(
        barmode="stack", title="Code Smell Distribution",
        xaxis_title="Count", plot_bgcolor="white",
        legend=dict(font=dict(size=7), orientation="h", y=1.12),
    )
    save(fig, "code_smell_severity_stacked_bar")


# ---------------------------------------------------------------------------
# 5. Complexity vs Test Gaps Bubble
# ---------------------------------------------------------------------------
def gen_complexity_vs_test_gaps_bubble() -> None:
    print("5. complexity_vs_test_gaps_bubble")
    df_class = read_csv("class_quality_metrics.csv")
    df_gaps = read_csv("test_gaps.csv")
    df_class = qu.add_repo_short(df_class)
    df_class = qu.add_class_short(df_class)

    if "wmc" not in df_class.columns:
        save(qu.empty_figure(), "complexity_vs_test_gaps_bubble")
        return

    # Join on className if possible
    if "className" in df_gaps.columns and "className" in df_class.columns:
        gap_counts = df_gaps.groupby("className").size().reset_index(name="untested_methods")
        df = df_class.merge(gap_counts, on="className", how="left")
        df["untested_methods"] = df["untested_methods"].fillna(0)
    else:
        df = df_class.copy()
        df["untested_methods"] = 0

    df = df[df["wmc"] >= 5]
    if len(df) == 0:
        save(qu.empty_figure(), "complexity_vs_test_gaps_bubble")
        return

    mi = df.get("maintainabilityIndex", pd.Series([50] * len(df)))
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=df["wmc"], y=df["untested_methods"], mode="markers",
            marker=dict(
                size=df["wmc"].clip(upper=40) / 3 + 4,
                color=mi, colorscale="RdYlGn", showscale=True,
                colorbar=dict(title="MI", thickness=10, len=0.6),
                line=dict(width=0.5, color="#333"),
            ),
            showlegend=False,
        )
    )
    # Quadrant lines
    med_x = df["wmc"].median()
    med_y = df["untested_methods"].median()
    fig.add_hline(y=med_y, line=dict(dash="dot", color="#ccc", width=1))
    fig.add_vline(x=med_x, line=dict(dash="dot", color="#ccc", width=1))
    fig.update_layout(
        title="Complexity vs Test Gaps",
        xaxis_title="WMC", yaxis_title="Untested Methods",
        plot_bgcolor="white",
    )
    save(fig, "complexity_vs_test_gaps_bubble")


# ---------------------------------------------------------------------------
# 6. Coupling Cohesion Quadrant
# ---------------------------------------------------------------------------
def gen_coupling_cohesion_quadrant() -> None:
    print("6. coupling_cohesion_quadrant")
    df = read_csv("class_quality_metrics.csv")
    df = qu.add_repo_short(df)
    df = qu.add_class_short(df)

    required = ["cbo", "tcc"]
    missing = [c for c in required if c not in df.columns]
    if missing or len(df) == 0:
        save(qu.empty_figure(), "coupling_cohesion_quadrant")
        return

    coupling_t, cohesion_t = 10, 0.5
    mi = df.get("maintainabilityIndex", pd.Series([50] * len(df)))

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=df["cbo"], y=df["tcc"], mode="markers",
            marker=dict(
                size=df.get("wmc", pd.Series([10] * len(df))).clip(upper=60) / 5 + 3,
                color=mi, colorscale="RdYlGn", showscale=False,
                line=dict(width=0.3, color="#555"),
            ),
            showlegend=False,
        )
    )
    fig.add_hline(y=cohesion_t, line=dict(dash="dot", color="#999", width=1))
    fig.add_vline(x=coupling_t, line=dict(dash="dot", color="#999", width=1))

    max_x = min(df["cbo"].quantile(0.98) * 1.1, df["cbo"].max() * 1.1)
    labels = [
        (coupling_t / 2, cohesion_t / 2, "Island"),
        (coupling_t / 2, (1 + cohesion_t) / 2, "Healthy"),
        (coupling_t + (max_x - coupling_t) / 2, cohesion_t / 2, "Spaghetti"),
        (coupling_t + (max_x - coupling_t) / 2, (1 + cohesion_t) / 2, "Hub"),
    ]
    for lx, ly, lt in labels:
        fig.add_annotation(x=lx, y=ly, text=lt, showarrow=False,
                           font=dict(size=7, color="#aaa"))

    fig.update_layout(
        title="Coupling vs Cohesion",
        xaxis_title="Coupling (CBO)", yaxis_title="Cohesion (TCC)",
        xaxis=dict(range=[0, max_x]), yaxis=dict(range=[-0.05, 1.05]),
        plot_bgcolor="white",
    )
    save(fig, "coupling_cohesion_quadrant")


# ---------------------------------------------------------------------------
# 7. Dependency Cycle Network
# ---------------------------------------------------------------------------
def gen_dependency_cycle_network() -> None:
    print("7. dependency_cycle_network")
    df = read_csv("package_quality_metrics.csv")

    if "cycleMembers" not in df.columns or "packageName" not in df.columns:
        save(qu.empty_figure(), "dependency_cycle_network")
        return

    import networkx as nx

    cycle_df = df[df["inCycle"] == True] if "inCycle" in df.columns else df[df["cycleMembers"].notna()]

    G = nx.DiGraph()
    for _, row in cycle_df.iterrows():
        pkg = row["packageName"]
        G.add_node(pkg)
        if pd.notna(row.get("cycleMembers")):
            for member in str(row["cycleMembers"]).split(","):
                member = member.strip()
                if member and member != pkg:
                    G.add_node(member)
                    G.add_edge(pkg, member)

    if len(G.nodes) == 0:
        save(qu.empty_figure("No dependency cycles found"), "dependency_cycle_network")
        return

    pos = nx.spring_layout(G, seed=42, k=2.0)

    edge_x, edge_y = [], []
    for u, v in G.edges():
        x0, y0 = pos[u]
        x1, y1 = pos[v]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])

    node_x = [pos[n][0] for n in G.nodes()]
    node_y = [pos[n][1] for n in G.nodes()]
    labels = [n.split(".")[-1] for n in G.nodes()]

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(x=edge_x, y=edge_y, mode="lines",
                   line=dict(width=1, color="#EF5350"), showlegend=False)
    )
    fig.add_trace(
        go.Scatter(
            x=node_x, y=node_y, mode="markers+text",
            marker=dict(size=10, color="#EF5350", line=dict(width=1, color="#333")),
            text=labels, textposition="top center", textfont=dict(size=6),
            showlegend=False,
        )
    )
    fig.update_layout(
        title="Dependency Cycle Network",
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        plot_bgcolor="white",
    )
    save(fig, "dependency_cycle_network")


# ---------------------------------------------------------------------------
# 8. Method Risk Radar
# ---------------------------------------------------------------------------
def gen_method_risk_radar() -> None:
    print("8. method_risk_radar")
    df = read_csv("method_quality_metrics.csv")
    df = qu.add_repo_short(df)
    df = qu.add_class_short(df)

    radar_metrics = [
        "cyclomaticComplexity", "cognitiveComplexity",
        "maxNestingDepth", "parameterCount", "halsteadEstimatedBugs",
    ]
    available = [m for m in radar_metrics if m in df.columns]
    if len(available) < 3 or len(df) == 0:
        save(qu.empty_figure(), "method_risk_radar")
        return

    df = df.dropna(subset=["className", "methodName"])
    norm = df[available].copy()
    for col in available:
        mx = norm[col].max()
        norm[col] = norm[col] / mx if mx > 0 else 0
    df["risk"] = norm.mean(axis=1)
    top = df.nlargest(5, "risk")

    labels = [m.replace("Complexity", "").replace("halstead", "Halstead")[:10] for m in available]
    colors = ["#EF5350", "#42A5F5", "#66BB6A", "#FFA726", "#AB47BC"]

    fig = go.Figure()
    for i, (_, row) in enumerate(top.iterrows()):
        vals = [norm.loc[row.name, c] for c in available]
        vals_closed = vals + [vals[0]]
        labels_closed = labels + [labels[0]]
        cn = str(row.get("classShort", "") or "")
        mn = str(row.get("methodName", "") or "")
        fig.add_trace(
            go.Scatterpolar(
                r=vals_closed, theta=labels_closed,
                fill="toself", fillcolor=f"rgba{tuple(list(int(colors[i][j:j+2], 16) for j in (1,3,5)) + [0.12])}",
                line=dict(color=colors[i], width=1.5),
                name=f"{cn}.{mn}"[:20] if cn else mn[:20],
            )
        )
    fig.update_layout(
        title="Method Risk Radar",
        polar=dict(radialaxis=dict(visible=True, range=[0, 1], tickfont=dict(size=6))),
        legend=dict(font=dict(size=6), y=-0.15, orientation="h"),
    )
    save(fig, "method_risk_radar")


# ---------------------------------------------------------------------------
# 9. Portfolio Health Sunburst
# ---------------------------------------------------------------------------
def gen_portfolio_health_sunburst() -> None:
    print("9. portfolio_health_sunburst")
    df = read_csv("class_quality_metrics.csv")
    df = qu.add_repo_short(df)
    df = qu.add_class_short(df)

    if len(df) == 0 or "maintainabilityIndex" not in df.columns:
        save(qu.empty_figure(), "portfolio_health_sunburst")
        return

    df = df.dropna(subset=["className", "lineCount"])
    df = df[df["lineCount"] > 0]
    df["package"] = df["package"].fillna("(default)") if "package" in df.columns else "(default)"

    repo_counts = df.groupby("repoShort").size().nlargest(10)
    df = df[df["repoShort"].isin(repo_counts.index)]

    df["package"] = df["package"].apply(
        lambda p: ".".join(str(p).split(".")[-2:]) if len(str(p).split(".")) > 2 else str(p)
    )

    fig = px.sunburst(
        df,
        path=["repoShort", "package", "classShort"],
        values="lineCount",
        color="maintainabilityIndex",
        color_continuous_scale=["#EF5350", "#FF8A65", "#FFE082", "#A5D6A7", "#4CAF50"],
        color_continuous_midpoint=50,
    )
    fig.update_layout(title="Portfolio Code Health")
    save(fig, "portfolio_health_sunburst")


# ---------------------------------------------------------------------------
# 10. Portfolio Quality Comparison Violin
# ---------------------------------------------------------------------------
def gen_portfolio_quality_comparison_violin() -> None:
    print("10. portfolio_quality_comparison_violin")
    df = read_csv("method_quality_metrics.csv")
    df = qu.add_repo_short(df)
    metric = "cyclomaticComplexity"

    if len(df) == 0 or metric not in df.columns:
        save(qu.empty_figure(), "portfolio_quality_comparison_violin")
        return

    repo_medians = df.groupby("repoShort")[metric].median().sort_values(ascending=False)
    top_repos = repo_medians.head(8).index.tolist()
    med_min, med_max = repo_medians.min(), repo_medians.max()
    med_range = med_max - med_min if med_max > med_min else 1
    cap = df[metric].quantile(0.95)

    fig = go.Figure()
    for repo in top_repos:
        repo_data = df[df["repoShort"] == repo][metric].clip(upper=cap)
        median_val = repo_medians[repo]
        norm = (median_val - med_min) / med_range
        r = int(76 + norm * (239 - 76))
        g = int(175 + norm * (83 - 175))
        fig.add_trace(
            go.Violin(
                y=repo_data, name=repo[:12],
                box_visible=True, meanline_visible=True, points=False,
                fillcolor=f"rgb({r},{g},80)", line_color="#333", opacity=0.75,
            )
        )
    fig.update_layout(
        title="Quality Distribution: Cyclomatic Complexity",
        showlegend=False, plot_bgcolor="white",
        xaxis=dict(tickangle=-35, tickfont=dict(size=6)),
    )
    save(fig, "portfolio_quality_comparison_violin")


# ---------------------------------------------------------------------------
# 11. Technical Debt Treemap
# ---------------------------------------------------------------------------
def gen_technical_debt_treemap() -> None:
    print("11. technical_debt_treemap")
    df = read_csv("method_quality_metrics.csv")
    df = qu.add_repo_short(df)
    df = qu.add_class_short(df)

    if len(df) == 0:
        save(qu.empty_figure(), "technical_debt_treemap")
        return

    # Compute debt score
    score_cols = ["cyclomaticComplexity", "cognitiveComplexity", "maxNestingDepth"]
    available = [c for c in score_cols if c in df.columns]
    if not available:
        save(qu.empty_figure(), "technical_debt_treemap")
        return

    norm = df[available].copy()
    for col in available:
        mx = norm[col].max()
        norm[col] = norm[col] / mx if mx > 0 else 0
    df["debtScore"] = norm.mean(axis=1) * 100

    df = df.dropna(subset=["methodName", "classShort"])
    df["lineCount"] = df.get("lineCount", pd.Series([10] * len(df))).clip(lower=1)
    top = df.nlargest(100, "debtScore")

    fig = px.treemap(
        top,
        path=["repoShort", "classShort", "methodName"],
        values="lineCount",
        color="debtScore",
        color_continuous_scale=["#A5D6A7", "#FFE082", "#FF8A65", "#EF5350"],
    )
    fig.update_layout(title="Technical Debt Hotspots")
    save(fig, "technical_debt_treemap")


# ---------------------------------------------------------------------------
# 12. Test Gap Risk Heatmap
# ---------------------------------------------------------------------------
def gen_test_gap_risk_heatmap() -> None:
    print("12. test_gap_risk_heatmap")
    df = read_csv("test_gaps.csv")
    df = qu.add_repo_short(df)

    if len(df) == 0 or "riskScore" not in df.columns:
        save(qu.empty_figure(), "test_gap_risk_heatmap")
        return

    bins = [0, 25, 50, 75, 100]
    labels = ["Low", "Medium", "High", "Critical"]
    df["riskBucket"] = pd.cut(df["riskScore"], bins=bins, labels=labels, include_lowest=True)

    top_repos = df.groupby("repoShort").size().nlargest(15).index
    df = df[df["repoShort"].isin(top_repos)]

    pivot = df.groupby(["repoShort", "riskBucket"]).size().unstack(fill_value=0)
    pivot = pivot.reindex(columns=labels, fill_value=0)
    # Sort by total descending
    pivot = pivot.loc[pivot.sum(axis=1).sort_values(ascending=True).index]

    fig = go.Figure(
        data=go.Heatmap(
            z=pivot.values, x=pivot.columns.tolist(), y=pivot.index.tolist(),
            colorscale=[[0, "#E8F5E9"], [0.33, "#FFE082"], [0.66, "#FF8A65"], [1, "#D32F2F"]],
            showscale=True, colorbar=dict(thickness=10, len=0.6),
        )
    )
    fig.update_layout(
        title="Test Gap Risk by Repository",
        xaxis_title="Risk Level",
        plot_bgcolor="white",
    )
    save(fig, "test_gap_risk_heatmap")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    generators = [
        gen_architectural_stability_scatter,
        gen_code_quality_data_grid,
        gen_code_quality_executive_dashboard,
        gen_code_smell_severity_stacked_bar,
        gen_complexity_vs_test_gaps_bubble,
        gen_coupling_cohesion_quadrant,
        gen_dependency_cycle_network,
        gen_method_risk_radar,
        gen_portfolio_health_sunburst,
        gen_portfolio_quality_comparison_violin,
        gen_technical_debt_treemap,
        gen_test_gap_risk_heatmap,
    ]
    for gen in generators:
        try:
            gen()
        except Exception as e:
            print(f"  ERROR: {e}")
