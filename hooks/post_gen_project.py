"""
Post-generation hook for Cookiecutter.

This script performs lightweight initialization steps after the project
has been rendered from the template.

The script is intentionally minimal to avoid introducing platform-specific
dependencies or side effects.
"""

from __future__ import annotations

import subprocess
from pathlib import Path


def run_command(cmd: list[str]) -> None:
    """
    Run a shell command, ignoring errors.

    Parameters
    ----------
    cmd : list[str]
        Command and arguments to execute.
    """
    try:
        subprocess.run(cmd, check=False)
    except Exception:
        # We keep this silent to avoid breaking template generation.
        pass


def main() -> None:
    project_dir = Path(".").resolve()

    print(f"\nInitializing Git repository in: {project_dir}")
    run_command(["git", "init"])
    run_command(["git", "add", "."])
    run_command(["git", "commit", "-m", "Initial project structure from cookiecutter"])

    print("Post-generation hook finished.\n")


if __name__ == "__main__":
    main()
