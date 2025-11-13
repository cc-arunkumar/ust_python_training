#Assignment 1 — Expense Reimbursement Tracker
claims_data = [
 ("E101", "C001", 3200, "Travel", "2025-11-02"),
 ("E101", "C002", 1800, "Food", "2025-11-03"),
 ("E102", "C003", 4500, "Hotel", "2025-11-02"),
 ("E103", "C004", 1200, "Travel", "2025-11-02"),
 ("E102", "C005", 2200, "Travel", "2025-11-04"),
 ("E101", "C006", 4200, "Hotel", "2025-11-05")
]

emp_claim={}
set_claim_id=set()
set_unique_category=set()

for emp_id,claim_id,amount,category,date in claims_data:
    if claim_id in set_claim_id:
        continue
    set_claim_id.add(claim_id)
    set_unique_category.add(category)
    if emp_id not in emp_claim:
        emp_claim[emp_id]=[]
        emp_claim[emp_id].append({
            "claim_id":claim_id,
            "amount":amount,
            "category":category,
            "date":date
        })


print("Total Reimbursement Summary")
total_reimburse={}
for emp_id,claims in emp_claim.items():
    total=sum(claim["amount"] for claim in claims )
    total_reimburse[emp_id]=total
print("Total Reimburse per employee: ")
for emp_id,total in total_reimburse.items():
    print(f"{emp_id}:{total}")
high=[emp_id for emp_id,total in total_reimburse.items() if total>10000]
if high:
    for emp_id in high:
        print(f"Employee {emp_id}: Rs{total_reimburse[emp_id]}")



#Sample Executions
# Total Reimburse per employee:
# E101:3200
# E102:4500
# E103:1200
