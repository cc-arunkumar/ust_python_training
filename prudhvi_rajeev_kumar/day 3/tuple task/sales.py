sales_data  = (
 ("Chennai", 85000),
 ("Bangalore", 92000),
 ("Hyderabad", 78000),
 ("Pune", 102000),
 ("Delhi", 98000)
)

for branch_name, total_sales_amount in sales_data:
    if total_sales_amount > 90000:
        print(branch_name)

total = 0
count_across = 0
for branch_name, total_sales_amount in sales_data:
    count_across += 1
    total += total_sales_amount
    average = total_sales_amount/count_across
print(average)

lowest_sales = 9999999
branch_lowest = ""
for branch_name, total_sales_amount in sales_data:
    if total_sales_amount < lowest_sales:
        lowest_sales = total_sales_amount
        branch_lowest = branch_name
print(branch_lowest)

#sample output!
# Bangalore
# Pune
# Delhi
# 19600.0
# Hyderabad
# PS C:\Users\303464\Desktop\Training> 