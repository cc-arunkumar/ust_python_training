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
# then convert it back to a tuple and print the updated data

#Code

sales_data = (
    ("Chennai", 85000),
    ("Bangalore", 92000),
    ("Hyderabad", 78000),
    ("Pune", 102000),
    ("Delhi", 98000)
)
print("Branches with sales above ₹90,000:")
for branch_name, total_sales_amount in sales_data:
    if total_sales_amount > 90000:
        print(branch_name)

No_sales = 0
for branch_name, total_sales_amount in sales_data:
    No_sales += total_sales_amount
avg = No_sales / len(sales_data)
print("Average sales across all branches:", avg)

min_sales = float('inf')
min_branch = ""
for branch_name, total_sales_amount in sales_data:
    if total_sales_amount < min_sales:
        min_sales = total_sales_amount
        min_branch = branch_name
print(f"Branch with lowest sales: {min_branch} ({min_sales})")

sales_list = list(sales_data)
i = 0
while i < len(sales_list):
    if sales_list[i][0] == "Pune":
        sales_list[i] = ("Pune", 105000)
        break
    i += 1

updated_sales_data = tuple(sales_list)
print("Updated Sales Data:")
print(updated_sales_data)

#output
# PS C:\Users\303379\day3_training> & C:/Users/303379/AppData/Local/Microsoft/WindowsApps/python3.13.exe c:/Users/303379/day3_training/task2_Sales_Record_Analyzer.py
# Branches with sales above ₹90,000:
# Bangalore
# Pune
# Delhi
# Average sales across all branches: 91000.0
# Branch with lowest sales: Hyderabad (78000)
# Updated Sales Data:
# (('Chennai', 85000), ('Bangalore', 92000), ('Hyderabad', 78000), ('Pune', 105000), ('Delhi', 98000))
# PS C:\Users\303379\day3_training> 