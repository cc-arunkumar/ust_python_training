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

for item, number in sales:
    if item in sales_summary:
        sales_summary[item] += number
    else:
        sales_summary[item] = number

for item, total in sales_summary.items():
    print(item, "→", total)

top_item = max(sales_summary, key=sales_summary.get)
print("Highest selling product:", top_item, "→", sales_summary[top_item])
# sampleoutput
# Laptop → 4
# Mobile → 9
# Tablet → 2
# Highest selling product: Mobile → 9