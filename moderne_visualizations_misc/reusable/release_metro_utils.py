import networkx as nx
import pandas as pd

# Scopes that determine release ordering. A test-only dependency does not
# require the producer to be released first, so test scopes are excluded —
# otherwise mutual `test`-scoped deps between two repos register as a cycle.
# Includes Gradle resolved configurations and Maven scopes; rows with no
# scope value are kept (treated as production by default).
_RELEASE_SCOPES = frozenset(
    {
        "compileClasspath",
        "runtimeClasspath",
        "compile",
        "runtime",
        "provided",
        "system",
    }
)


def build_release_graph(
    coords_df: pd.DataFrame,
    deps_df: pd.DataFrame,
    parents_df: pd.DataFrame,
) -> nx.DiGraph:
    """Build a repo-level directed dependency graph from the three ReleaseMetroPlan tables.

    Edge direction: producer -> consumer (the repo that is depended-on points to the
    repo that depends on it).  This matches the convention in repository_release_order.
    """
    # Map groupId:artifactId -> repositoryPath for all known project artifacts
    coords = coords_df.copy()
    coords["_key"] = coords["groupId"].astype(str) + ":" + coords["artifactId"].astype(str)
    artifact_to_repo: dict[str, str] = (
        coords.drop_duplicates(subset="_key", keep="first")
        .set_index("_key")["repositoryPath"]
        .astype(str)
        .to_dict()
    )

    # Collect edges keyed by (producer_repo, consumer_repo) -> edge_type
    edges: dict[tuple[str, str], str] = {}

    # --- dependency edges ---
    if len(deps_df) > 0:
        deps = deps_df.copy()
        if "scope" in deps.columns:
            scope = deps["scope"].astype(str)
            deps = deps[scope.isin(_RELEASE_SCOPES) | (scope == "nan") | (scope == "")]
        deps["_key"] = deps["groupId"].astype(str) + ":" + deps["artifactId"].astype(str)
        deps["_producer"] = deps["_key"].map(artifact_to_repo)
        deps["_consumer"] = deps["repositoryPath"].astype(str)
        internal = deps.dropna(subset=["_producer"])
        internal = internal[internal["_producer"] != internal["_consumer"]]
        for pair in internal[["_producer", "_consumer"]].drop_duplicates().itertuples(index=False):
            edges.setdefault((pair[0], pair[1]), "dependency")

    # --- parent edges (override dependency if both exist) ---
    if len(parents_df) > 0:
        par = parents_df.copy()
        par["_key"] = par["parentGroupId"].astype(str) + ":" + par["parentArtifactId"].astype(str)
        par["_parent"] = par["_key"].map(artifact_to_repo)
        par["_child"] = par["repositoryPath"].astype(str)
        internal_par = par.dropna(subset=["_parent"])
        internal_par = internal_par[internal_par["_parent"] != internal_par["_child"]]
        for pair in internal_par[["_parent", "_child"]].drop_duplicates().itertuples(index=False):
            edges[(pair[0], pair[1])] = "parent"

    # Build NetworkX graph
    G = nx.DiGraph()

    # Add all repos from ProjectCoordinates as nodes (even if they have no edges)
    for repo in coords_df["repositoryPath"].unique():
        G.add_node(str(repo))

    for (src, tgt), etype in edges.items():
        G.add_edge(src, tgt, edge_type=etype)

    return G


def compute_release_waves(
    G: nx.DiGraph,
) -> tuple[list[list[str]], list[str]]:
    """Compute release waves via Kahn-style topological grouping.

    Returns (waves, circular_deps) where waves[0] contains repos with no
    internal dependencies and circular_deps lists repos stuck in cycles.
    """
    remaining = set(G.nodes())
    waves: list[list[str]] = []

    while remaining:
        # Nodes whose predecessors (dependencies) are all already released
        wave = [
            n
            for n in remaining
            if all(p not in remaining for p in G.predecessors(n))
        ]
        if not wave:
            break  # remaining nodes are in cycles
        waves.append(sorted(wave))
        remaining -= set(wave)

    circular = sorted(remaining)
    return waves, circular


def cubic_bezier(
    p0: tuple[float, float],
    p1: tuple[float, float],
    p2: tuple[float, float],
    p3: tuple[float, float],
    n: int = 30,
) -> list[tuple[float, float]]:
    """Sample *n+1* points along a cubic Bézier curve."""
    pts: list[tuple[float, float]] = []
    for i in range(n + 1):
        t = i / n
        t1 = 1 - t
        x = t1**3 * p0[0] + 3 * t1**2 * t * p1[0] + 3 * t1 * t**2 * p2[0] + t**3 * p3[0]
        y = t1**3 * p0[1] + 3 * t1**2 * t * p1[1] + 3 * t1 * t**2 * p2[1] + t**3 * p3[1]
        pts.append((x, y))
    return pts
