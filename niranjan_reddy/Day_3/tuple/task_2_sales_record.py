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

average=0
total=0
length=0

min_branch,min_sales=sales_data[0]


# 1. Print all branches with sales above ₹90,000.
for branch_name, total_sales_amount in sales_data:
    if total_sales_amount>90000:
        print(f"Branch Name: {branch_name}, Total Sales: {total_sales_amount}")
    total+=total_sales_amount
    length+=1

    # 3. Identify and print the branch with the lowest sales.
    if total_sales_amount<min_sales:
        min_sales=total_sales_amount
        min_branch=branch_name
        
# 2. Find the average sales across all branches.
average=total/length
print(f"Average:",average)
print(f"Branch name: {min_branch}, {min_sales}")


# 4. Convert this tuple data into a list of tuples and update Pune’s sales to 105000 ,
# then convert it back to a tuple and print the updated data.
sales_list=list(sales_data)
for i, (branch,sales) in enumerate(sales_list):
    if branch=="Pune":
        sales_list[i]=("Pune",105000)

sales_data=tuple(sales_list)
print("Sales Data:",sales_data)


# Sample output

# Branch Name: Bangalore, Total Sales: 92000

# Branch Name: Pune, Total Sales: 102000

# Branch Name: Delhi, Total Sales: 98000

# Branch name: Hyderabad, 78000

# Average: 91000.0

# Sales Data: (('Chennai', 85000), ('Bangalore', 92000), ('Hyderabad', 78000), ('Pune', 105000), ('Delhi', 98000))