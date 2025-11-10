sales_data = (
 ("Chennai", 85000),
 ("Bangalore", 92000),
 ("Hyderabad", 78000),
 ("Pune", 102000),
 ("Delhi", 98000)
)
sum=0
low=sales_data[0][1]
low_br=sales_data[0][0]
print(" All branches with sales above ₹90,000: ")
for branch_name, total_sales_amount in sales_data:
    sum+=total_sales_amount
    if total_sales_amount>90000:
        print(branch_name)
    if low>total_sales_amount:
        low=total_sales_amount
        low_br=branch_name
print("Average sales across all branch: ",sum//len(sales_data))
print("branch with the lowest sales: ",low_br)
sales_list = list(sales_data)

for i in range(len(sales_list)):
    if sales_list[i][0] == "Pune":
        sales_list[i] = ("Pune", 105000)

sales_data =tuple(sales_list)
print("Updated tuple: ",sales_data)

#  All branches with sales above ₹90,000: 
# Bangalore
# Pune
# Delhi
# Average sales across all branch:  91000
# branch with the lowest sales:  Hyderabad
# Updated tuple:  (('Chennai', 85000), ('Bangalore', 92000), ('Hyderabad', 78000), ('Pune', 105000), ('Delhi', 98000))