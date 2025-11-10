#  Sales_Record_Analyzer

sales_data = (
 ("Chennai", 85000),
 ("Bangalore", 92000),
 ("Hyderabad", 78000),
 ("Pune", 102000),
 ("Delhi", 98000)
)

total = 0
count = 0
min=sales_data[0][1]
branch = sales_data[0]

print("Branches with sales above $90,000:")
for (city,sales) in sales_data:
    if sales>90000:
        print(city)
    total += sales
    count += 1
    if sales<min:
        min = sales
        branch = city

print("Average sales: ",total/count)
print("Branch with the lowest sales: ",branch)

list1 = list(sales_data)
for i in range(len(list1)):
    if list1[i][0] == "Pune":
        list1[i]=("Pune",105000)
        
new_sales_data = tuple(list1)
print("Updates data: ",new_sales_data)

# output

# Branches with sales above $90,000:
# Bangalore
# Pune
# Delhi
# Average sales:  91000.0
# Branch with the lowest sales:  Hyderabad
# Updates data:  (('Chennai', 85000), ('Bangalore', 92000), ('Hyderabad', 78000), ('Pune', 105000), ('Delhi', 98000))
