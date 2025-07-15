"""Resource dependency visualization placeholder."""
from typing import List, Dict


def map_dependencies(records: List[Dict]) -> Dict[str, List[str]]:
    """Return a mock dependency map keyed by provider."""
    deps = {}
    for rec in records:
        deps.setdefault(rec["provider"], []).append(rec["service"])
    return deps
