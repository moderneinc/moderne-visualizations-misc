# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python package (`moderne-visualizations-misc`) that provides data visualizations for the Moderne platform. The package consists of 50+ Jupyter notebooks that create interactive visualizations for code analysis, dependency management, and codebase insights.

## Development Setup

1. **Package Manager**: This project uses `uv` (not pip or poetry directly)
   ```bash
   # Install dependencies
   uv sync --dev
   
   # Activate virtual environment
   source .venv/bin/activate
   ```

2. **Python Version**: Requires Python 3.9+

## Essential Development Commands

### Code Quality Checks
```bash
# Run all checks (recommended before committing)
poe check-all

# Individual checks
poe format          # Auto-format code with ruff
poe lint            # Lint code with ruff  
poe fix             # Auto-fix linting issues with ruff
poe check-types     # Type checking with mypy
poe check-options   # Validate notebook parameters match spec files
poe check-sentence-casing  # Validate proper naming conventions
```

### Running Individual Notebooks
```bash
# Run a specific notebook with papermill (useful for testing)
papermill moderne_visualizations_misc/dependency_tree_view.ipynb output.ipynb -p data_file samples/dependency_tree_view.csv

# Or run from within Jupyter
jupyter notebook
```

### Testing
There are no traditional unit tests. Instead, the project uses:
- Validation scripts to ensure consistency between notebooks and specs
- Sample CSV files in `samples/` for manual testing
- CI/CD checks on pull requests

## Architecture and Structure

### Key Directories
- `moderne_visualizations_misc/` - Main package directory
  - `*.ipynb` - Jupyter notebooks (one per visualization type)
  - `specs/*.yml` - YAML specifications defining metadata for each visualization
  - `images/` - Preview images (300px PNGs) for each visualization
  - `reusable/` - Shared Python modules for common functionality
  - `resources/` - External resources (e.g., plantuml.jar)
- `samples/` - CSV data files for testing visualizations
- `scripts/` - Utility scripts for validation

### Important Patterns

1. **Adding a New Visualization**:
   - Create a new `.ipynb` file in `moderne_visualizations_misc/`
   - Create a corresponding `.yml` spec file in `moderne_visualizations_misc/specs/`
   - Add a preview image in `moderne_visualizations_misc/images/`
   - Ensure the notebook parameters match the spec file options

2. **Notebook Structure**:
   - Each notebook should have parameters defined in the first cell (these are extracted by `papermill`)
   - Parameters must match the options defined in the corresponding spec file (validated by `poe check-options`)
   - Use the reusable modules for common functionality (e.g., `moderne_visualizations_misc.reusable.tree_view_nodejs`)
   - Follow the pattern: data loading → processing → visualization output

3. **Common Imports and Patterns**:
   ```python
   from code_data_science import (
       data_table as dt,
       unique_dictionaries as ud,
       tree_data_grid,
   )
   import pandas as pd
   import plotly.express as px
   # For tree visualizations
   from moderne_visualizations_misc.reusable import tree_view_nodejs, violin_nodejs
   ```

4. **Spec File Format**:
   ```yaml
   ---
   type: specs.moderne.io/v1beta/visualization
   name: io.moderne.YourVisualizationName
   displayName: Your visualization name  # Must be sentence case
   description: >
     Brief description of the visualization.
   recipe: org.openrewrite.recipe.Name
   dataTable: org.openrewrite.recipe.table.TableName
   options:  # Must match notebook parameters
     - paramName:
         displayName: Parameter display name
         description: Parameter description
   ```

## Key Dependencies

- `code-data-science==2.1.2` - Core utilities for Moderne visualizations (data_table, tree_data_grid, etc.)
- `pandas==2.0.3` - Data manipulation
- `plotly==5.14.1` - Interactive visualizations  
- `matplotlib==3.7.1` - Static plotting
- `graphviz==0.20.1` - Graph visualizations
- `networkx==3.1` - Network analysis
- `papermill` - Notebook execution and parameterization
- `nbqa` - Code quality tools for notebooks (ruff, mypy)

### Development Tools
- `uv` - Fast Python package manager (replaces pip/poetry)
- `poethepoet` (poe) - Task runner for development commands
- `ruff` - Fast Python linter and formatter
- `mypy` (via nb_mypy) - Type checking for notebooks

## CI/CD and Publishing

- PRs to main branch trigger automated checks
- Version bumping uses semantic versioning (major/minor/patch)
- Package is published to PyPI as `moderne-visualizations-misc`
- Publishing is done via GitHub Actions workflow (manual trigger)

## Validation and Quality Checks

The project uses custom validation scripts instead of traditional unit tests:

1. **`poe check-options`**: Validates that notebook parameters match spec file options using `papermill.inspect_notebook()`
2. **`poe check-sentence-casing`**: Ensures all `displayName` fields in spec files use sentence case
3. **`poe check-types`**: Runs mypy type checking on notebooks via `nbqa`
4. **`poe format`**: Auto-formats notebooks with ruff via `nbqa`

## Common Issues and Solutions

1. **Import Errors**: Ensure you've activated the virtual environment (`source .venv/bin/activate`)
2. **Type Checking Failures**: Run `poe format` first, as ruff may fix import ordering issues
3. **Spec/Notebook Mismatch**: Use `poe check-options` to identify parameter mismatches between notebooks and spec files
4. **PlantUML Visualizations**: Require `plantuml.jar` in `resources/` directory
5. **Missing Dependencies**: Always use `uv sync --dev` instead of pip install
6. **Notebook Parameter Errors**: Parameters in the first cell must match exactly with spec file options (case-sensitive)