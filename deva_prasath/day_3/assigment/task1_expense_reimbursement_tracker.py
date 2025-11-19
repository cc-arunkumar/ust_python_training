# Expense Reimbursement Tracker
# UST’s Finance Department wants to track employee reimbursement claims for
# business travel.

# Sample claims data for employees
claims_data = [
    ("E101", "C001", 3200, "Travel", "2025-11-02"),
    ("E101", "C002", 1800, "Food", "2025-11-03"),
    ("E102", "C003", 4500, "Hotel", "2025-11-02"),
    ("E103", "C004", 1200, "Travel", "2025-11-02"),
    ("E102", "C005", 2200, "Travel", "2025-11-04"),
    ("E101", "C006", 4200, "Hotel", "2025-11-05")
]

# Initialize dictionaries and sets for processing claims
employee_claims = {}        # Store claims by employee ID
seen_claim_ids = set()      # Set to track processed claim IDs
unique_categories = set()   # Set to track unique expense categories
employee_totals = {}        # Store total claims per employee

# Process claims data
for emp_id, claim_id, amount, category, date in claims_data:
    if claim_id in seen_claim_ids:  # Skip duplicate claim IDs
        continue
    seen_claim_ids.add(claim_id)
    
    # Add claim details to employee claims
    if emp_id not in employee_claims:
        employee_claims[emp_id] = []
    employee_claims[emp_id].append((claim_id, amount, category, date))
    
    # Add category to unique categories set
    unique_categories.add(category)
    
    # Update total claims for the employee
    employee_totals[emp_id] = employee_totals.get(emp_id, 0) + amount

# Print total reimbursements for each employee
print("Total Reimbursements per Employee")
for emp_id, total in employee_totals.items():
    print(f"{emp_id}: ₹{total}")

# Identify employees with total claims greater than 10,000
print("Employees with Total Claims > 10000")
high_claims = []
for emp, total in employee_totals.items():
    if total > 10000:
        high_claims.append(emp)

# Display employees with high claims or no employees exceeding 10,000
if high_claims:
    for emp in high_claims:
        print(f"{emp} → {employee_totals[emp]}")
else:
    print("No employees exceeded 10000.")

# Print sorted unique expense categories
print("Unique Expense Categories")
print(", ".join(sorted(unique_categories)))

# Print each employee's claims and total reimbursement
for emp_id, claims in employee_claims.items():
    print(f"\n{emp_id}:")
    for claim_id, amount, category, date in claims:
        print(f"{claim_id}|{category}|{amount}|{date}")
    print(f"Total: {employee_totals[emp_id]}")



#Sample output

# Total Reimbursements per Employee
# E101: ₹9200
# E102: ₹6700
# E103: ₹1200
# Employees with Total Claims > 10000
# No employees exceeded 10000.
# Unique Expense Categories
# Food, Hotel, Travel

# E101:
# C006|Hotel|4200|2025-11-05
# Total: 9200

# E102:
# C005|Travel|2200|2025-11-04
# Total: 6700

# E103:
# C004|Travel|1200|2025-11-02
# Total: 1200




