"""Anomaly detection placeholder."""
from typing import List, Dict


def detect_anomalies(records: List[Dict]) -> List[str]:
    """Return dummy anomalies if any cost exceeds a high threshold."""
    alerts = []
    for rec in records:
        if rec["cost"] > 200:
            alerts.append(f"Anomaly detected for {rec['provider']} {rec['service']}")
    return alerts
