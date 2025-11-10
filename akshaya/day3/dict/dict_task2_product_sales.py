# Task 2: Product Sales Summary

sales = [
    ("Laptop", 3),
    ("Mobile", 5),
    ("Tablet", 2),
    ("Mobile", 4),
    ("Laptop", 1)
]


sales_summary = {}

for product, quantity in sales:
    if product in sales_summary:
        sales_summary[product] += quantity
    else:
        sales_summary[product] = quantity

print("Product Sales Summary:")
for product, total_qty in sales_summary.items():
    print(f"{product} → {total_qty}")


highest_product = max(sales_summary, key=sales_summary.get)
print(f"\nHighest Selling Product: {highest_product} → {sales_summary[highest_product]}")

#sample output
# PS C:\Users\303375\Downloads\Tasks> python dict_t2_product_sales.py
# Product Sales Summary:
# Laptop → 4
# Mobile → 9
# Tablet → 2

# Highest Selling Product: Mobile → 9




