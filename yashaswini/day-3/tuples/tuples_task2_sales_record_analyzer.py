# sales Record Analyzer
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

sales_data = (("Chennai", 85000),("Bangalore", 92000),("Hyderabad", 78000),("Pune", 102000),("Delhi", 98000))
print("Braches with sales above 90,000:")
for branch_name,total_sales_amount in sales_data:
    if total_sales_amount>90000:
        print(branch_name)
total_sales = sum(amount for _, amount in sales_data)
average_sales = total_sales / len(sales_data)
print("Average Sales across all branches:", average_sales)
lowest_branch = min(sales_data, key=lambda x: x[1])
print("Branch with the lowest sales:", lowest_branch[0], "-", lowest_branch[1])
sales_list = list(sales_data)
for i, (branch, sales) in enumerate(sales_list):
    if branch == "Pune":
        sales_list[i] = ("Pune", 105000)
updated_sales_data = tuple(sales_list)
print("Updated Sales Data:")
for branch, sales in updated_sales_data:
    print(branch, "-", sales)


#o/p:
# Braches with sales above 90,000:
# Bangalore
# Pune
# Delhi
# Average Sales across all branches: 91000.0
# Branch with the lowest sales: Hyderabad - 78000
# Updated Sales Data:
# Chennai - 85000
# Bangalore - 92000
# Hyderabad - 78000
# Pune - 105000
# Delhi - 98000