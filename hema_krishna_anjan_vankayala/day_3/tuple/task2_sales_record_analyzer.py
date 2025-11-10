#Task 2: Sales Record Analyzer

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

branches_more_than_90000 = [i[1] for i in sales_data if i[1]>=90000]
print("Branches with sales more than or equal to 90000:", branches_more_than_90000)

average_sales_all_branches = ((sum([i[1] for i in sales_data]))/len(sales_data))
print("Average sales across all branches:", average_sales_all_branches)

lowest_sale = min([i[1] for i in sales_data])
lowest_branch = [branch[1] for branch in sales_data if branch[1]==lowest_sale]
print("Lowest sale in:", lowest_branch[0])

list_data = list(sales_data)
for i in range(len(list_data)):
    if list_data[i][0]=="Pune":
        list_data[i] = ("Pune",105000)

print("updated sales data:", tuple(list_data))

#Sample Output
# Branches with sales more than or equal to 90000: [92000, 102000, 98000]
# Average sales across all branches: 91000.0
# Lowest sale in: 78000
# updated sales data: (('Chennai', 85000), ('Bangalore', 92000), ('Hyderabad', 78000), ('Pune', 105000), ('Delhi', 98000))