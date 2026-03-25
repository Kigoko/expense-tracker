# Expense Tracker
# Saves your expenses to a file so they're not lost when you close the program

import csv
import os

FILENAME = "expenses.csv"

def load_expenses ():
    expenses = []
    if os.path.exists (FILENAME):
        with open (FILENAME, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["amount"] = float(row["amount"])
                expenses.append(row)
    return expenses
            
def save_expenses(expenses):
    with open(FILENAME, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["description", "amount", "category"])
        writer.writeheader()
        writer.writerows(expenses)

def add_expense(expenses):
    description = input("What did you spend on?")
    amount = float(input("How much did it cost?"))
    category = input("category (e.g. Food, Transport, Entertainment): ")
    expenses.append({"description": description, "amount": amount, "category": category})
    save_expenses(expenses)
    print("Expense saved!\n")

def view_expenses(expenses):
    if not expenses:
        print("no expenses yet.\n")
        return
    print("\n--- Your Expenses ---")
    for i, e in enumerate(expenses, 1):
        print(f"{i}. {e['description']} - Kshs{e['amount']:.2f} [{e['category']}]")
    total = sum(e["amount"] for e in expenses)
    print(f"\nTotal spent: Kshs{total:.2f}\n")

def view_by_category(expenses):
    if not expenses:
        print("No expenses yet.\n")
        return
    totals = {}
    for e in expenses:
        cat = e["category"]
        totals[cat] = totals.get(cat, 0) + e["amount"]
    print("\n--- Spending by Category--- ")
    for cat, total in totals.items():
        print(f"{cat}: ${total:.2f}")
    print()

def main():
    expenses = load_expenses();
    while True:
        print("=== Expense Tracker===")
        print("1. Add expense")
        print("2. View all expenses")
        print("3. View by category")
        print("4. Quit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            view_by_category(expenses)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.\n")
    
if __name__ == "__main__":
    main()