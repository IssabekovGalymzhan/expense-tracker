from contextlib import redirect_stdout
from io import StringIO
import unittest
from pathlib import Path
from unittest.mock import patch

from expenses import Expense, add_expense, total_by_category, total_expenses
from main import main
from storage import load_expenses, save_expenses


class ExpenseTests(unittest.TestCase):
    def test_add_expense_appends_valid_expense(self) -> None:
        expenses: list[Expense] = []

        created = add_expense(expenses, " food ", "12.50", "Lunch")

        self.assertEqual(created.category, "food")
        self.assertEqual(str(created.amount), "12.50")
        self.assertEqual(expenses, [created])

    def test_add_expense_rejects_invalid_values(self) -> None:
        for category, amount in (("food", 0), ("food", -1), ("", 5)):
            with self.assertRaises(ValueError):
                add_expense([], category, amount)

    def test_add_expense_rejects_non_finite_values(self) -> None:
        for amount in ("NaN", "Infinity", "-Infinity"):
            with self.assertRaises(ValueError):
                add_expense([], "food", amount)

    def test_total_expenses_uses_decimal_money(self) -> None:
        expenses = [Expense("food", "10.10"), Expense("transport", "5.55")]

        self.assertEqual(str(total_expenses(expenses)), "15.65")

    def test_total_by_category(self) -> None:
        expenses = [Expense("food", "10.10"), Expense("food", "5.55"), Expense("books", "20")]

        self.assertEqual(str(total_by_category(expenses, "food")), "15.65")

    def test_save_and_load_round_trip(self) -> None:
        original = [Expense("food", "10.10", "Lunch"), Expense("books", "20.00")]
        path = Path("test-expenses.json")

        try:
            save_expenses(path, original)
            self.assertEqual(load_expenses(path), original)
        finally:
            if path.exists():
                path.unlink()

    def test_load_rejects_malformed_json(self) -> None:
        path = Path("malformed-expenses.json")
        path.write_text("{not valid json", encoding="utf-8")

        try:
            with self.assertRaises(ValueError):
                load_expenses(path)
        finally:
            if path.exists():
                path.unlink()

    def test_main_saves_expenses_to_storage(self) -> None:
        path = Path("main-test-expenses.json")

        try:
            with patch("main.DATA_PATH", path), patch(
                "builtins.input",
                side_effect=["food", "12.50", "Lunch", ""],
            ):
                main()

            self.assertEqual(load_expenses(path), [Expense("food", "12.50", "Lunch")])
        finally:
            if path.exists():
                path.unlink()

    def test_main_rejects_nan_without_crashing(self) -> None:
        path = Path("main-nan-test-expenses.json")
        output = StringIO()

        try:
            with patch("main.DATA_PATH", path), patch(
                "builtins.input",
                side_effect=["food", "NaN", "ignored description", ""],
            ), redirect_stdout(output):
                main()

            self.assertIn("Amount must be a finite number", output.getvalue())
        finally:
            if path.exists():
                path.unlink()


if __name__ == "__main__":
    unittest.main()
