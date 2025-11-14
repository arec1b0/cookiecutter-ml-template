from __future__ import annotations

from pathlib import Path
from typing import Union

import pandas as pd

PathLike = Union[str, Path]


def load_csv(path: PathLike) -> pd.DataFrame:
    """
    Load a CSV file into a pandas DataFrame.

    Parameters
    ----------
    path : str | Path
        Path to the CSV file.

    Returns
    -------
    pandas.DataFrame
        Loaded dataframe.

    Raises
    ------
    FileNotFoundError
        If the given path does not exist.
    """
    path_obj = Path(path)
    if not path_obj.exists():
        raise FileNotFoundError(f"CSV file not found: {path_obj}")
    return pd.read_csv(path_obj)


def save_csv(df: pd.DataFrame, path: PathLike, index: bool = False) -> None:
    """
    Save a pandas DataFrame to a CSV file.

    Parameters
    ----------
    df : pandas.DataFrame
        Dataframe to save.
    path : str | Path
        Output CSV file path.
    index : bool, default False
        Whether to write row names (index).
    """
    path_obj = Path(path)
    path_obj.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path_obj, index=index)
