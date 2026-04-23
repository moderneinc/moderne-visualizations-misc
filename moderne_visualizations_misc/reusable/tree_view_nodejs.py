from moderne_visualizations_misc.reusable.data_loader import read_data_table
from code_data_science import (
    data_table as dt,
    unique_dictionaries as ud,
    tree_data_grid,
)


def dataframe_to_tree(df):
    df["repositoryPath"].fillna("", inplace=True)
    df["version"].fillna("", inplace=True)
    df["requestedVersion"].fillna("", inplace=True)

    tree = ud.UniqueDictionaries()

    for _, row in df.iterrows():
        parent_path = row["repositoryPath"]
        child_name = row["name"]

        tree.add(
            {
                "path": (parent_path, child_name),
                "version": f"{row['requestedVersion']}",
            }
        )

    return tree.to_list()


def create_tree_view():
    # df = read_data_table("../samples/dependency_tree_view_nodejs.csv")
    df = read_data_table("../samples/v2/org.openrewrite.nodejs.table.DependenciesInUse.csv")
    df = df.drop_duplicates(subset=["repositoryPath", "name"])
    tree_data = dataframe_to_tree(df)

    tree_data_grid.display(
        tree_data,
        "Projects",
        [
            {"field": "version", "headerName": "Version requested", "minWidth": 200},
        ],
    )