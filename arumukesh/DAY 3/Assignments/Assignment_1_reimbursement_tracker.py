claims_data = [
 ("E101", "C001", 3200, "Travel", "2025-11-02"),
 ("E101", "C002", 1800, "Food", "2025-11-03"),
 ("E102", "C003", 4500, "Hotel", "2025-11-02"),
 ("E103", "C004", 1200, "Travel", "2025-11-02"),
 ("E102", "C005", 2200, "Travel", "2025-11-04"),
 ("E101", "C006", 4200, "Hotel", "2025-11-05")
]
emp_claims = {}
claim_id=set()
unique_categories=set()
employee_totals={}
for (emp_id, claim_id_val, amount, category, date) in claims_data:
    if claim_id_val in claim_id:
        print(f"Duplicate Claim ID found: {claim_id_val} for Employee: {emp_id}")
        continue
    claim_id.add(claim_id_val)
    unique_categories.add(category)
    if emp_id not in emp_claims:
        emp_claims[emp_id] = {}
    emp_claims[emp_id][claim_id_val]=(amount, category, date)
    unique_categories.add(category)
print(emp_claims)

for emp_id, claims in emp_claims.items():
    total=0
    for amount, category, date in claims.values():
        total+=amount
    employee_totals[emp_id]=total
print("Employee Total Claims:", employee_totals)
for emp_id, tot_claims in employee_totals.items():
    if tot_claims > 4000:
        print(f"Alert! Employee {emp_id} has high total claims: {tot_claims}")
print("Unique Claim Categories:", unique_categories)
print("total reimbursement of every employee:",employee_totals)
        # if amount > 10000:
        #     print(f"High Value Claim by Employee: {emp_id} Amount: {amount} Category: {category} Date: {date}")

# {'E101': {'C001': (3200, 'Travel', '2025-11-02'), 'C002': (1800, 'Food', '2025-11-03'), 'C006': (4200, 'Hotel', '2025-11-05')}, 'E102': {'C003': (4500, 'Hotel', '2025-11-02'), 'C005': (2200, 'Travel', '2025-11-04')}, 'E103': {'C004': (1200, 'Travel', '2025-11-02')}}
# Employee Total Claims: {'E101': 9200, 'E102': 6700, 'E103': 1200}
# Alert! Employee E101 has high total claims: 9200
# Alert! Employee E102 has high total claims: 6700
# Unique Claim Categories: {'Travel', 'Food', 'Hotel'}
# total reimbursement of every employee: {'E101': 9200, 'E102': 6700, 'E103': 1200