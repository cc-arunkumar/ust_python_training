# Expense Reimbursement Tracker Scenario:
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

#code

# List of claims data: each tuple contains
# (Employee ID, Claim ID, Amount, Category, Date)
claims_data = [
    ("E101", "C001", 3200, "Travel", "2025-11-02"),
    ("E101", "C002", 1800, "Food", "2025-11-03"),
    ("E102", "C003", 4500, "Hotel", "2025-11-02"),
    ("E103", "C004", 1200, "Travel", "2025-11-02"),
    ("E102", "C005", 2200, "Travel", "2025-11-04"),
    ("E101", "C006", 4200, "Hotel", "2025-11-05")
]

# Dictionary to store claims grouped by employee
employee_claims = {}

# Set to track unique claim IDs (avoid duplicates)
claim_ids = set()

# Set to track unique expense categories
unique_categories = set()

# Process each claim record
for emp_id, claim_id, amount, category, date in claims_data:
    # Skip duplicate claim IDs
    if claim_id in claim_ids:
        continue
    
    # Add claim ID to the set
    claim_ids.add(claim_id)
    
    # Add category to the set of unique categories
    unique_categories.add(category)
    
    # Add claim amount to the employee's list of claims
    # setdefault() ensures a list exists for each employee
    employee_claims.setdefault(emp_id, []).append(amount)

# Calculate total reimbursement per employee
totals = {emp_id: sum(amounts) for emp_id, amounts in employee_claims.items()}

# Find employees whose total claims exceed ₹10,000
high_claim_employees = [emp_id for emp_id, total in totals.items() if total > 10000]

# Print total reimbursement per employee
print("Total reimbursement per employee:")
for emp_id, total in totals.items():
    print(f"{emp_id}: ₹{total}")

# Print employees with high claims
print("\nEmployees with total > ₹10,000:")
print(high_claim_employees)

# Print all unique expense categories
print("\nUnique expense categories:")
print(unique_categories)

#output
# g/Assignment1_Expense_reimbursementTracker.py
# Total reimbursement per employee:
# E101: ₹9200
# E102: ₹6700
# E103: ₹1200
# Employees with total > ₹10,000:
# []
# Unique expense categories:
# {'Travel', 'Food', 'Hotel'}
# PS C:\Users\303379\day3_training> 