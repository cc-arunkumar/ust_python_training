#Task 2: Sales Record Analyzer
sales_data = (
 ("Chennai", 85000),
 ("Bangalore", 92000),
 ("Hyderabad", 78000),
 ("Pune", 102000),
 ("Delhi", 98000)
)

sum=0
count=0
min=1100000
name="k"
for(branch_name, total_sales_amount) in sales_data:
    if(total_sales_amount>90000):
        print(branch_name)
    sum+=total_sales_amount
    count+=1
    if(min>total_sales_amount):
        min=total_sales_amount
        name=branch_name
print("average sales: ",sum/count)
new=list(sales_data)

for i in range(len(new)):
    if new[i][0] == "Pune":
        new[i] = ("Pune", 105000)


newsales_data=tuple(new)
print(newsales_data)

#Sample output
# Bangalore
# Pune
# Delhi
# average sales:  91000.0
# (('Chennai', 85000), ('Bangalore', 92000), ('Hyderabad', 78000), ('Pune', 105000), ('Delhi', 98000))
