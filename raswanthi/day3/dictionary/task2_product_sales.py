# Task 2: Product Sales Summary
sales = [
    ("Laptop", 3),
    ("Mobile", 5),
    ("Tablet", 2),
    ("Mobile", 4),
    ("Laptop", 1)
]


sales_summary = {}


for item, quantity in sales:
    if item in sales_summary:
        sales_summary[item] += quantity
    else:
        sales_summary[item] = quantity


for item, total_quantity in sales_summary.items():
    print(f"{item} → {total_quantity}")


highest_product = max(sales_summary, key=sales_summary.get)
print(f"\nHighest selling product: {highest_product} → {sales_summary[highest_product]}")

'''
output:
Laptop → 4
Mobile → 9
Tablet → 2

Highest selling product: Mobile → 9
'''