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
# Sample Input(for understanding only):
# claims_data = [
#  ("E101", "C001", 3200, "Travel", "2025-11-02"),
#  ("E101", "C002", 1800, "Food", "2025-11-03"),
#  ("E102", "C003", 4500, "Hotel", "2025-11-02"),
#  ("E103", "C004", 1200, "Travel", "2025-11-02"),
#  ("E102", "C005", 2200, "Travel", "2025-11-04"),
# Assignment 1
#  ("E101", "C006", 4200, "Hotel", "2025-11-05")
# ]
# Your Task:
# Design the right combination of Python data structures to:
# 1. Store each employee’s claims properly (avoid duplicates).
# 2. Calculate total claim amount per employee.
# 3. Print:
# Total reimbursement per employee
# List of employees whose total > ₹10,000
# Set of all unique expense categories used

claims = []
claim_id = 1
while(True):
    print("1.Submit claim\n2.Exit")
    choice = int(input("Enetr choice: "))
    if choice == 1:
        emp_id = input("Employee ID: ")
        amount = int(input("Amount: "))
        category = input("Category: ")
        date = input("Date: ")

        claims.append((emp_id,"C00"+str(claim_id),amount,category,date))
        claim_id += 1
    elif choice == 2:
        break
    print("\n")

employee_claim_amount = {}
for i in claims:
    employee_claim_amount[i[0]] = employee_claim_amount.get(i[0],0) + i[2]
print(employee_claim_amount)

list = []
for i in employee_claim_amount:
    if employee_claim_amount[i]>10000:
        list.append(i)

print("List of employees whose total >10000: ",list)

category1 = []
for i in claims:
    category1.append(i[3])

unique_category = set(category1)
print("Unique category: ",unique_category)


# output

# 1.Submit claim
# 2.Exit
# Enetr choice: 2
# {'E101': 5000, 'E103': 4700, 'E102': 12200}
# List of employees whose total >10000:  ['E102']
# Unique category:  {'Food', 'Travel', 'Hotel'}