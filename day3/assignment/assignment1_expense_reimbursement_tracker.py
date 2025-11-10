# Assignment 1 — Expense Reimbursement Tracker
# Scenario:
# UST’s Finance Department wants to track employee reimbursement claims for
# business travel.

claims_data=[
("E101","C001",3200,"Travel","2025-11-02"),
("E101","C002",1800,"Food","2025-11-03"),
("E102","C003",4500,"Hotel","2025-11-02"),
("E103","C004",1200,"Travel","2025-11-02"),
("E102","C005",2200,"Travel","2025-11-04"),
("E101","C006",4200,"Hotel","2025-11-05")
]

claims_by_emp={}
unique_ids=set()

for emp,claim,amt,cat,date in claims_data:
    if claim not in unique_ids:
        unique_ids.add(claim)
        if emp not in claims_by_emp:
            claims_by_emp[emp]={"claims":[],"total":0}
        claims_by_emp[emp]["claims"].append((claim,amt,cat,date))
        claims_by_emp[emp]["total"]+=amt


categories=set()

for emp,data in claims_by_emp.items():
    for c in data["claims"]:
        categories.add(c[2])

for emp,data in claims_by_emp.items():
    print(f"{emp} → Total ₹{data['total']}")

high_claims=[emp for emp,data in claims_by_emp.items() if data["total"]>10000]
print("Employees with total > ₹10000:",high_claims)
print("Unique Categories:",categories)

# sample output:

# E101 → Total ₹9200
# E102 → Total ₹6700
# E103 → Total ₹1200
# Employees with total > ₹10000: []
# Unique Categories: {'Food', 'Hotel', 'Travel'}