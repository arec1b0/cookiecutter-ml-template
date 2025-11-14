SHELL := /usr/bin/env bash

.PHONY: install lint format test run

install:
	pip install -r requirements.txt

lint:
	flake8 src tests
	black --check src tests
	isort --check-only src tests
	mypy src

format:
	black src tests
	isort src tests

test:
	pytest -q

run:
	python -m {{ cookiecutter.package_name }}.pipelines.train
