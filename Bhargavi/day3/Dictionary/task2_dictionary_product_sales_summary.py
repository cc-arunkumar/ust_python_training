# product Sales Summary
# Task 2: Product Sales Summary
# Dictionary Tasks 1
# Scenario:
# You work in the Sales Analytics team.
# You receive a list of daily sales transactions — each as a tuple: (product, quantity) .

# Instructions:
# 1. Given:
# sales = [("Laptop", 3),("Mobile", 5),("Tablet", 2),("Mobile", 4),("Laptop", 1) ]

# 2. Create an empty dictionary sales_summary = {} .
# 3. Loop through the sales list and build the total quantity per product.
# 4. Print results like:
# Laptop → 4
# Mobile → 9
# Tablet → 2
# 5. Print the highest selling product name and its quantity.
# Task 3: Department Budget Tracker
# (Nested Dictionary)


# Sample sales data (product, quantity)
sales = [("Laptop", 3),("Mobile", 5),("Tablet", 2),("Mobile", 4),("Laptop", 1)]

# Dictionary to store total sales per product
sales_summary = {}

# Step 1: Aggregate sales quantities by product
for product, quantity in sales:
    if product in sales_summary:
        sales_summary[product] += quantity   # add to existing total
    else:
        sales_summary[product] = quantity    # initialize with first quantity

# Step 2: Print total quantity per product
for product, total_quantity in sales_summary.items():
    print(f"{product} -> {total_quantity}")

# Step 3: Find the highest selling product
highest_selling = max(sales_summary.items(), key=lambda x: x[1])
print(f"\nHighest selling product: {highest_selling[0]} → {highest_selling[1]}")


# Output:

# Laptop -> 4
# Mobile -> 9
# Tablet -> 2

# Highest selling product: Mobile → 9