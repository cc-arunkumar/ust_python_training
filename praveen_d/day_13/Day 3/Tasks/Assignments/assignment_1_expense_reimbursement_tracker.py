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

employess_claims=set()
total_claim_amount_per_emp={}
high_payable_emp=[]
unique_expences=set()

for emp_id,claim_id,amount,reason,date in claims_data:

    employess_claims.add(claim_id)
    unique_expences.add(reason)

    if emp_id not in employess_claims:
        employess_claims.add(emp_id)
        total_claim_amount_per_emp[emp_id]=total_claim_amount_per_emp.get(emp_id,0)+amount
    else:
        total_claim_amount_per_emp[emp_id]=total_claim_amount_per_emp.get(emp_id)+amount

for key,value in total_claim_amount_per_emp.items():
    if value>10000:
        high_payable_emp.append(key)

    

print(total_claim_amount_per_emp)
print(high_payable_emp)
print(unique_expences)


# EXPECTED OUTPUT
# {'E101': 9200, 'E102': 6700, 'E103': 1200}
# []
# {'Travel', 'Food', 'Hotel'}





