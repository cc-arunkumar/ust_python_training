# Task 2: Sales Record Analyzer
# Scenario:
# Your company stores weekly sales data as tuples.
# Each tuple has:
# (branch_name, total_sales_amount)
# Example data:
# sales_data = (
#  ("Chennai", 85000),
#  ("Bangalore", 92000),
#  ("Hyderabad", 78000),
#  ("Pune", 102000),
#  ("Delhi", 98000)
# )
# Your Tasks:
# 1. Print all branches with sales above ₹90,000.
# 2. Find the average sales across all branches.
# 3. Identify and print the branch with the lowest sales.
# 4. Convert this tuple data into a list of tuples and update Pune’s sales to 105000 ,
# then convert it back to a tuple and print the updated data.

sales_data = (
    ("Chennai", 85000),
    ("Bangalore", 92000),
    ("Hyderabad", 78000),
    ("Pune", 102000),
    ("Delhi", 98000)
    )

# Print branches with sales above ₹90,000
for (branch_name, total_sales_amount) in sales_data:
    if(total_sales_amount>90000):
        print("Branches:",branch_name)

# Find average sales
total_sale=0
for (branch_name, total_sales_amount) in sales_data:
    total_sale+=total_sales_amount
    avg=total_sale/len(sales_data)
print("average:",avg)

# Identify branch with lowest sales
min_sales = 99999999
min_branch = ""
for branch_name, total_sales_amount in sales_data:
    if total_sales_amount < min_sales:
        min_sales = total_sales_amount
        min_branch = branch_name
print(f"Branch with lowest sales: {min_branch} (₹{min_sales})")

# Update Pune's sales to 105000
sales_list = list(sales_data)
for i in range(len(sales_list)):
    branch_name, total_sales_amount = sales_list[i]
    if branch_name == "Pune":
        sales_list[i] = ("Pune", 105000)
update_sales=tuple(sales_list)
print(update_sales)


# Branches: Bangalore
# Branches: Pune
# Branches: Delhi
# average: 91000.0
# Branch with the lowest sales: Hyderabad (₹78000)
# (('Chennai', 85000), ('Bangalore', 92000), ('Hyderabad', 78000), ('Pune', 105000), ('Delhi', 98000))




