#Expense Tracker
claims_data = [
    ("E101", "C001", 3200, "Travel", "2025-11-02"),
    ("E101", "C002", 1800, "Food", "2025-11-03"),
    ("E102", "C003", 4500, "Hotel", "2025-11-02"),
    ("E103", "C004", 1200, "Travel", "2025-11-02"),
    ("E102", "C005", 2200, "Travel", "2025-11-04"),
    ("E101", "C006", 4200, "Hotel", "2025-11-05")
]


employee_claims = {}
seen_claim_ids = set()
unique_categories = set()

for emp_id, claim_id, amount, category, date in claims_data:
    if claim_id in seen_claim_ids:
        continue  
    seen_claim_ids.add(claim_id)

    if emp_id not in employee_claims:
        employee_claims[emp_id] = []

    employee_claims[emp_id].append({
        "claim_id": claim_id,
        "amount": amount,
        "category": category,
        "date": date
    })

    unique_categories.add(category)

total_per_employee = {}
for emp_id, claims in employee_claims.items():
    total = sum(claim["amount"] for claim in claims)
    total_per_employee[emp_id] = total


print("Total Reimbursement per employee:")
for emp_id, total in total_per_employee.items():
    print(f"{emp_id}: Rs.{total}")

print("Unique expense categories:")
print(unique_categories)

'''
output:
Total Reimbursement per employee:
E101: Rs.9200
E102: Rs.6700
E103: Rs.1200
Unique expense categories:
{'Travel', 'Food', 'Hotel'}
'''