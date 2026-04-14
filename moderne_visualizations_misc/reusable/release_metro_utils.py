import networkx as nx
import pandas as pd


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
    artifact_to_repo: dict[str, str] = {}
    for _, row in coords_df.iterrows():
        key = f"{row['groupId']}:{row['artifactId']}"
        repo = str(row["repositoryPath"])
        if key not in artifact_to_repo:
            artifact_to_repo[key] = repo

    # Collect edges keyed by (producer_repo, consumer_repo) -> edge_type
    edges: dict[tuple[str, str], str] = {}

    # --- dependency edges ---
    for _, row in deps_df.iterrows():
        consumer_repo = str(row["repositoryPath"])
        dep_key = f"{row['groupId']}:{row['artifactId']}"
        producer_repo = artifact_to_repo.get(dep_key)
        if producer_repo and producer_repo != consumer_repo:
            edges.setdefault((producer_repo, consumer_repo), "dependency")

    # --- parent edges (override dependency if both exist) ---
    for _, row in parents_df.iterrows():
        child_repo = str(row["repositoryPath"])
        parent_key = f"{row['parentGroupId']}:{row['parentArtifactId']}"
        parent_repo = artifact_to_repo.get(parent_key)
        if parent_repo and parent_repo != child_repo:
            edges[(parent_repo, child_repo)] = "parent"

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
