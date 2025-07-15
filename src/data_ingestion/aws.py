"""AWS cost data retrieval (simulated)."""
from typing import List, Dict


def fetch_cost_data() -> List[Dict]:
    """Return mocked AWS cost data."""
    return [
        {"provider": "aws", "service": "ec2", "cost": 120.5},
        {"provider": "aws", "service": "s3", "cost": 45.0},
    ]
