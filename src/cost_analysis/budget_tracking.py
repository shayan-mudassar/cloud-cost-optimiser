"""Simple budget tracking utilities."""
from typing import List, Dict


def total_cost(records: List[Dict]) -> float:
    return sum(rec["cost"] for rec in records)


def is_over_budget(total: float, limit: float) -> bool:
    return total > limit
