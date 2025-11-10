
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




sales = [("Laptop", 3),("Mobile", 5),("Tablet", 2),("Mobile", 4),("Laptop", 1)]
sales_summary={}

for product,quantity in sales:
    if product in sales_summary:
        sales_summary[product]+=quantity
    else:
        sales_summary[product]=quantity
for product, total in sales_summary.items():
    print(f"{product} → {total}")
highest_product = max(sales_summary, key=sales_summary.get)
print(f"Highest selling product: {highest_product} → {sales_summary[highest_product]}")

#Sample Output
# Laptop → 4
# Mobile → 9
# Tablet → 2
# Highest selling product: Mobile → 9