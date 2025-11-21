# Assignment 1 — Expense Reimbursement Tracker

"""
Scenario:
UST’s Finance Department wants to track employee reimbursement claims for
business travel.
Every employee can submit multiple claims — each claim has:
Claim ID
Amount
Category (Travel, Hotel, Food, etc.)
Date
Finance needs to:
1. Store and organize claim data for multiple employees.
2. Ensure no duplicate claim IDs exist.
3. Generate a quick summary for each employee.
4. Identify employees with total claims exceeding ₹10,000.
5. Find all unique categories claimed by employees company-wide
"""

# List of tuples containing claim data (Employee ID, Claim ID, Amount, Category, Date)
claims_data=[
("E101","C001",3200,"Travel","2025-11-02"),
("E101","C002",1800,"Food","2025-11-03"),
("E102","C003",4500,"Hotel","2025-11-02"),
("E103","C004",1200,"Travel","2025-11-02"),
("E102","C005",2200,"Travel","2025-11-04"),
("E101","C006",4200,"Hotel","2025-11-05")
]

# Dictionary to store claims organized by employee
claims_by_emp={}

# Set to track unique claim IDs to avoid duplicates
unique_ids=set()

# Process each claim in the data
for emp,claim,amt,cat,date in claims_data:
    # Only process if claim ID is not already seen
    if claim not in unique_ids:
        unique_ids.add(claim)
        # Initialize employee entry if not present
        if emp not in claims_by_emp:
            claims_by_emp[emp]={"claims":[],"total":0}
        # Add claim details to employee's list of claims
        claims_by_emp[emp]["claims"].append((claim,amt,cat,date))
        # Update total claimed amount for the employee
        claims_by_emp[emp]["total"]+=amt

# Set to store all unique categories company-wide
categories=set()

# Collect all unique categories from all employee claims
for emp,data in claims_by_emp.items():
    for c in data["claims"]:
        categories.add(c[2])

# Print total claimed amount per employee
for emp,data in claims_by_emp.items():
    print(f"{emp} → Total ₹{data['total']}")

# Identify employees with total claims exceeding ₹10,000
high_claims=[emp for emp,data in claims_by_emp.items() if data["total"]>10000]
print("Employees with total > ₹10000:",high_claims)

# Print all unique categories claimed
print("Unique Categories:",categories)


# sample output

"""
E101 → Total ₹9200
E102 → Total ₹6700
E103 → Total ₹1200
Employees with total > ₹10000: []
Unique Categories: {'Travel', 'Hotel', 'Food'}

"""
