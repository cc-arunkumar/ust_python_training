# Assignment 1 — Expense Reimbursement Tracker

#Code
claims_data = [
 ("E101", "C001", 3200, "Travel", "2025-11-02"),
 ("E101", "C002", 1800, "Food", "2025-11-03"),
 ("E102", "C003", 4500, "Hotel", "2025-11-02"),
 ("E103", "C004", 1200, "Travel", "2025-11-02"),
 ("E102", "C005", 2200, "Travel", "2025-11-04"),
 ("E101", "C006", 4200, "Hotel", "2025-11-05")
]

emp_claims={}
claim_ids =set()
unique_categories=set()

for emp_id , claim_id, amount ,category, date in claims_data:
    if claim_id in claim_ids:
        continue
    claim_ids.add(claim_id)
    # if emp id is not there then we will add emp id 
    
    if emp_id not in emp_claims:
        emp_claims[emp_id]=[]

    emp_claims[emp_id].append({
        "claim_id" : claim_id,
        "amount" : amount,
        "category" : category,
        "date" : date
    })
    unique_categories.add(category)

#Summary of employees

employee_result={}
for emp_id , claims in emp_claims.items():
    total = sum(claim["amount"] for claim in claims )
    employee_result[emp_id]=total
print("Total Reimbursement per Employee : ")
for emp_id , total in employee_result.items():
    print(f"{emp_id} : {total}")
high_claim= [emp_id for emp_id,total in employee_result.items() if total > 10000]
if high_claim:
    for emp_id in high_claim:
        print(f"Employee {emp_id}: ₹{employee_result[emp_id]}")
else:
    print("No Employee Above 10000")
print("Unique Expense Categories : ")
print(unique_categories)

#Output
# Total Reimbursement per Employee : 
# E101 : 9200
# E102 : 6700
# E103 : 1200
# No Employee Above 10000
# Unique Expense Categories : 
# {'Food', 'Hotel', 'Travel'}
