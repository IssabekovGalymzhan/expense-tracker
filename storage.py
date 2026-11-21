"""JSON persistence for expenses."""

import json
from pathlib import Path

from expenses import Expense


def save_expenses(path: str | Path, expenses: list[Expense]) -> None:
    """Save expenses to a JSON file."""
    payload = [expense.__dict__ for expense in expenses]
    Path(path).write_text(json.dumps(payload, indent=2), encoding="utf-8")


def load_expenses(path: str | Path) -> list[Expense]:
    """Load expenses from a JSON file."""
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    return [Expense(**item) for item in payload]
