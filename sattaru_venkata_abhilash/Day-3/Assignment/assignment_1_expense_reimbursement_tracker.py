# Assignment 1 — Expense Reimbursement Tracker
# Scenario:
# UST’s Finance Department wants to track employee reimbursement claims for business travel.
# Each claim contains: Employee ID, Claim ID, Amount, Category, and Date.
# Requirements:
# 1. Store and organize claim data for multiple employees.
# 2. Ensure no duplicate claim IDs exist.
# 3. Generate a summary for each employee.
# 4. Identify employees with total claims exceeding ₹10,000.
# 5. Find all unique categories claimed by employees.

claims_data = [
    ("E101", "C001", 3200, "Travel", "2025-11-02"),
    ("E101", "C002", 1800, "Food", "2025-11-03"),
    ("E102", "C003", 4500, "Hotel", "2025-11-02"),
    ("E103", "C004", 1200, "Travel", "2025-11-02"),
    ("E102", "C005", 2200, "Travel", "2025-11-04"),
    ("E101", "C006", 4200, "Hotel", "2025-11-05")
]

# Use a dictionary to store employee claims (avoid duplicate Claim IDs)
employee_claims = {}
unique_claim_ids = set()

for emp_id, claim_id, amount, category, date in claims_data:
    if claim_id not in unique_claim_ids:
        unique_claim_ids.add(claim_id)
        employee_claims.setdefault(emp_id, []).append((claim_id, amount, category, date))

# Calculate total reimbursement per employee
total_per_employee = {emp: sum(c[1] for c in claims) for emp, claims in employee_claims.items()}

# Find employees with total > ₹10,000
high_claimers = [emp for emp, total in total_per_employee.items() if total > 10000]

# Find all unique categories used
unique_categories = {c[2] for claim_list in employee_claims.values() for c in claim_list}

# Print results
print("Total Reimbursement per Employee:")
for emp, total in total_per_employee.items():
    print(f"{emp}: ₹{total}")

print("\nEmployees with total > ₹10,000:", high_claimers)
print("\nUnique Expense Categories:", unique_categories)


# Sample Output:
# Total Reimbursement per Employee:
# E101: ₹9200
# E102: ₹6700
# E103: ₹1200
#
# Employees with total > ₹10,000: []
#
# Unique Expense Categories: {'Travel', 'Food', 'Hotel'}
