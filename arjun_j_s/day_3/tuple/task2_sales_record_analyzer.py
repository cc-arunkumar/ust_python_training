#Task 2: Sales Record Analyzer
sales_data = (
 ("Chennai", 85000),
 ("Bangalore", 92000),
 ("Hyderabad", 78000),
 ("Pune", 102000),
 ("Delhi", 98000)
)
summ=0
mini=sales_data[0][1]
mini_name=sales_data[0][0]
new_list=list(sales_data)
for place,sales in sales_data:
    if(sales<mini):
        mini = sales
        mini_name = place
    if(sales>90000):
        print(place)
    summ+=sales
print(summ/len(sales_data))
print("Lowest",mini_name)
for i in range(len(new_list)):
    if(new_list[i][0]=="Pune"):
        new_list[i]=("Pune",105000)
print(new_list)
print(tuple(new_list))
#Output
# Bangalore
# Pune
# Delhi
# 91000.0
# Lowest Hyderabad
# [('Chennai', 85000), ('Bangalore', 92000), ('Hyderabad', 78000), ('Pune', 105000), ('Delhi', 98000)]
# (('Chennai', 85000), ('Bangalore', 92000), ('Hyderabad', 78000), ('Pune', 105000), ('Delhi', 98000))