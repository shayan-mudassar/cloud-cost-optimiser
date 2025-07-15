"""Mock ML-based cost prediction."""
from typing import List, Dict


def predict_next_month(records: List[Dict]) -> float:
    """Return a naive prediction based on average cost."""
    if not records:
        return 0.0
    total = sum(r["cost"] for r in records)
    return total / len(records)
