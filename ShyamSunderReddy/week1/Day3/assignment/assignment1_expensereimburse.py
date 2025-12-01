#Assignment 1 — Expense Reimbursement Tracker
claims_data = [
 ("E101", "C001", 3200, "Travel", "2025-11-02"),
 ("E101", "C002", 2800, "Food", "2025-11-03"),
 ("E102", "C003", 4500, "Hotel", "2025-11-02"),
 ("E103", "C004", 1200, "Travel", "2025-11-02"),
 ("E102", "C005", 2200, "Travel", "2025-11-04"),
 ("E101", "C006", 4200, "Hotel", "2025-11-05")
]

unique_claims = {}
emp_claims={}
above10k=[]
unique_category=set()
for emp_id, claim_id, amount, category, date in claims_data:
    if claim_id not in unique_claims:
        unique_claims[claim_id] = (emp_id, amount, category, date)
    if emp_id not in emp_claims:
        emp_claims[emp_id] = 0
    emp_claims[emp_id]+=amount
    if emp_claims[emp_id]>10000 and emp_id not in above10k:
        above10k.append(emp_id)
    unique_category.add(category)

for emp_id,total in emp_claims.items():
    print(f"Total claims for Employee {emp_id}: {total}")

print("Employees with claims above 10,000:", above10k)
print("Unique claim categories:", unique_category)

# #sample output
# Total claims for Employee E101: 10200
# Total claims for Employee E102: 6700
# Total claims for Employee E103: 1200
# Employees with claims above 10,000: ['E101']
# Unique claim categories: {'Hotel', 'Food', 'Travel'}