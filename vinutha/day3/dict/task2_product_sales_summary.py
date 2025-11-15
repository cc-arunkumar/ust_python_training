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

#Code
# List of sales records: each tuple contains (Product, Quantity)
sales = [
    ("Laptop", 3),
    ("Mobile", 5),
    ("Tablet", 2),
    ("Mobile", 4),
    ("Laptop", 1)
]

# Dictionary to store total quantity sold per product
sales_summary = {}

# Loop through each sale record
for product, qty in sales:
    # Add quantity to the product's total
    # .get(product, 0) → returns current total if product exists, else 0
    sales_summary[product] = sales_summary.get(product, 0) + qty

# Print the total quantity sold for each product
for product, total_qty in sales_summary.items():
    print(f"{product} → {total_qty}")

# Find the product with the highest total quantity sold
# max(..., key=sales_summary.get) → returns the product with the largest value
highest_selling = max(sales_summary, key=sales_summary.get)

# Print the highest selling product and its quantity
print(f"Highest selling product name: {highest_selling}, Quantity: {sales_summary[highest_selling]}")

#Output
# PS C:\Users\303379\day3_training> & C:/Users/303379/AppData/Local/Microsoft/WindowsApps/python3.13.exe c:/Users/303379/day3_training/task2_Product_Sales_Summary.py
# Laptop → 4
# Mobile → 9
# Tablet → 2
# Highest selling product name: Mobile, Quantity: 9
# PS C:\Users\303379\day3_training> 
