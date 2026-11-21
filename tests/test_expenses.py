import unittest
from pathlib import Path

from expenses import Expense, add_expense, total_by_category, total_expenses
from storage import load_expenses, save_expenses


class ExpenseTests(unittest.TestCase):
    def test_add_expense_appends_valid_expense(self) -> None:
        expenses: list[Expense] = []

        created = add_expense(expenses, "food", 12.50, "Lunch")

        self.assertEqual(created.category, "food")
        self.assertEqual(created.amount, 12.50)
        self.assertEqual(expenses, [created])

    def test_add_expense_rejects_non_positive_amount(self) -> None:
        for amount in (0, -1):
            with self.assertRaises(ValueError):
                add_expense([], "food", amount)

    def test_total_expenses(self) -> None:
        expenses = [Expense("food", 10.0), Expense("transport", 5.5)]

        self.assertEqual(total_expenses(expenses), 15.5)

    def test_total_by_category(self) -> None:
        expenses = [Expense("food", 10.0), Expense("food", 5.5), Expense("books", 20.0)]

        self.assertEqual(total_by_category(expenses, "food"), 15.5)

    def test_save_and_load_round_trip(self) -> None:
        original = [Expense("food", 10.0, "Lunch"), Expense("books", 20.0)]
        path = Path("test-expenses.json")

        try:
            save_expenses(path, original)
            self.assertEqual(load_expenses(path), original)
        finally:
            if path.exists():
                path.unlink()


if __name__ == "__main__":
    unittest.main()
