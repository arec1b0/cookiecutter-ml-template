def test_package_imports() -> None:
    """
    Basic smoke test to verify that the main package is importable.
    """
    import {{ cookiecutter.package_name }}  # noqa: F401
