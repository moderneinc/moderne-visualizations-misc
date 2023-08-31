import os
import papermill as pm
import yaml


def check_notebook_options(notebook_filename):
    notebook_path = f"/Users/kylescully/Repos/visualizations-misc/moderne_visualizations_misc/{notebook_filename}"
    notebook_options = pm.inspect_notebook(notebook_path)
    option_names = list(notebook_options.keys())

    spec__path = f"/Users/kylescully/Repos/visualizations-misc/moderne_visualizations_misc/specs/{notebook_filename.replace('.ipynb', '.yml')}"

    result = None
    with open(spec__path, 'r') as stream:
        try:
            spec = yaml.safe_load(stream)
            options = spec.get("options", [])
            result = [list(item.keys())[0] for item in options]
        except yaml.YAMLError as exc:
            print(exc)

    return set(option_names) == set(result)


print("\nCheck notebook options and spec file options match")
print("-----------------------------------------------------------------------------")

# get list of all notebooks in the moderne_visualizations_misc directory
notebook_filenames = [
    filename for filename in os.listdir('./moderne_visualizations_misc') if filename.endswith(".ipynb")]

exit_code = 0

for notebook_filename in notebook_filenames:
    if check_notebook_options(notebook_filename):
        print(f"✅ {notebook_filename}")
    else:
        print(f"❌ {notebook_filename}")
        exit_code = 1

exit(exit_code)
