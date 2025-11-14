# Cookiecutter ML Project Template

This repository provides a standardized Cookiecutter template for machine learning projects.
It is designed to minimize time-to-first-experiment and enforce a consistent, maintainable
project structure.

## Features

- Opinionated directory structure:
  - `data/` for raw, processed, and external datasets
  - `src/` as a Python package with models, pipelines, and utilities
  - `notebooks/` for exploratory research
  - `tests/` for automated testing
- Preconfigured tooling:
  - `flake8`, `black`, `isort`, `mypy` for code quality
  - `pytest` for tests
  - `Makefile` with common commands
- YAML-based configuration for experiments and models
- Minimal, SRP-oriented design ready for extension

## Requirements

- Python 3.11 (or compatible with your environment)
- `pip` installed and available in `PATH`
- `cookiecutter` Python package

Install Cookiecutter:

```bash
pip install cookiecutter
````

On Windows, this can be run from PowerShell if Python and `Scripts` are on your `PATH`.

## Usage

From any working directory, run:

```bash
cookiecutter path\to\cookiecutter-ml-template
```

You will be prompted for:

* `project_name`
* `project_slug`
* `package_name`
* `description`
* `author`
* `python_version`

Cookiecutter will generate a new project in a directory named
`{{ cookiecutter.project_slug }}` with the following structure:

```text
{{ cookiecutter.project_slug }}/
├── README.md
├── pyproject.toml
├── requirements.txt
├── .gitignore
├── Makefile
├── data/
├── notebooks/
├── src/
└── tests/
```

After generation, move into the project directory:

```bash
cd {{ cookiecutter.project_slug }}
```

Then install dependencies:

```bash
pip install -r requirements.txt
```

Run code quality checks:

```bash
make lint
```

Run tests:

```bash
make test
```

Run the baseline training pipeline:

```bash
make run
```

## Design principles

The template follows common software design principles:

* Single Responsibility Principle (SRP)
* Open/Closed Principle (OCP)
* Liskov Substitution Principle (LSP)
* Interface Segregation Principle (ISP)
* Dependency Inversion Principle (DIP)
* DRY (Don't Repeat Yourself)
* KISS (Keep It Simple, Stupid)

The aim is to keep the initial setup minimal yet extensible, allowing teams
to evolve the architecture without fighting the template.

## License

You can apply any license you prefer to your own copy or fork of this template.