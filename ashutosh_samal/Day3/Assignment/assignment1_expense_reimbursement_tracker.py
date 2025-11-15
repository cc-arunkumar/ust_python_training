#Assignment 1 — Expense Reimbursement Tracker

# Data representing claims made by employees
claims_data = [
    ("E101", "C001", 3200, "Travel", "2025-11-02"), 
    ("E101", "C002", 1800, "Food", "2025-11-03"),
    ("E102", "C003", 4500, "Hotel", "2025-11-02"), 
    ("E103", "C004", 1200, "Travel", "2025-11-02"),
    ("E102", "C005", 2200, "Travel", "2025-11-04"),
    ("E101", "C006", 4200, "Hotel", "2025-11-05")
]

# Initialize a dictionary to store claims for each employee
emp_claim = {}

# Set to keep track of unique claim IDs (to avoid duplicates)
claim_ids = set()

# Set to store all unique expense categories
all_categories = set()

# Process each claim in the claims_data list
for emp_id, claim_id, amount, category, date in claims_data:
    # Skip the claim if the ClaimID already exists (avoid duplicate claims)
    if claim_id in claim_ids:
        continue
    claim_ids.add(claim_id)  # Add the claim ID to the set of claim IDs
    all_categories.add(category)  # Add the category to the set of unique categories
    
    # If the employee is not yet in the emp_claim dictionary, add them with an empty list
    if emp_id not in emp_claim:
        emp_claim[emp_id] = []
    
    # Append the current claim details to the employee's list of claims
    emp_claim[emp_id].append({
        "ClaimID": claim_id,
        "Amount": amount,
        "Category": category,
        "Date": date
    })

# Dictionary to store the total claim amount for each employee
emp_totals = {}

# Calculate the total reimbursement for each employee
for emp_id, claims in emp_claim.items():
    total = sum(claim["Amount"] for claim in claims)  # Sum all amounts for each employee
    emp_totals[emp_id] = total

# List of employees whose total claims are greater than ₹10,000
high_claim = [emp for emp, total in emp_totals.items() if total > 10000]

# Print the UST Expense Reimbursement Summary
print("UST Expense Reimbursement Summary")

# Print the total reimbursement for each employee
print("Total reimbursement per employee:")
for emp_id, total in emp_totals.items():
    print(f"Employee {emp_id}: ₹{total}")

# Print the employees with total claims greater than ₹10,000
print("Employees with total claims > ₹10,000:")
print(high_claim)

# Print all unique expense categories
print("All unique expense categories:")
print(all_categories)


#Sample Execution
# UST Expense Reimbursement Summary
# Total reimbursement per employee:
# Employee E101: 9200
# Employee E102: 6700
# Employee E103: 1200
# Employees with total claims > ₹10,000:
# []
# All unique expense categories:
# {'Travel', 'Hotel', 'Food'}