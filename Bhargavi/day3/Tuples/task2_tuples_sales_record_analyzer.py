# Sales Record Analyzer

# Task 2: Sales Record Analyzer

# Scenario:
# Your company stores weekly sales data as tuples.

# Each tuple has:
# (branch_name, total_sales_amount)
# Example data:
# sales_data = (("Chennai", 85000),("Bangalore", 92000),("Hyderabad", 78000),("Pune", 102000),("Delhi", 98000))

# Your Tasks:
# 1. Print all branches with sales above ₹90,000.
# 2. Find the average sales across all branches.
# 3. Identify and print the branch with the lowest sales.
# 4. Convert this tuple data into a list of tuples and update Pune’s sales to 105000 ,
# then convert it back to a tuple and print the updated data.


# Tuple of branch sales data (branch, sales_amount)
sales_data = (
    ("Chennai", 85000),
    ("Bangalore", 92000),
    ("Hyderabad", 78000),
    ("Pune", 102000),
    ("Delhi", 98000)
)

# Print branches with sales greater than 90,000
for branch, sales in sales_data:
    if sales > 90000:
        print(branch)

# Calculate average sales across all branches
total = 0
for branch, sales in sales_data:
    total += sales
average = total / len(sales_data)
print("Average:", average)

# Find branch with lowest sales
lowest = sales_data[0]   # assume first branch is lowest initially
for branch in sales_data:
    if branch[1] < lowest[1]:
        lowest = branch
print("Lowest:", lowest[0])

# Update Pune branch sales to 105,000
sales_list = list(sales_data)   # convert tuple to list for modification
for i in range(len(sales_list)):
    if sales_list[i][0] == "Pune":
        sales_list[i] = ("Pune", 105000)
sales_data = tuple(sales_list)  # convert back to tuple
print("Updated data:", sales_data)

#  Output:
# Bangalore
# Pune
# Delhi
# Average: 91000.0
# Lowest: Hyderabad
# Updated data: (('Chennai', 85000), ('Bangalore', 92000), ('Hyderabad', 78000), ('Pune', 105000), ('Delhi', 98000))
