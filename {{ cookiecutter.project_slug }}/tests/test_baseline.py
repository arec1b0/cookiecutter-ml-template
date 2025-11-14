from __future__ import annotations

import numpy as np
from sklearn.datasets import make_classification

from {{ cookiecutter.package_name }}.models.baseline import (
    BaselineModelConfig,
    build_baseline_model,
)


def test_baseline_model_trains_and_predicts() -> None:
    """
    Ensure that the baseline model can be trained and used for prediction
    on a small synthetic dataset.
    """
    X, y = make_classification(
        n_samples=100,
        n_features=5,
        n_informative=3,
        n_redundant=0,
        n_clusters_per_class=1,
        random_state=42,
    )

    config = BaselineModelConfig(max_iter=100)
    model = build_baseline_model(config)
    model.fit(X, y)

    preds = model.predict(X)
    assert preds.shape == (100,)
    assert set(np.unique(preds)) <= {0, 1}
