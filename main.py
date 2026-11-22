"""Small command-line entry point for the expense tracker."""

from pathlib import Path

from expenses import add_expense, total_expenses
from storage import load_expenses, save_expenses


DATA_PATH = Path("expenses.json")


def main() -> None:
    if DATA_PATH.exists():
        try:
            expenses = load_expenses(DATA_PATH)
        except ValueError as error:
            print(f"Could not load saved expenses: {error}")
            expenses = []
    else:
        expenses = []

    print("Expense Tracker")
    print("Enter a blank category to finish. Data is saved to expenses.json.")

    while True:
        category = input("Category: ").strip()
        if not category:
            break
        try:
            amount = input("Amount: ")
            description = input("Description: ").strip()
            add_expense(expenses, category, amount, description)
            save_expenses(DATA_PATH, expenses)
        except (OSError, ValueError) as error:
            print(f"Invalid expense: {error}")
            continue

    print(f"Total: {total_expenses(expenses)}")


if __name__ == "__main__":
    main()
