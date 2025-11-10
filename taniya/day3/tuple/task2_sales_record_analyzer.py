tuple1 = (("Chennai", 85000),
 ("Bangalore", 92000),
 ("Hyderabad", 78000),
 ("Pune", 102000),
 ("Delhi", 98000))
for branch_name, total_sales_amount in tuple1:
    if total_sales_amount > 90000:
        print("branch with sale above 90000:",branch_name)

sum = 0
sum += total_sales_amount
count = len(tuple1)

average = sum/count
print("total average of sales:",average)

for branch_name, total_sales_amount in tuple1:
    if total_sales_amount < 90000:
    
     print("branch with lowest sales:",branch_name)


sales_list = list(tuple1)
for i in range(len(sales_list)):
    if sales_list[i][0] == "Pune":
        sales_list[i] = ("Pune", 105000)

tuple2 = tuple(sales_list)
print("Updated branch data:", tuple2)

# output
# total average of sales: 19600.0
# branch with lowest sales: Chennai
# branch with lowest sales: Hyderabad
# Updated branch data: (('Chennai', 85000), ('Bangalore', 92000), ('Hyderabad', 78000), ('Pune', 105000), ('Delhi', 98000))
