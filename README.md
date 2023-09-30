# <img src="https://github.com/moderneinc/moderne-visualizations-misc/assets/4691147/b8c59f5c-f603-431e-a8e9-08227954186c" height="120px" />

[![PyPI version](https://badge.fury.io/py/moderne-visualizations-misc.svg)](https://badge.fury.io/py/moderne-visualizations-misc)
[![CI](https://github.com/moderneinc/moderne-visualizations-misc/actions/workflows/checks.yml/badge.svg)](https://github.com/moderneinc/moderne-visualizations-misc/actions/workflows/checks.yml)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

## Installation

```bash
pip install moderne-visualizations-misc
```

## Run

```bash
jupyter notebook
```

## Contributing

Install development requirements:

```bash
pip install ".[dev]"
```

Run type checking:

```bash
poe check-types
```

Run formatter:

```bash
poe format
```

Cross validating options to make sure both spec files and notebooks have the same options:

```bash
poe check-options
```

Check sentence casing on display names:

```bash
poe check-sentence-casing
```
