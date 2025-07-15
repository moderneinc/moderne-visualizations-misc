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
poe check-types     # Type checking with mypy
poe check-options   # Validate notebook parameters match spec files
poe check-sentence-casing  # Validate proper naming conventions
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
   - Each notebook should have parameters defined in the first cell
   - Parameters must match the options defined in the corresponding spec file
   - Use the reusable modules for common functionality (e.g., `moderne_visualizations_misc.reusable.dataframe`)

3. **Common Imports**:
   ```python
   from code_data_science import notebook, data_table
   import pandas as pd
   import plotly.express as px
   from moderne_visualizations_misc.reusable import dataframe
   ```

## Key Dependencies

- `code-data-science` - Core utilities for Moderne visualizations
- `pandas` - Data manipulation
- `plotly` - Interactive visualizations
- `matplotlib` - Static plotting
- `graphviz` - Graph visualizations
- `networkx` - Network analysis

## CI/CD and Publishing

- PRs to main branch trigger automated checks
- Version bumping uses semantic versioning (major/minor/patch)
- Package is published to PyPI as `moderne-visualizations-misc`
- Publishing is done via GitHub Actions workflow (manual trigger)

## Common Issues and Solutions

1. **Import Errors**: Ensure you've activated the virtual environment (`.venv/bin/activate`)
2. **Type Checking Failures**: Run `poe format` first, as ruff may fix import ordering
3. **Spec/Notebook Mismatch**: Use `poe check-options` to identify parameter mismatches
4. **PlantUML Visualizations**: Require `plantuml.jar` in resources directory