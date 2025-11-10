# Task 2: Product Sales Summary

# Scenario:
# You work in the Sales Analytics team.
# You receive a list of daily sales transactions — each as a tuple: (product, quantity) .
# Instructions:
# 1. Given:
# sales = [
#  ("Laptop", 3),
#  ("Mobile", 5),
#  ("Tablet", 2),
#  ("Mobile", 4),
#  ("Laptop", 1)
# ]
# 2. Create an empty dictionary sales_summary = {} .
# 3. Loop through the sales list and build the total quantity per product.
# 4. Print results like:
# Laptop → 4
# Mobile → 9
# Tablet → 2
# 5. Print the highest selling product name and its quantity.


sales = [
 ("Laptop", 3),
 ("Mobile", 5),
 ("Tablet", 2),
 ("Mobile", 4),
 ("Laptop", 1)
]

sales_summary={}

for key,val in sales:
    if key in sales_summary:
        sales_summary[key]+=val
    else:
        sales_summary[key]=val


max=0

for key,val in sales_summary.items():
    print(f"{key}->{val}")

    if val>max:
        max=val
        name=key

print("Hightest selling product: ",name) 

# Sample output

# Laptop->4
# Mobile->9
# Tablet->2

# Hightest selling product: Mobile

