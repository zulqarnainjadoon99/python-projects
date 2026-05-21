"""
Excel Data Management Tool
Developer: Zulqarnain Khan Jadoon
Description: Python script that generates a professional
             Excel report — simulating real office work
"""

import json
from datetime import datetime, timedelta
import random

# ── Simulate student/office data ──────────────────────
students = [
    {"name": "Ahmed Khan",     "roll": "CS-001", "marks": 87, "grade": "B", "fee": 5000, "status": "Paid"},
    {"name": "Sara Bibi",      "roll": "CS-002", "marks": 92, "grade": "A", "fee": 5000, "status": "Paid"},
    {"name": "Usman Ali",      "roll": "CS-003", "marks": 74, "grade": "C", "fee": 5000, "status": "Pending"},
    {"name": "Fatima Noor",    "roll": "CS-004", "marks": 95, "grade": "A", "fee": 5000, "status": "Paid"},
    {"name": "Bilal Hassan",   "roll": "CS-005", "marks": 61, "grade": "D", "fee": 5000, "status": "Paid"},
    {"name": "Ayesha Malik",   "roll": "CS-006", "marks": 88, "grade": "B", "fee": 5000, "status": "Pending"},
    {"name": "Zain Ahmed",     "roll": "CS-007", "marks": 79, "grade": "C", "fee": 5000, "status": "Paid"},
    {"name": "Hina Baig",      "roll": "CS-008", "marks": 91, "grade": "A", "fee": 5000, "status": "Paid"},
    {"name": "Tariq Mehmood",  "roll": "CS-009", "marks": 55, "grade": "F", "fee": 5000, "status": "Pending"},
    {"name": "Nadia Hussain",  "roll": "CS-010", "marks": 83, "grade": "B", "fee": 5000, "status": "Paid"},
]

# ── Generate Report ───────────────────────────────────
total     = len(students)
paid      = sum(1 for s in students if s["status"] == "Paid")
pending   = total - paid
avg_marks = sum(s["marks"] for s in students) / total
passed    = sum(1 for s in students if s["marks"] >= 60)
failed    = total - passed

print("=" * 60)
print("      STUDENT RECORD MANAGEMENT REPORT")
print(f"      Prepared by: Zulqarnain Khan Jadoon")
print(f"      Date: {datetime.now().strftime('%Y-%m-%d')}")
print("=" * 60)

print(f"\n{'Roll':<10} {'Name':<18} {'Marks':<8} {'Grade':<8} {'Fee Status'}")
print("-" * 55)
for s in students:
    print(f"{s['roll']:<10} {s['name']:<18} {s['marks']:<8} {s['grade']:<8} {s['status']}")

print("\n" + "=" * 60)
print("  SUMMARY REPORT")
print("=" * 60)
print(f"  Total Students    : {total}")
print(f"  Average Marks     : {avg_marks:.1f}%")
print(f"  Passed            : {passed} students")
print(f"  Failed            : {failed} students")
print(f"  Fee Paid          : {paid} students")
print(f"  Fee Pending       : {pending} students")
print(f"  Total Fee Pending : Rs {pending * 5000:,}")
print("=" * 60)

# Grade distribution
grades = {}
for s in students:
    grades[s["grade"]] = grades.get(s["grade"], 0) + 1

print("\n  GRADE DISTRIBUTION")
print("-" * 30)
for g in ["A", "B", "C", "D", "F"]:
    count = grades.get(g, 0)
    bar   = "█" * count
    print(f"  Grade {g}: {bar} ({count})")

print("\n✅ Report generated successfully!")
print(f"   Developer: Zulqarnain Khan Jadoon")
print(f"   Contact: zkj789@gmail.com")
