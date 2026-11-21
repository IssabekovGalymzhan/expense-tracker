"""Core expense calculations."""

from dataclasses import dataclass
from decimal import Decimal, InvalidOperation


MONEY_QUANTUM = Decimal("0.01")


@dataclass
class Expense:
    category: str
    amount: Decimal
    description: str = ""

    def __post_init__(self) -> None:
        category = self.category.strip()
        if not category:
            raise ValueError("Category must not be empty")

        try:
            amount = Decimal(str(self.amount)).quantize(MONEY_QUANTUM)
        except (InvalidOperation, ValueError):
            raise ValueError("Amount must be a valid number") from None

        if amount <= 0:
            raise ValueError("Amount must be greater than zero")

        self.category = category
        self.amount = amount


def add_expense(
    expenses: list[Expense],
    category: str,
    amount: Decimal | float | int | str,
    description: str = "",
) -> Expense:
    """Create and append one expense."""
    expense = Expense(category=category, amount=amount, description=description)
    expenses.append(expense)
    return expense


def total_expenses(expenses: list[Expense]) -> Decimal:
    """Return the total amount of all expenses."""
    return sum((expense.amount for expense in expenses), Decimal("0.00"))


def total_by_category(expenses: list[Expense], category: str) -> Decimal:
    """Return the total amount for one category."""
    return sum(
        (expense.amount for expense in expenses if expense.category == category),
        Decimal("0.00"),
    )
