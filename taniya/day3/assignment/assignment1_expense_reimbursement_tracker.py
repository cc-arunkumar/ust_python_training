# Sample claims data: (EmployeeID, ClaimID, Amount, Category, Date)
claims_data = [
    ("E101", "C001", 3200, "Travel", "2025-11-02"),
    ("E101", "C002", 1800, "Food", "2025-11-03"),
    ("E102", "C003", 4500, "Hotel", "2025-11-02"),
    ("E103", "C004", 1200, "Travel", "2025-11-02"),
    ("E102", "C005", 2200, "Travel", "2025-11-04"),
    ("E101", "C006", 4200, "Hotel", "2025-11-05")
]

# Dictionary to store claims grouped by employee
emp_claim = {}

# Set to track unique claim IDs (avoid duplicates)
claim_ids = set()

# Set to track all unique expense categories
all_categories = set()

# Process each claim record
for emp_id, claim_id, amount, category, date in claims_data:
    # Skip duplicate claim IDs
    if claim_id in claim_ids:
        continue
    claim_ids.add(claim_id)
    
    # Add category to unique categories set
    all_categories.add(category)
    
    # Initialize employee claim list if not already present
    if emp_id not in emp_claim:
        emp_claim[emp_id] = []
    
    # Append claim details for the employee
    emp_claim[emp_id].append({
        "ClaimID": claim_id,
        "Amount": amount,
        "Category": category,
        "Date": date
    })

# Dictionary to store total reimbursement per employee
emp_totals = {}
for emp_id, claims in emp_claim.items():
    # Sum all claim amounts for each employee
    total = sum(claim["Amount"] for claim in claims)
    emp_totals[emp_id] = total

# Find employees with claims exceeding ₹10,000
high_claim = [emp for emp, total in emp_totals.items() if total > 10000]

# Print summary report
print("UST Expense Reimbursement Summary")
print("Total reimbursement per employee:")
for emp_id, total in emp_totals.items():
    print(f"Employee {emp_id}: {total}")

print("Employees with total claims > ₹10,000:")
print(high_claim)

print("All unique expense categories:")
print(all_categories)

# -------------------------
# Expected Output:
# UST Expense Reimbursement Summary
# Total reimbursement per employee:
# Employee E101: 9200
# Employee E102: 6700
# Employee E103: 1200
# Employees with total claims > ₹10,000:
# []
# All unique expense categories:
# {'Food', 'Hotel', 'Travel'}