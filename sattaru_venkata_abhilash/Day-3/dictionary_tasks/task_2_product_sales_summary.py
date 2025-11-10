# Task 2: Product Sales Summary
# Scenario:
# You work in the Sales Analytics team.
# You receive a list of daily sales transactions — each as a tuple: (product, quantity).

sales = [
    ("Laptop", 3),
    ("Mobile", 5),
    ("Tablet", 2),
    ("Mobile", 4),
    ("Laptop", 1)
]

# Step 1: Create an empty dictionary
sales_summary = {}

# Step 2: Build total quantity per product
for product, quantity in sales:
    if product in sales_summary:
        sales_summary[product] += quantity
    else:
        sales_summary[product] = quantity

# Step 3: Print results
print("Product Sales Summary:")
for product, total_qty in sales_summary.items():
    print(f"{product} -> {total_qty}")

# Step 4: Find and print the highest selling product
max_product = max(sales_summary, key=sales_summary.get)
print("Highest Selling Product:")
print(f"{max_product} -> {sales_summary[max_product]}")
print(sales_summary)

# Sample Output:
# Product Sales Summary:
# Laptop -> 4
# Mobile -> 9
# Tablet -> 2
# Highest Selling Product:
# Mobile -> 9
# {'Laptop': 4, 'Mobile': 9, 'Tablet': 2}
