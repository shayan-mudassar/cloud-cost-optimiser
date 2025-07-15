"""Basic rules engine."""
from typing import Callable, List, Dict


Rule = Callable[[Dict], bool]


def apply_rules(records: List[Dict], rules: List[Rule]) -> List[Dict]:
    """Return records that match any of the provided rules."""
    matched = []
    for rec in records:
        if any(rule(rec) for rule in rules):
            matched.append(rec)
    return matched
