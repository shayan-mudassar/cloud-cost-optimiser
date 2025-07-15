"""Generate simple text reports."""
from typing import Dict, List


def generate(breakdown: Dict[str, float], recommendations: List[str]) -> str:
    lines = ["Cost Report:"]
    for provider, cost in breakdown.items():
        lines.append(f"- {provider}: ${cost:.2f}")
    if recommendations:
        lines.append("\nRecommendations:")
        lines.extend(f"- {r}" for r in recommendations)
    return "\n".join(lines)
