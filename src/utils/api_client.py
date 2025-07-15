"""Simple HTTP client wrapper using requests."""
from typing import Any, Dict
import logging

try:
    import requests
except ImportError:  # pragma: no cover - requests may not be installed
    requests = None  # type: ignore

logger = logging.getLogger(__name__)


def get(url: str, **kwargs: Any) -> Dict:
    if requests is None:
        raise RuntimeError("requests library is required")
    resp = requests.get(url, **kwargs)
    resp.raise_for_status()
    return resp.json()
