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


total_sales=0
for branch,sales_amount in sales_data:

    total_sales+=sales_amount

    if(sales_amount>90000):
        print(branch)

avg_sales=total_sales/len(sales_data)

min_sales=85000

for branch,sales_amount in sales_data:
    if sales_amount<min_sales:
        min_sales=sales_amount


list_of_sales_data=list(sales_data)

for i in range (len(list_of_sales_data)):
    if list_of_sales_data[i][0]=="Pune":
        list_of_sales_data[i]="Pune",105000

tuple1=tuple(list_of_sales_data)

print(tuple1)  

# Bangalore
# Pune
# Delhi
# (('Chennai', 85000), ('Bangalore', 92000), ('Hyderabad', 78000), ('Pune', 105000), ('Delhi', 98000))