from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class VectorRecord:
    """A single memory/vector record managed by the Helios substrate."""

    id: str
    content: str
    vector: List[float]
    tier: int = 1
    age: float = 0.0


class HeliosDistributedCore:
    """Core scoring and cluster state for the Helios memory substrate.

    This is still an early implementation. It currently provides validated
    importance scoring and a place to attach future cluster behavior.
    """

    def __init__(self, drift_factor: float = 0.05):
        if drift_factor < 0:
            raise ValueError("drift_factor cannot be negative")

        self.clusters: dict[str, list[VectorRecord]] = {}
        self.drift_factor = drift_factor

    def calculate_importance_score(
        self,
        similarity: float,
        tier: int,
        age: float = 0.0,
    ) -> float:
        """Calculate importance using similarity, retention tier, and age.

        Args:
            similarity: Match score between 0 and 1.
            tier: Memory tier. Tier 1 is strongest; unknown tiers receive low weight.
            age: Age value used for drift/decay. Must be non-negative.

        Returns:
            A floating-point importance score.
        """
        if not 0 <= similarity <= 1:
            raise ValueError("similarity must be between 0 and 1")

        if age < 0:
            raise ValueError("age cannot be negative")

        tier_weight = {1: 1.0, 2: 0.7, 3: 0.4}.get(tier, 0.1)
        return (similarity * tier_weight) / (1 + (self.drift_factor * age))
