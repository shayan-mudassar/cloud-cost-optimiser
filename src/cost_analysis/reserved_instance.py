"""Reserved instance recommendation stub."""
from typing import List, Dict


def recommend_reserved(records: List[Dict]) -> List[str]:
    """Suggest purchasing reserved instances for high-cost services."""
    suggestions = []
    for rec in records:
        if rec["cost"] > 100:
            suggestions.append(f"Purchase reserved instance for {rec['provider']} {rec['service']}")
    return suggestions
