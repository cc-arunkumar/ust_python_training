# Task 2: Product Sales Summary
# Scenario:
# UST’s HR team keeps employee details in a Python dictionary.
# Each employee has a unique ID and name.
# Instructions:
# 1. Create a dictionary named employees with:
# "E101": "Arjun"
# "E102": "Neha"
# "E103": "Ravi"
# 2. Add two new employees:
# "E104": "Priya"
# "E105": "Vikram"
# 3. Update "E103" to "Ravi Kumar" .
# 4. Remove "E102" .
# 5. Display the total number of employees.
# 6. Print the final list like:
# Employee ID: E101 → Name: Arjun
# 7. If "E110" is searched, print "Employee not found" .
# Task 2: Product Sales Summar

sales = [
 ("Laptop", 3),
 ("Mobile", 5),
 ("Tablet", 2),
 ("Mobile", 4),
 ("Laptop", 1)
]

sales_summary={}

for product, quantity in sales:
    if product in sales_summary:
        sales_summary[product]+=quantity
    else:
        sales_summary[product]=quantity

max_value=0
max_key="Laptop"

for key,value in sales_summary.items():
    if value>max_value:
        max_value=value
        max_key=key

    print(f"{key}->{value}")

print(f"The highest selling product is:{max_key}->{max_value}")

# EXPECTED OUTPUT:
# Laptop->4
# Mobile->9
# Tablet->2
# The highest selling product is:Mobile->9
