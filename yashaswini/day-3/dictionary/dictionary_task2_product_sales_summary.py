# product Sales Summary
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
for product, qty in sales:
    sales_summary[product] = sales_summary.get(product, 0) + qty
for product, total_qty in sales_summary.items():
    print(f"{product} = {total_qty}")
best_seller = max(sales_summary, key=sales_summary.get)
print(f"Highest selling product: {best_seller} = {sales_summary[best_seller]}")


#o/p:
# Laptop = 4
# Mobile = 9
# Tablet = 2
# Highest selling product: Mobile = 9