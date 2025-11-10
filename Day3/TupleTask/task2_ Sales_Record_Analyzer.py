sales_data = (
    ("Chennai", 85000),
    ("Bangalore", 92000),
    ("Hyderabad", 78000),
    ("Pune", 102000),
    ("Delhi", 98000)
    )

for (branch_name, total_sales_amount) in sales_data:
    if(total_sales_amount>90000):
        print("Branches:",branch_name)


total_sale=0
for (branch_name, total_sales_amount) in sales_data:
    total_sale+=total_sales_amount
    avg=total_sale/len(sales_data)
print("average:",avg)




min_sales = 99999999
min_branch = ""
for branch_name, total_sales_amount in sales_data:
    if total_sales_amount < min_sales:
        min_sales = total_sales_amount
        min_branch = branch_name
print(f"Branch with lowest sales: {min_branch} (₹{min_sales})")




sales_list = list(sales_data)
for i in range(len(sales_list)):
    branch_name, total_sales_amount = sales_list[i]
    if branch_name == "Pune":
        sales_list[i] = ("Pune", 105000)
update_sales=tuple(sales_list)
print(update_sales)


# Branches: Bangalore
# Branches: Pune
# Branches: Delhi
# average: 91000.0
# Branch with the lowest sales: Hyderabad (₹78000)
# (('Chennai', 85000), ('Bangalore', 92000), ('Hyderabad', 78000), ('Pune', 105000), ('Delhi', 98000))




