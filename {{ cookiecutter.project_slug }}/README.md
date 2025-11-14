# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

This project was generated from a standardized machine learning project template.

## Project structure

```text
data/           - datasets (raw, processed, external)
notebooks/      - Jupyter notebooks for research and experiments
src/            - Python package with pipelines, models, and utilities
tests/          - Automated tests
scripts/        - Helper scripts (e.g. dev.ps1 for Windows)
````

## Quick start

### 1. Create and activate a virtual environment

On Windows 11 (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

On Linux / macOS (bash/zsh):

```bash
python -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies and the project

On Windows (using the helper script):

```powershell
.\scripts\dev.ps1 -Task install
```

On Linux / macOS:

```bash
pip install --upgrade pip
pip install -r requirements.txt
pip install -e .[dev]
```

## Common tasks

### Windows (PowerShell)

```powershell
# Run linters and type checks
.\scripts\dev.ps1 -Task lint

# Auto-format code
.\scripts\dev.ps1 -Task format

# Run tests
.\scripts\dev.ps1 -Task test

# Run the baseline training pipeline
.\scripts\dev.ps1 -Task run
```

### Linux / macOS (with make installed)

```bash
make lint      # flake8 + black --check + isort --check-only + mypy
make format    # black + isort
make test      # pytest
make run       # python -m {{ cookiecutter.package_name }}.pipelines.train
```

If `make` is not available, you can call the underlying commands directly using `python -m ...`
and `pytest` from the activated virtual environment.

## Development workflow

1. Add or modify code inside `src/{{ cookiecutter.package_name }}/`.
2. Keep experiments and exploratory work in `notebooks/`.
3. Add or update tests in `tests/`.
4. Run `lint` and `test` tasks before committing changes.

## Coding standards

This project follows common software design principles:

* Single Responsibility Principle (SRP)
* Open/Closed Principle (OCP)
* Liskov Substitution Principle (LSP)
* Interface Segregation Principle (ISP)
* Dependency Inversion Principle (DIP)
* DRY (Don't Repeat Yourself)
* KISS (Keep It Simple, Stupid)

The aim is to keep the initial setup minimal yet extensible, allowing the project
to evolve without fighting the initial template.

## Author

{{ cookiecutter.author }}