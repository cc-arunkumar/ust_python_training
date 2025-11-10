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
unique_catagories = set()

for emp_id, claim_id, amount, category, date in claims_data:
    if claim_id in seen_claim_ids:
        continue
    seen_claim_ids.add(claim_id)
    
    if emp_id not in employee_claims:
        employee_claims[emp_id] = []
        
    employee_claims[emp_id].append({
        "claim_id" : claim_id,
        "amount" : amount,
        "catagory" : category,
        "date" : date 
    })
    
    unique_catagories.add(category)
    
employee_totals = {}
for emp_id, claims in employee_claims.items():
    total = sum(claim["amount"] for claim in claims)
    employee_totals[emp_id] = total

print("total reimbursement per employee : ")
for emp_id, total in employee_totals.items():
    print(f"{emp_id} : ₹{total}")

high_claim_employees = [emp_id for emp_id, total in employee_totals.items() if total > 10000]
print("\nEmployees with total claims exceeding 10,000: ")
print(high_claim_employees)

print(unique_catagories)

