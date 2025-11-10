# Expense Reimbursement Tracker
claims_data = [
    ("E101", "C001", 3200, "Travel", "2025-11-02"),
    ("E101", "C002", 1800, "Food", "2025-11-03"),
    ("E102", "C003", 4500, "Hotel", "2025-11-02"),
    ("E103", "C004", 1200, "Travel", "2025-11-02"),
    ("E102", "C005", 2200, "Travel", "2025-11-04"),
    ("E101", "C006", 4200, "Hotel", "2025-11-05")
]

employees = {}
claim_ids = set()
categories = set()

for e_id, c_id, amt, cat, date in claims_data:
    if c_id in claim_ids:
        continue
    claim_ids.add(c_id)
    categories.add(cat)
    employees[e_id] = employees.get(e_id, 0) + amt

print("Total per employee:")
for e, total in employees.items():
    print(e, "₹", total)

print("\nEmployees with total > ₹10,000:")
for e, total in employees.items():
    if total > 10000:
        print(e)

print("\nUnique categories:")
print(categories)


# Total per employee:
# E101 ₹ 9200
# E102 ₹ 6700
# E103 ₹ 1200

# Employees with total > ₹10,000:

# Unique categories:
# {'Food', 'Hotel', 'Travel'}