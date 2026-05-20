"""
Personal Expense Tracker
Developer: Zulqarnain Khan Jadoon
Description: Track daily expenses, view reports, and manage budget
"""

import json
import os
from datetime import datetime

FILE = "expenses.json"

CATEGORIES = [
    "Food", "Transport", "Shopping",
    "Bills", "Health", "Education", "Other"
]

def load():
    if os.path.exists(FILE):
        with open(FILE) as f:
            return json.load(f)
    return []

def save(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_expense(data):
    print("\n--- Add Expense ---")
    print("Categories:", ", ".join(f"{i+1}.{c}" for i,c in enumerate(CATEGORIES)))
    try:
        cat_i  = int(input("Choose category (1-7): ")) - 1
        cat    = CATEGORIES[cat_i] if 0 <= cat_i < len(CATEGORIES) else "Other"
        amount = float(input("Amount (Rs): "))
        desc   = input("Description: ").strip()
    except ValueError:
        print("❌ Invalid input.")
        return

    entry = {
        "id"      : len(data) + 1,
        "category": cat,
        "amount"  : amount,
        "desc"    : desc,
        "date"    : datetime.now().strftime("%Y-%m-%d"),
        "time"    : datetime.now().strftime("%H:%M")
    }
    data.append(entry)
    save(data)
    print(f"✅ Rs {amount:.0f} added under '{cat}'")

def view_all(data):
    if not data:
        print("\n⚠  No expenses recorded.")
        return
    print(f"\n{'ID':<5} {'Date':<12} {'Category':<12} {'Amount':>10}  Description")
    print("-" * 60)
    total = 0
    for e in data:
        print(f"{e['id']:<5} {e['date']:<12} {e['category']:<12} Rs {e['amount']:>8.0f}  {e['desc']}")
        total += e["amount"]
    print("-" * 60)
    print(f"{'TOTAL':<30} Rs {total:>8.0f}")

def by_category(data):
    if not data:
        print("\n⚠  No data.")
        return
    summary = {}
    for e in data:
        summary[e["category"]] = summary.get(e["category"], 0) + e["amount"]
    print("\n--- Expenses by Category ---")
    for cat, total in sorted(summary.items(), key=lambda x: -x[1]):
        print(f"  {cat:<15} Rs {total:,.0f}")

def monthly_report(data):
    month = input("\nEnter month (YYYY-MM): ").strip()
    filtered = [e for e in data if e["date"].startswith(month)]
    if not filtered:
        print("❌ No data for this month.")
        return
    total = sum(e["amount"] for e in filtered)
    print(f"\n--- Report for {month} ---")
    print(f"  Transactions : {len(filtered)}")
    print(f"  Total Spent  : Rs {total:,.0f}")

def delete_expense(data):
    try:
        eid = int(input("\nEnter Expense ID to delete: "))
    except ValueError:
        print("❌ Invalid ID.")
        return
    for i, e in enumerate(data):
        if e["id"] == eid:
            data.pop(i)
            save(data)
            print("✅ Expense deleted.")
            return
    print("❌ ID not found.")

def main():
    print("=" * 50)
    print("      Personal Expense Tracker")
    print("   Developer: Zulqarnain Khan Jadoon")
    print("=" * 50)

    data = load()

    while True:
        print("\n--- Menu ---")
        print("  1. Add Expense")
        print("  2. View All Expenses")
        print("  3. View by Category")
        print("  4. Monthly Report")
        print("  5. Delete Expense")
        print("  6. Exit")

        choice = input("\nEnter choice (1-6): ").strip()

        if   choice == "1": add_expense(data)
        elif choice == "2": view_all(data)
        elif choice == "3": by_category(data)
        elif choice == "4": monthly_report(data)
        elif choice == "5": delete_expense(data)
        elif choice == "6":
            print("\n👋 Goodbye!")
            break
        else:
            print("⚠  Invalid choice.")

if __name__ == "__main__":
    main()
