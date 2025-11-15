# Task 2: Product Sales Summary
# Dictionary Tasks 1
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

sales_summary = {}

# Calculate total quantity sold per product
for product,quantity in sales:
    sales_summary[product]=sales_summary.get(product,0)+ quantity

# Print the sales summary
for product,quantity in sales_summary.items():
    print(f"{product} -> {quantity}")

# Identify the highest selling product
highest=max(sales_summary,key=sales_summary.get)
print(f"highest selling product is {highest} and quantity is {sales_summary[highest]} ")

# Laptop -> 4
# Mobile -> 9
# Tablet -> 2
# highest selling product is Mobile and quantity is 9