# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

This project was generated from a standardized machine learning project template.

## Project structure

```text
data/           - datasets (raw, processed, external)
notebooks/      - Jupyter notebooks for research and experiments
src/            - Python package with pipelines, models, and utilities
tests/          - Automated tests
````

## Quick start

### Prerequisites

* Python {{ cookiecutter.python_version }} installed
* `pip` available in your environment
* (Optional) `virtualenv` or `venv` for isolated environments

### Setup

Install dependencies:

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

## Development workflow

1. Add or modify code inside `src/{{ cookiecutter.package_name }}/`.
2. Keep experiments and exploratory work in `notebooks/`.
3. Add or update tests in `tests/`.
4. Run `make lint` and `make test` before committing changes.

## Coding standards

This project follows common software design principles:

* Single Responsibility Principle (SRP)
* Open/Closed Principle (OCP)
* Liskov Substitution Principle (LSP)
* Interface Segregation Principle (ISP)
* Dependency Inversion Principle (DIP)
* DRY (Don't Repeat Yourself)
* KISS (Keep It Simple, Stupid)

## Author

D.Kriyhanovskzi