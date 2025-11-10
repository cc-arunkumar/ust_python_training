# TASK 2 - Sales Record Analyzer

sales_data = ("Chennai", 85000),("Bangalore", 92000),("Hyderabad", 78000),("Pune", 102000),("Delhi", 98000)

for branch_name,total_sales_amount in sales_data:
    if total_sales_amount > 90000:
        print("Branches with sales above ₹90,000:",branch_name)


total_sales = sum(sales for branch,sales in sales_data)
avg = total_sales/len(sales_data)
print("Average Sales",avg)


lowest_branch, lowest_sales = sales_data[0]  

for branch_name, total_sales_amount in sales_data:
    if total_sales_amount < lowest_sales:
        lowest_branch = branch_name
        lowest_sales = total_sales_amount
print("Branch with lowest sales:", lowest_branch, "(", lowest_sales, ")")

sales_list = list(sales_data)

for i, (branch_name, total_sales_amount) in enumerate(sales_list):
    if branch_name == "Pune":
        sales_list[i] = ("Pune", 105000)

sales_data = tuple(sales_list)

print("Updated sales data:", sales_data)

# ------------------------------------------------------------------------

# Sample Output
# Branches with sales above ₹90,000: Bangalore
# Branches with sales above ₹90,000: Pune
# Branches with sales above ₹90,000: Delhi
# Average Sales 91000.0
# Branch with lowest sales: Hyderabad ( 78000 )
# Updated sales data: (('Chennai', 85000), ('Bangalore', 92000), ('Hyderabad', 78000), ('Pune', 105000), ('Delhi', 98000))
