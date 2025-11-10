# Assignment 1 — Expense Reimbursement Tracker

# Scenario:
# UST’s Finance Department wants to track employee reimbursement claims for
# business travel.
# Every employee can submit multiple claims — each claim has:
# Claim ID
# Amount
# Category (Travel, Hotel, Food, etc.)
# Date

# Finance needs to:
# 1. Store and organize claim data for multiple employees.
# 2. Ensure no duplicate claim IDs exist.
# 3. Generate a quick summary for each employee.
# 4. Identify employees with total claims exceeding ₹10,000.
# 5. Find all unique categories claimed by employees company-wide.
# Sample Input(for understanding only):
# claims_data = [
#  ("E101", "C001", 3200, "Travel", "2025-11-02"),
#  ("E101", "C002", 1800, "Food", "2025-11-03"),
#  ("E102", "C003", 4500, "Hotel", "2025-11-02"),
#  ("E103", "C004", 1200, "Travel", "2025-11-02"),
#  ("E102", "C005", 2200, "Travel", "2025-11-04"),
# Assignment 1
#  ("E101", "C006", 4200, "Hotel", "2025-11-05")
# ]

# Your Task:
# Design the right combination of Python data structures to:
# 1. Store each employee’s claims properly (avoid duplicates).
# 2. Calculate total claim amount per employee.
# 3. Print:
# Total reimbursement per employee
# List of employees whose total > ₹10,000
# Set of all unique expense categories used

claims_data = [
    ("E101", "C001", 3200, "Travel", "2025-11-02"),
    ("E101", "C002", 1800, "Food", "2025-11-03"),
    ("E102", "C003", 4500, "Hotel", "2025-11-02"),
    ("E103", "C004", 1200, "Travel", "2025-11-02"),
    ("E102", "C005", 2200, "Travel", "2025-11-04"),
    ("E101", "C006", 4200, "Hotel", "2025-11-05")
]

employee_claims, all_categories, seen = {}, set(), set()

for e, c, amt, cat, d in claims_data:
    if c in seen: continue
    seen.add(c); all_categories.add(cat)
    employee_claims.setdefault(e, {"claims": {}, "total": 0})
    employee_claims[e]["claims"][c] = (amt, cat, d)
    employee_claims[e]["total"] += amt

print("Total Reimbursement per Employee")
[print(f"{e}: ₹{v['total']}") for e, v in employee_claims.items()]

high = [e for e, v in employee_claims.items() if v["total"] > 10000]
print("Employees with Total > ₹10,000:", ", ".join(high) if high else "None")
print("Unique Expense Categories:", all_categories)


# Sample Output
# Total Reimbursement per Employee
# E101: ₹9200
# E102: ₹6700
# E103: ₹1200
# Employees with Total > ₹10,000
# None
# Unique Expense Categories {'Hotel', 'Food', 'Travel'}