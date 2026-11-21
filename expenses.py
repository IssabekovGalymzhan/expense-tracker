"""Core expense calculations for the baseline version."""

from dataclasses import dataclass


@dataclass
class Expense:
    category: str
    amount: float
    description: str = ""


def add_expense(
    expenses: list[Expense],
    category: str,
    amount: float,
    description: str = "",
) -> Expense:
    """Create and append one expense."""
    if amount <= 0:
        raise ValueError("Amount must be greater than zero")

    expense = Expense(category=category, amount=float(amount), description=description)
    expenses.append(expense)
    return expense


def total_expenses(expenses: list[Expense]) -> float:
    """Return the total amount of all expenses."""
    return sum(expense.amount for expense in expenses)


def total_by_category(expenses: list[Expense], category: str) -> float:
    """Return the total amount for one category."""
    return sum(expense.amount for expense in expenses if expense.category == category)
