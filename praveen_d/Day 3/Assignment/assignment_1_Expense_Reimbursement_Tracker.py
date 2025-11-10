# Assignment 1 — Expense Reimbursement Tracker



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





