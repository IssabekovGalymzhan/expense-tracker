"""JSON persistence for expenses."""

import json
from pathlib import Path

from expenses import Expense


def save_expenses(path: str | Path, expenses: list[Expense]) -> None:
    """Save expenses to a JSON file."""
    payload = [
        {
            "category": expense.category,
            "amount": str(expense.amount),
            "description": expense.description,
        }
        for expense in expenses
    ]
    Path(path).write_text(json.dumps(payload, indent=2), encoding="utf-8")


def load_expenses(path: str | Path) -> list[Expense]:
    """Load expenses from a JSON file."""
    try:
        payload = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise ValueError(f"Could not read expense data: {error}") from error

    if not isinstance(payload, list):
        raise ValueError("Expense data must be a JSON list")

    loaded: list[Expense] = []
    for index, item in enumerate(payload):
        if not isinstance(item, dict):
            raise ValueError(f"Expense at index {index} must be an object")
        try:
            loaded.append(Expense(**item))
        except (TypeError, ValueError) as error:
            raise ValueError(f"Invalid expense at index {index}: {error}") from error
    return loaded
