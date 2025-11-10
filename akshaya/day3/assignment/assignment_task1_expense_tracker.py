# Assignment 1 — Expense Reimbursement Tracker

claims_data = [
    ("E101", "C001", 3200, "Travel", "2025-11-02"),
    ("E101", "C002", 1800, "Food", "2025-11-03"),
    ("E102", "C003", 4500, "Hotel", "2025-11-02"),
    ("E103", "C004", 1200, "Travel", "2025-11-02"),
    ("E102", "C005", 2200, "Travel", "2025-11-04"),
    ("E101", "C006", 4200, "Hotel", "2025-11-05")
]

all_claim_ids = []
unique_categories = set()
employee_total_amount = {}

for employee_id, claim_id, claim_amount, claim_category, claim_date in claims_data:
    if claim_id not in all_claim_ids:   
        all_claim_ids.append(claim_id)
        unique_categories.add(claim_category)

        if employee_id not in employee_total_amount:
            employee_total_amount[employee_id] = 0
        employee_total_amount[employee_id] += claim_amount

print("Total reimbursement amount per employee:")
for employee_id, total_amount in employee_total_amount.items():
    print(employee_id, ":", "₹", total_amount)

print("\nEmployees whose total reimbursement exceeds ₹10,000:")
for employee_id, total_amount in employee_total_amount.items():
    if total_amount > 10000:
        print(employee_id)

print("\nAll unique expense categories:")
print(unique_categories)


#sample output
# Total reimbursement amount per employee:
# E101 : ₹ 9200
# E102 : ₹ 6700
# E103 : ₹ 1200

# Employees whose total reimbursement exceeds ₹10,000:

# All unique expense categories:
# {'Food', 'Travel', 'Hotel'}
