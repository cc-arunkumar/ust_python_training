#Assignment 1 — Expense Reimbursement Tracker

claims_data = [
    ("E101", "C001", 3200, "Travel", "2025-11-02"), ("E101", "C002", 1800, "Food", "2025-11-03"),
    ("E102", "C003", 4500, "Hotel", "2025-11-02"), ("E103", "C004", 1200, "Travel", "2025-11-02"),
    ("E102", "C005", 2200, "Travel", "2025-11-04"),("E101", "C006", 4200, "Hotel", "2025-11-05")
]

emp_claim = {}
claim_ids = set()
all_categories = set()

for emp_id, claim_id, amount, category, date in claims_data:
    if claim_id in claim_ids:
        continue
    claim_ids.add(claim_id)
    all_categories.add(category)
    
    if emp_id not in emp_claim:
        emp_claim[emp_id] = []
    
    emp_claim[emp_id].append({
        "ClaimID": claim_id,
        "Amount": amount,
        "Category": category,
        "Date": date
    })


emp_totals = {}
for emp_id, claims in emp_claim.items():
    total = sum(claim["Amount"] for claim in claims)
    emp_totals[emp_id] = total


high_claim = [emp for emp, total in emp_totals.items() if total > 10000]
print("UST Expense Reimbursement Summary")
print("Total reimbursement per employee:")
for emp_id, total in emp_totals.items():
    print(f"Employee {emp_id}: {total}")

print("Employees with total claims > ₹10,000:")
print(high_claim)

print("All unique expense categories:")
print(all_categories)

#Sample Execution
# UST Expense Reimbursement Summary
# Total reimbursement per employee:
# Employee E101: 9200
# Employee E102: 6700
# Employee E103: 1200
# Employees with total claims > ₹10,000:
# []
# All unique expense categories:
# {'Travel', 'Hotel', 'Food'}