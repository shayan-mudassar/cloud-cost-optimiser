"""GCP cost data retrieval (simulated)."""
from typing import List, Dict


def fetch_cost_data() -> List[Dict]:
    """Return mocked GCP cost data."""
    return [
        {"provider": "gcp", "service": "compute", "cost": 50.0},
        {"provider": "gcp", "service": "storage", "cost": 25.0},
    ]
