import pytest

from helios_core import HeliosDistributedCore


def test_importance_score_decreases_with_age():
    core = HeliosDistributedCore()

    newer = core.calculate_importance_score(similarity=1.0, tier=1, age=0)
    older = core.calculate_importance_score(similarity=1.0, tier=1, age=10)

    assert newer > older


def test_invalid_similarity_raises_error():
    core = HeliosDistributedCore()

    with pytest.raises(ValueError):
        core.calculate_importance_score(similarity=1.5, tier=1, age=0)


def test_negative_age_raises_error():
    core = HeliosDistributedCore()

    with pytest.raises(ValueError):
        core.calculate_importance_score(similarity=0.5, tier=1, age=-1)
