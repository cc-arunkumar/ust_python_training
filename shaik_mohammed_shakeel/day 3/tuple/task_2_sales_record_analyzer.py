# Task 2- Sales Record Analyzer

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



from functools import reduce

sales_data = (
    ("Chennai", 85000),
    ("Bangalore", 92000),
    ("Hyderabad", 78000),
    ("Pune", 102000),
    ("Delhi", 98000)
)

for branch_name, total_sales in sales_data:
    if total_sales > 90000:
        print(branch_name)

total = reduce(lambda x, y: x + y, [sales for _, sales in sales_data])
avg_sales = total / len(sales_data)
print("Average Sales:", avg_sales)

min_branch = min(sales_data, key=lambda x: x[1])
print("Branch with lowest sales:", min_branch[0], "-", min_branch[1])

list1 = list(sales_data)
for i, (branch, sales) in enumerate(list1):
    if branch == "Pune":
        list1[i] = ("Pune", 105000)

sales_data = tuple(list1)
print("Updated sales data:", sales_data)

# Sample Output
# Bangalore
# Pune
# Delhi
# Average Sales: 91000.0
# Branch with lowest sales: Hyderabad - 78000
# Updated sales data: (('Chennai', 85000), ('Bangalore', 92000), ('Hyderabad', 78000), ('Pune', 105000), ('Delhi', 98000))