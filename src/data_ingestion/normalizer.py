"""Utilities for normalizing cost data from different providers."""
from typing import List, Dict


def normalize(records: List[Dict]) -> List[Dict]:
    """Ensure each record has provider, service, and cost keys."""
    normalized = []
    for rec in records:
        normalized.append({
            "provider": rec.get("provider"),
            "service": rec.get("service"),
            "cost": float(rec.get("cost", 0)),
        })
    return normalized
