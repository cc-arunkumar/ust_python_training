# Task 2: Sales Record Analyzer
# Scenario:
# Your company stores weekly sales data as tuples.

# Step 1: Initialize sales data as a tuple of (branch, sales amount)
sales_data = (
    ("Chennai", 85000),
    ("Bangalore", 92000),
    ("Hyderabad", 78000),
    ("Pune", 102000),
    ("Delhi", 98000)
)

# Step 2: Initialize variables for total sales and tracking lowest sales
sum = 0
max = 99999999  # Used to find the minimum sales amount
lowest_sales = ''  # Stores branch with lowest sales

# Step 3: Iterate through each branch's sales data
print("Printing branches with sales above 90,000")
for sales in sales_data:
    branch_name, total_sales_amount = sales
    sum += total_sales_amount  # Accumulate total sales

    # Step 4: Update lowest sales tracker
    if max > total_sales_amount:
        max = total_sales_amount
        lowest_sales = branch_name

    # Step 5: Print branches with sales above 90,000
    if total_sales_amount > 90000:
        print(branch_name)

# Step 6: Convert tuple to list for updating
sales_list = list(sales_data)

# Step 7: Update Pune's sales amount
for i in range(len(sales_list)):
    branch, amount = sales_list[i]
    if branch == "Pune":
        sales_list[i] = ("Pune", 105000)

# Step 8: Convert updated list back to tuple
print("convert updated list back to tuple ")
updated_sales_data = tuple(sales_list)
print(updated_sales_data)

# Step 9: Print branch with lowest sales and its amount
print(f"lowest sales {lowest_sales} {max}")

# Step 10: Calculate and print average sales
print("Calculate and print average sales")
print(sum / len(sales_data))


# =============sample output =====================
# Printing branches with sales above 90,000
# Bangalore
# Pune
# Delhi
# convert updated list back to tuple 
# (('Chennai', 85000), ('Bangalore', 92000), ('Hyderabad', 78000), ('Pune', 105000), ('Delhi', 98000))
# lowest sales Hyderabad 78000
# Calculate and print average sales
# 91000.0