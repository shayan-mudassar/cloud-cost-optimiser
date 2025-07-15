"""Common helper utilities."""
import json
from pathlib import Path
from typing import Any


def load_json(path: str) -> Any:
    with open(path) as f:
        return json.load(f)


def save_text(path: str, text: str) -> None:
    Path(path).write_text(text)
