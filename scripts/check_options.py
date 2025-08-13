import os

import papermill as pm
import yaml


def check_notebook_options(notebook_filename):
    notebook_path = f"./moderne_visualizations_misc/{notebook_filename}"
    nb_options = pm.inspect_notebook(notebook_path)
    option_names = set(nb_options.keys())

    spec__path = f"./moderne_visualizations_misc/specs/{notebook_filename.replace('.ipynb', '.yml')}"

    spec_option_names = set()
    with open(spec__path, "r") as stream:
        try:
            spec = yaml.safe_load(stream)
            options = spec.get("options", [])
            spec_option_names = set([list(item.keys())[0] for item in options])
        except yaml.YAMLError as exc:
            print(exc)

    return option_names == spec_option_names, option_names, spec_option_names


print("\nCheck notebook options and spec file options match")
print("-----------------------------------------------------------------------------")

# get list of all notebooks in the moderne_visualizations_misc directory
notebook_filenames = [
    filename
    for filename in os.listdir("./moderne_visualizations_misc")
    if filename.endswith(".ipynb")
]

exit_code = 0

for notebook_filename in notebook_filenames:
    matches, notebook_options, spec_options = check_notebook_options(notebook_filename)
    if matches:
        print(f"✅ {notebook_filename}")
    else:
        print(f"❌ {notebook_filename}")

        # Show options that are in notebook but not in spec
        notebook_only = notebook_options - spec_options
        if notebook_only:
            print(f"   Options in notebook but not in spec: {sorted(notebook_only)}")

        # Show options that are in spec but not in notebook
        spec_only = spec_options - notebook_options
        if spec_only:
            print(f"   Options in spec but not in notebook: {sorted(spec_only)}")

        exit_code = 1

exit(exit_code)
exit(exit_code)
