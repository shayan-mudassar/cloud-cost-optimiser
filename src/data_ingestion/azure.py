"""Azure cost data retrieval (simulated)."""
from typing import List, Dict


def fetch_cost_data() -> List[Dict]:
    """Return mocked Azure cost data."""
    return [
        {"provider": "azure", "service": "vm", "cost": 80.0},
        {"provider": "azure", "service": "storage", "cost": 30.0},
    ]
