from __future__ import annotations

from pathlib import Path

import yaml
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

from {{ cookiecutter.package_name }}.models.baseline import (
    BaselineModelConfig,
    build_baseline_model,
)
from {{ cookiecutter.package_name }}.utils.io import load_csv


def load_config() -> dict:
    """
    Load the default YAML configuration.

    Returns
    -------
    dict
        Parsed configuration dictionary.
    """
    config_path = Path(__file__).resolve().parents[1] / "config" / "defaults.yaml"
    with config_path.open("r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)
    if cfg is None:
        raise ValueError(f"Configuration file is empty: {config_path}")
    return cfg


def run_training() -> float:
    """
    Run the baseline training pipeline.

    The pipeline is intentionally simple:
    - load configuration
    - load dataset
    - split train/test
    - train baseline model
    - evaluate on test set

    Returns
    -------
    float
        Accuracy score on the test split.
    """
    cfg = load_config()

    train_path = cfg["data"]["train_path"]
    target_column = cfg["data"]["target_column"]

    df = load_csv(train_path)

    if target_column not in df.columns:
        raise KeyError(f"Target column '{target_column}' not found in dataset.")

    X = df.drop(columns=[target_column])
    y = df[target_column]

    test_size = cfg["validation"]["test_size"]
    seed = cfg["experiment"]["seed"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=seed,
        shuffle=cfg["validation"]["shuffle"],
    )

    model_config = BaselineModelConfig(
        max_iter=cfg["model"]["params"]["max_iter"],
        n_jobs=cfg["model"]["params"]["n_jobs"],
    )

    model = build_baseline_model(model_config)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)

    print(f"Accuracy: {acc:.4f}")
    return acc


def main() -> None:
    """
    Entry point for the training pipeline.
    """
    run_training()


if __name__ == "__main__":
    main()
