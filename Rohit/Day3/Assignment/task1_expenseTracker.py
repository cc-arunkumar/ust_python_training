# Assignment 1 — Expense Reimbursement Tracker
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


# Step 1: Initialize the claims data as a list of tuples
claims_data = [
    ("E101", "C001", 3200, "Travel", "2025-11-02"),
    ("E101", "C002", 1800, "Food", "2025-11-03"),
    ("E102", "C003", 4500, "Hotel", "2025-11-02"),
    ("E103", "C004", 1200, "Travel", "2025-11-02"),
    ("E102", "C005", 2200, "Travel", "2025-11-04"),
    ("E101", "C006", 4200, "Hotel", "2025-11-05")
]

# Step 2: Initialize dictionaries and sets
total_reim = {}       # To store total reimbursement per employee
expense_ctg = set()   # To store unique expense categories
data_set = set()      # To track unique claim IDs and avoid duplicates

# Step 3: Process each claim entry
for eid, cid, amt, catgry, date in claims_data:
    
    # Step 3a: If claim ID is new, add to data_set and track its category
    if cid not in data_set:
        data_set.add(cid)
        expense_ctg.add(catgry)
    
    # Step 3b: Initialize reimbursement total for new employee ID
    if eid not in total_reim:
        total_reim[eid] = 0
    
    # Step 3c: Accumulate the claim amount for the employee
    total_reim[eid] += amt

# Step 4: Display total reimbursement per employee
for eid, total in total_reim.items():
    print(f"Toatal reimbrusement per employee {eid} : Rs{total}")

# Step 5: Identify employees with total claims exceeding Rs 10,000
for eid, total in total_reim.items():
    if total > 10000:
        print(f" Totatl claims exceeding Rs 10,000 {eid}")

# Step 6: Display all unique expense categories
print(f"All unique expense categories {expense_ctg}")




# ==============sample output=======================
# Toatal reimbrusement per employee E101 : Rs9200
# Toatal reimbrusement per employee E102 : Rs6700
# Toatal reimbrusement per employee E103 : Rs1200
# All unique expense categories {'Hotel', 'Travel', 'Food'}