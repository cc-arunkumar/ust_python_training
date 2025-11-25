# Sample sales data: (Product, Quantity)
sales = [
    ("Laptop", 3),
    ("Mobile", 5),
    ("Tablet", 2),
    ("Mobile", 4),
    ("Laptop", 1)
]

# Dictionary to store total sales per product
sales_summary = {}

# Aggregate quantities for each product
for product, quantity in sales:
    # Add quantity to existing product total, or start from 0 if not present
    sales_summary[product] = sales_summary.get(product, 0) + quantity

# Print total sales per product
for product, quantity in sales_summary.items():
    print(f"{product} -> {quantity}")

# Find product with maximum sales
max_sale_product = max(sales_summary, key=sales_summary.get)
max_quantity = sales_summary[max_sale_product]

# Print product with maximum sales
print(f"Maximum sales: {max_sale_product} -> {max_quantity}")

# -------------------------
# Expected Output:
# Laptop -> 4
# Mobile -> 9
# Tablet -> 2
# Maximum sales: Mobile -> 9