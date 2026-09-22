import os
import papermill as pm
import yaml

# The moderne-saas installer defaults an option's GraphQL type to "String" when
# the spec has no `type:` key, so that's the baseline every notebook default
# is checked against here too.
INFERRED_TO_DECLARED_TYPE = {
    "int": "Integer",
    "float": "Number",
    "bool": "Boolean",
}


def load_spec(notebook_filename):
    spec_path = f"./moderne_visualizations_misc/specs/{notebook_filename.replace('.ipynb', '.yml')}"
    with open(spec_path, "r") as stream:
        return yaml.safe_load(stream)


def check_notebook_options(notebook_filename, spec):
    notebook_path = f"./moderne_visualizations_misc/{notebook_filename}"
    notebook_options = pm.inspect_notebook(notebook_path)
    option_names = list(notebook_options.keys())

    options = spec.get("options", [])
    result = [list(item.keys())[0] for item in options]
    additional = spec.get("additionalDataTables", {})
    if additional:
        result += list(additional.keys())

    return set(option_names) == set(result)


def check_option_types(notebook_filename, spec):
    """A numeric or boolean default with no matching declared `type:` silently
    becomes a String option on the SaaS side, and a value submitted as text can
    crash the notebook (e.g. `x >= complexity_threshold` on a str)."""
    notebook_path = f"./moderne_visualizations_misc/{notebook_filename}"
    notebook_options = pm.inspect_notebook(notebook_path)

    declared_types = {}
    for item in spec.get("options", []):
        for name, props in item.items():
            declared_types[name] = (props or {}).get("type")

    mismatches = []
    for name, info in notebook_options.items():
        expected = INFERRED_TO_DECLARED_TYPE.get(info.get("inferred_type_name"))
        if expected and declared_types.get(name, "String") != expected:
            mismatches.append((name, info.get("inferred_type_name"), expected))
    return mismatches


print("\nCheck notebook options and spec file options match")
print("-----------------------------------------------------------------------------")

notebook_filenames = [
    filename
    for filename in os.listdir("./moderne_visualizations_misc")
    if filename.endswith(".ipynb")
]

exit_code = 0

for notebook_filename in notebook_filenames:
    spec = load_spec(notebook_filename)

    if check_notebook_options(notebook_filename, spec):
        print(f"✅ {notebook_filename}")
    else:
        print(f"❌ {notebook_filename}")
        exit_code = 1

    mismatches = check_option_types(notebook_filename, spec)
    for name, inferred, expected in mismatches:
        print(
            f"❌ {notebook_filename}: option '{name}' has a {inferred} default "
            f"but no `type: {expected}` in the spec"
        )
        exit_code = 1

exit(exit_code)
