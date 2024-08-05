from code_data_science import data_table as dt
from code_data_science.versions import index as index_versions
import plotly.graph_objects as go
import code_data_science.palette as palette

def create_violin_plot():
    df = dt.read_csv("../samples/dependency_usage_violin_nodejs.csv")
    df = df[["name", "requestedVersion"]]

    # make sure version is a string
    df["requestedVersion"] = df["requestedVersion"].astype(str)
    df["version"] = list(
        map(
            lambda v: v.removeprefix("^")
            .removeprefix("~")
            .removeprefix(">")
            .removeprefix("="),
            df.requestedVersion,
        )
    )

    vmap = index_versions(df.version)
    df["nVersion"] = list(map(lambda v: vmap[v], df.version))

    def index_name(names):
        sorted_names = sorted(list(set(names)))
        return {name: sorted_names.index(name) for name in sorted_names}

    nmap = index_name(df.name)
    df["nName"] = list(map(lambda g: nmap[g], df.name))

    df = df.sort_values(by=["nVersion", "nName"])

    colors = palette.colors_by_weight(500)

    fig = go.Figure()

    # Add a trace to the plot for each category
    for i, category in enumerate(df["nName"].unique()):
        category_data = df[df["nName"] == category]

        # Calculate counts for each dependency and version combination
        counts = (
            category_data.groupby("nVersion")["nName"].count().reset_index(name="count")
        )

        category_data_with_counts = category_data.merge(counts, on="nVersion")

        # Generate hover text including the count information
        hover_text = category_data_with_counts.apply(
            lambda row: f'<b>Package</b>: {row["name"]}<br><b>Version</b>: {row["version"]}<br><b>Count</b>: {row["count"]}',
            axis=1,
        )

        fig.add_trace(
            go.Scatter(
                x=category_data["nName"],
                y=category_data["nVersion"],
                mode="markers",
                marker=dict(color=colors[i % len(colors)], size=8),
                showlegend=False,
                name="",
                text=hover_text,
                hoverinfo="text",
                hoverlabel=dict(font=dict(size=18)),
            )
        )

        fig.add_trace(
            go.Violin(
                x=category_data["nName"],
                y=category_data["nVersion"],
                fillcolor="black",
                opacity=0.15,
                line_color="black",
                showlegend=False,
                width=0.7,
                bandwidth=0.4,
                hoverinfo="none",
                hoveron="points",
            )
        )

    num_versions = df["nVersion"].nunique()
    height_per_version = 32
    width_per_dependency = 80
    fig_height = max(num_versions * height_per_version, 900)
    fig_width = max(len(list(nmap.values())) * width_per_dependency, 900)
    tick_font_size = 13
    # Customizing the layout
    fig.update_layout(
        title="Package versions in use",
        xaxis_title="Packages",
        yaxis_title="Versions",
        height=fig_height,
        width=fig_width,
        xaxis=dict(
            tickfont=dict(size=tick_font_size),
            tickmode="array",
            tickvals=list(nmap.values()),
            ticktext=list(nmap.keys()),
        ),
        yaxis=dict(
            tickfont=dict(size=tick_font_size),
            tickmode="array",
            tickvals=list(vmap.values()),
            ticktext=list(vmap.keys()),
        ),
    )

    fig.show()
