# Task 2: Product Sales Summary
# Dictionary Tasks 1
# Scenario:
# You work in the Sales Analytics team.
# You receive a list of daily sales transactions — each as a tuple

# Step 1: Initialize sales data as a list of tuples
sales = [
    ("Laptop", 3),
    ("Mobile", 5),
    ("Tablet", 2),
    ("Mobile", 4),
    ("Laptop", 1)
]

# Step 2: Create an empty dictionary to store total quantity per product
sales_summary = dict()

# Step 3: Aggregate quantities for each product
for item in sales:
    first, second = item  # first = product name, second = quantity
    if first in sales_summary:
        sales_summary[first] += second  # Add to existing total
    else:
        sales_summary[first] = second   # Initialize with first quantity

# Step 4: Print the aggregated sales summary
print(f"The aggregated sales summary {sales_summary}")

# Step 5: Initialize variables to track the product with highest sales
max_quantity = -1
top_product = ''

# Step 6: Iterate through the summary to find the highest-selling product
for item in sales_summary:
   
    val = sales_summary.get(item)  # Get total quantity
    if max_quantity < val:
        max_quantity = val
        top_product = item

# Step 7: Print the highest quantity and corresponding product name
print(f"the highest quantity and corresponding product name {max_quantity}, {top_product}")

# ============= sample output=============================
# The aggregated sales summary {'Laptop': 4, 'Mobile': 9, 'Tablet': 2}
# the highest quantity and corresponding product name 9, , Mobile