"""Simple cost breakdown utilities."""
from collections import defaultdict
from typing import List, Dict


def by_provider(records: List[Dict]) -> Dict[str, float]:
    totals = defaultdict(float)
    for rec in records:
        totals[rec["provider"]] += rec["cost"]
    return dict(totals)
