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
# Tuple Tasks 
sales_data = (
    ("Chennai", 85000),
    ("Bangalore", 92000),
    ("Hyderabad", 78000),
    ("Pune", 102000),
    ("Delhi", 98000)
)


print("Branches with sales above ₹90,000:")
for branch, sales in sales_data:
    if sales > 90000:
        print(branch)


total = 0
for branch, sales in sales_data:
    total += sales
average = total / len(sales_data)
print("\nAverage sales:", average)


lowest = sales_data[0]
for branch, sales in sales_data:
    if sales < lowest[1]:
        lowest = (branch, sales)
print("\nBranch with lowest sales:", lowest[0], "with ₹", lowest[1])


sales_list = list(sales_data)  
for i in range(len(sales_list)):
    if sales_list[i][0] == "Pune":
        sales_list[i] = ("Pune", 105000)
sales_data = tuple(sales_list)  
print("\nUpdated sales data:")
print(sales_data)
# sample output
# Branches with sales above ₹90,000:
# Bangalore
# Pune
# Delhi

# Average sales: 91000.0

# Branch with lowest sales: Hyderabad with ₹ 78000

# Updated sales data:
# (('Chennai', 85000), ('Bangalore', 92000), ('Hyderabad', 78000), ('Pune', 105000), ('Delhi', 98000))