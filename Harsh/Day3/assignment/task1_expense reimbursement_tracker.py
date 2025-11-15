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
# Your Task:
# Design the right combination of Python data structures to:
# 1. Store each employee’s claims properly (avoid duplicates).
# 2. Calculate total claim amount per employee.
# 3. Print:
# Total reimbursement per employee
# List of employees whose total > ₹10,000
# Set of all unique expense categories used

# Sample data: List of expense claims (Employee ID, Claim ID, Amount, Category, Date)
claims_data = [
 ("E101", "C001", 3200, "Travel", "2025-11-02"),
 ("E101", "C002", 1800, "Food", "2025-11-03"),
 ("E102", "C003", 4500, "Hotel", "2025-11-02"),
 ("E103", "C004", 1200, "Travel", "2025-11-02"),
 ("E102", "C005", 2200, "Travel", "2025-11-04"),
 ("E101", "C006", 4200, "Hotel", "2025-11-05")
 ]

total_reim={}
expense_ctg=set()
data_set=set()

# Process each claim
for eid,cid,amt,catgry,date in claims_data:
    
    # Track unique claim IDs to avoid duplicates
    if cid not in data_set:
        data_set.add(cid)
        expense_ctg.add(catgry)
        
    # Calculate total reimbursement per employee
    if eid not in total_reim:
        total_reim[eid]=0
    total_reim[eid]+=amt
    

for eid,total in total_reim.items():
    print(f"{eid} : Rs{total}")

# Set of all unique expense categories used
for eid,total in total_reim.items():
    if total>10000:
        print(eid)
        
print(expense_ctg)

#  Total reimbursement per employee
# E101 : Rs9200
# E102 : Rs6700
# E103 : Rs1200

# Set of all unique expense categories used
# {'Food', 'Hotel', 'Travel'}