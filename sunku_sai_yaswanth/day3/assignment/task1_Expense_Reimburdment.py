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
# 5. Find all unique categories claimed by employees company-wid
# Sample Input(for understanding only):
# claims_data = [
#  ("E101", "C001", 3200, "Travel", "2025-11-02"),
#  ("E101", "C002", 1800, "Food", "2025-11-03"),
#  ("E102", "C003", 4500, "Hotel", "2025-11-02"),
#  ("E103", "C004", 1200, "Travel", "2025-11-02"),
#  ("E102", "C005", 2200, "Travel", "2025-11-04"),
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

new_claims={}
unique_category=set()
for employee_id,claim_id,amount,category,date in claims_data:
    new_claims[employee_id]=new_claims.get(employee_id,0)+amount
    unique_category.add(category)
total={}
for key,value in new_claims.items():
    print(f"{key}-> ₹{value}")
    if value>10000:
        
        total[key]=value

print("total reimbursment more than 10000",total)
print("unique expenses:",unique_category)


# output
# E101-> ₹9200
# E102-> ₹6700
# E103-> ₹1200
# total reimbursment more than 10000 {}
# unique expenses: {'Food', 'Travel', 'Hotel'}