sales_data = (
("Chennai", 85000),
("Bangalore",92000),
("Hyderabad", 78000),
("Pune", 102000),
("Delhi", 98000)
)
sum = 0
max=99999999
lowest_sales = ''
for sales in sales_data:
    branch_name,total_sales_amount = sales
    sum+=total_sales_amount
    if max>total_sales_amount:
        max = total_sales_amount
        lowest_sales = branch_name
    if total_sales_amount>90000:
        print(branch_name)
sales_list = list(sales_data)
for i in range(len(sales_list)):
    branch, amount = sales_list[i]
    if branch == "Pune":
        sales_list[i] = ("Pune", 105000)
updated_sales_data = tuple(sales_list)
print(updated_sales_data)




print(f"lowest sales {lowest_sales} {max}")
print(sum/len(sales_data))

# =============sample output =====================
# Bangalore
# Pune
# Delhi
# (('Chennai', 85000), ('Bangalore', 92000), ('Hyderabad', 78000), ('Pune', 105000), ('Delhi', 98000))
# lowest sales Hyderabad 78000
# 91000.0