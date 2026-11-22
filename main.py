import csv
from pathlib import Path

FILE_NAME = Path(__file__).parent / "expenses.csv"
HEADERS = ["description", "amount", "category"]


def load_expenses(file_name=FILE_NAME):

    expenses = []
    if not file_name.exists():
        return expenses

    with open(file_name, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                amount = float(row["amount"])
                if 0 < amount < float("inf"):
                    expenses.append({
                        "description": row["description"],
                        "amount": amount,
                        "category": row["category"],
                    })
            except (KeyError, ValueError, TypeError):
                print("Skipped an invalid saved expense.")
    return expenses


def save_expenses(expenses, file_name=FILE_NAME):
    """Write the current expense list to a CSV file."""
    with open(file_name, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=HEADERS)
        writer.writeheader()
        writer.writerows(expenses)


def add_expense(expenses):
    """Ask the user for a new expense and add it to the list."""
    description = input("Description: ").strip()
    if not description:
        print("Description cannot be empty.")
        return

    try:
        amount = float(input("Amount ($): "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if not 0 < amount < float("inf"):
        print("Amount must be greater than zero and finite.")
        return

    category = input("Category: ").strip()
    if not category:
        print("Category cannot be empty.")
        return

    expenses.append({
        "description": description,
        "amount": round(amount, 2),
        "category": category,
    })
    print("Expense added!")


def view_expenses(expenses):
    """Print every saved expense."""
    if not expenses:
        print("No expenses yet.")
        return

    print("\n--- Your expenses ---")
    for number, expense in enumerate(expenses, start=1):
        print(f"{number}. {expense['description']} | "
              f"{expense['category']} | ${expense['amount']:.2f}")


def calculate_total(expenses):
    """Return the total amount spent."""
    return sum(expense["amount"] for expense in expenses)


def category_totals(expenses):
    """Return the amount spent in each category."""
    totals = {}
    for expense in expenses:
        category = expense["category"].strip().title()
        if category not in totals:
            totals[category] = 0
        totals[category] += expense["amount"]
    return totals


def show_menu():
    print("\n===== PERSONAL EXPENSE TRACKER =====")
    print("1. Add expense")
    print("2. View expenses")
    print("3. View total spending")
    print("4. View spending by category")
    print("5. Save expenses")
    print("6. Exit")


def main():
    try:
        expenses = load_expenses()
    except (OSError, csv.Error) as error:
        print(f"Could not load expenses: {error}")
        return

    while True:
        show_menu()
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            print(f"Total spent: ${calculate_total(expenses):.2f}")
        elif choice == "4":
            totals = category_totals(expenses)
            if not totals:
                print("No expenses yet.")
            for category, amount in sorted(totals.items()):
                print(f"{category}: ${amount:.2f}")
        elif choice == "5" or choice == "6":
            try:
                save_expenses(expenses)
                print("Expenses saved.")
            except OSError as error:
                print(f"Could not save expenses: {error}")
                continue
            if choice == "6":
                print("Goodbye!")
                break
        else:
            print("Please choose a number between 1 and 6.")


if __name__ == "__main__":
    main()
