"""Small command-line entry point for the expense tracker."""

from expenses import add_expense, total_expenses


def main() -> None:
    expenses = []
    print("Expense Tracker")
    print("Enter a blank category to finish.")

    while True:
        category = input("Category: ").strip()
        if not category:
            break
        try:
            amount = input("Amount: ")
            description = input("Description: ").strip()
            add_expense(expenses, category, amount, description)
        except ValueError as error:
            print(f"Invalid expense: {error}")
            continue

    print(f"Total: {total_expenses(expenses)}")


if __name__ == "__main__":
    main()
