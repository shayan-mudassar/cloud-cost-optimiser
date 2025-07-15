"""Generate simple optimization recommendations."""
from typing import List, Dict


def find_underutilized(records: List[Dict], threshold: float = 50.0) -> List[str]:
    """Return services costing less than threshold to consider downsizing."""
    recommendations = []
    for rec in records:
        if rec["cost"] < threshold:
            recommendations.append(f"Consider downsizing {rec['provider']} {rec['service']}")
    return recommendations
