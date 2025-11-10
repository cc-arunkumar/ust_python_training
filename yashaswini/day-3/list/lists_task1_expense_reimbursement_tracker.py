#  Expense Reimbursement Tracker
# Scenario:
# UST’s Finance Department wants to track employee reimbursement claims for
# business travel.
# Every employee can submit multiple claims — each claim has:
# Claim ID
# Amount
# Category (Travel, Hotel, Food, etc.)
# Date
# Finance needs to:
# 1. Store and organize claim data for multiple employees.
# 2. Ensure no duplicate claim IDs exist.
# 3. Generate a quick summary for each employee.
# 4. Identify employees with total claims exceeding ₹10,000.
# 5. Find all unique categories claimed by employees company-wide.


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
for emp_id, claim_id, amount, category, date in claims_data:
    if claim_id not in claim_ids:
        claim_ids.add(claim_id)
        categories.add(category)
        if emp_id not in employees:
            employees[emp_id] = []
        employees[emp_id].append((claim_id, amount, category, date))
totals = {emp: sum(c[1] for c in claims) for emp, claims in employees.items()}
high_claimers = [emp for emp, total in totals.items() if total > 10000]
print("Total reimbursement per employee:", totals)
print("Employees with total > ₹10,000:", high_claimers)
print("Unique expense categories:", categories)

#o/p:
# Total reimbursement per employee: {'E101': 9200, 'E102': 6700, 'E103': 1200}
# Employees with total > ₹10,000: []
# Unique expense categories: {'Travel', 'Food', 'Hotel'}