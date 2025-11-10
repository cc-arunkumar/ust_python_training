# Task 2: Sales Record Analyzer
# Scenario:
# Your company stores weekly sales data as tuples.

sales_data = (
 ("Chennai", 85000),
 ("Bangalore", 92000),
 ("Hyderabad", 78000),
 ("Pune", 102000),
 ("Delhi", 98000),
 )

tot_sales = 0
tot_branch = 0
print(f"branches with sales above ₹90,000 are :")
for branch,sal in sales_data:
    if(sal>90000):
        print(branch)
    
    tot_sales += sal
    tot_branch += 1
    avg = tot_sales/tot_branch
print(f"\naverage sales across all branches:{avg}\n")


min_branch = sales_data[0]
for branch in sales_data:
    if branch[1] < min_branch[1]:
        min_branch = branch
print(f"branch with the lowest sales.{min_branch}")


sales_list = list(sales_data)
for i in range(len(sales_list)):
    if sales_list[i][0] == "Pune":
        sales_list[i] = ("Pune", 105000)

updated_sales_data = tuple(sales_list)

# sample output:
# branches with sales above ₹90,000 are :
# Bangalore
# Pune
# Delhi

# average sales across all branches:91000.0

# branch with the lowest sales.('Hyderabad', 78000)