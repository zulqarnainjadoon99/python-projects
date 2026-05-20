"""
Student Record Management System
Developer: Zulqarnain Khan Jadoon
Description: A simple command-line tool to manage student records
             - Add, view, search and delete students
             - Save records to a file
"""

import json
import os
from datetime import datetime

FILE = "students.json"

def load_records():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def save_records(records):
    with open(FILE, "w") as f:
        json.dump(records, f, indent=4)

def add_student(records):
    print("\n--- Add New Student ---")
    name    = input("Student Name   : ").strip()
    roll_no = input("Roll Number    : ").strip()
    grade   = input("Grade/Class    : ").strip()
    marks   = input("Total Marks    : ").strip()
    contact = input("Contact Number : ").strip()

    student = {
        "id"      : len(records) + 1,
        "name"    : name,
        "roll_no" : roll_no,
        "grade"   : grade,
        "marks"   : marks,
        "contact" : contact,
        "added_on": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    records.append(student)
    save_records(records)
    print(f"\n✅ Student '{name}' added successfully!")

def view_students(records):
    if not records:
        print("\n⚠  No students found.")
        return
    print("\n--- All Students ---")
    print(f"{'ID':<5} {'Name':<20} {'Roll No':<12} {'Grade':<8} {'Marks':<8} {'Contact'}")
    print("-" * 65)
    for s in records:
        print(f"{s['id']:<5} {s['name']:<20} {s['roll_no']:<12} {s['grade']:<8} {s['marks']:<8} {s['contact']}")

def search_student(records):
    query = input("\nEnter name or roll number to search: ").strip().lower()
    results = [s for s in records if query in s["name"].lower() or query in s["roll_no"].lower()]
    if results:
        print(f"\n✅ Found {len(results)} result(s):")
        for s in results:
            print(f"  Name: {s['name']} | Roll: {s['roll_no']} | Grade: {s['grade']} | Marks: {s['marks']}")
    else:
        print("❌ No student found.")

def delete_student(records):
    roll = input("\nEnter Roll Number to delete: ").strip()
    for i, s in enumerate(records):
        if s["roll_no"] == roll:
            records.pop(i)
            save_records(records)
            print(f"✅ Student deleted successfully.")
            return
    print("❌ Student not found.")

def total_summary(records):
    if not records:
        print("\n⚠  No records available.")
        return
    total = len(records)
    marks = [int(s["marks"]) for s in records if s["marks"].isdigit()]
    avg   = sum(marks) / len(marks) if marks else 0
    print(f"\n--- Summary ---")
    print(f"  Total Students : {total}")
    print(f"  Average Marks  : {avg:.1f}")
    print(f"  Highest Marks  : {max(marks) if marks else 'N/A'}")
    print(f"  Lowest Marks   : {min(marks) if marks else 'N/A'}")

def main():
    print("=" * 50)
    print("   Student Record Management System")
    print("   Developer: Zulqarnain Khan Jadoon")
    print("=" * 50)

    records = load_records()

    while True:
        print("\n--- Main Menu ---")
        print("  1. Add Student")
        print("  2. View All Students")
        print("  3. Search Student")
        print("  4. Delete Student")
        print("  5. Summary Report")
        print("  6. Exit")

        choice = input("\nEnter your choice (1-6): ").strip()

        if   choice == "1": add_student(records)
        elif choice == "2": view_students(records)
        elif choice == "3": search_student(records)
        elif choice == "4": delete_student(records)
        elif choice == "5": total_summary(records)
        elif choice == "6":
            print("\n👋 Thank you for using Student Record System!")
            break
        else:
            print("⚠  Invalid choice. Please enter 1-6.")

if __name__ == "__main__":
    main()
