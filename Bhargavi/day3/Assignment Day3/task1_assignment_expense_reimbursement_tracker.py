# Expense Reimbursement Tracker

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


# Sample claims data (employee_id, claim_id, amount, category, date)
claims_data = [
    ("E101", "C001", 3200, "Travel", "2025-11-02"),
    ("E101", "C002", 1800, "Food", "2025-11-03"),
    ("E102", "C003", 4500, "Hotel", "2025-11-02"),
    ("E103", "C004", 1200, "Travel", "2025-11-02"),
    ("E102", "C005", 2200, "Travel", "2025-11-04"),
    ("E101", "C006", 4200, "Hotel", "2025-11-05")
]

# Dictionaries and sets for processing
employees = {}       # stores total claims per employee
claim_ids = set()    # ensures claim IDs are unique (avoids duplicates)
categories = set()   # stores unique claim categories

# Step 1: Process each claim
for e_id, c_id, amt, cat, date in claims_data:
    if c_id in claim_ids:       # skip duplicate claim IDs
        continue
    claim_ids.add(c_id)         # add claim ID to set
    categories.add(cat)         # add category to set
    employees[e_id] = employees.get(e_id, 0) + amt   # update employee total

# Step 2: Print total claims per employee
print("Total per employee:")
for e, total in employees.items():
    print(e, "₹", total)

# Step 3: Print employees with claims > ₹10,000
print("\nEmployees with total > ₹10,000:")
for e, total in employees.items():
    if total > 10000:
        print(e)

# Step 4: Print unique claim categories
print("\nUnique categories:")
print(categories)



#output
# Total per employee:
# E101 ₹ 9200
# E102 ₹ 6700
# E103 ₹ 1200

# Employees with total > ₹10,000:

# Unique categories:
# {'Food', 'Hotel', 'Travel'}