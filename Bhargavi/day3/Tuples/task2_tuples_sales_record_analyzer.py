# Sales Record Analyzer
sales_data = (("Chennai", 85000),("Bangalore", 92000),("Hyderabad", 78000),("Pune", 102000),("Delhi", 98000))
for branch, sales in sales_data:
    if sales > 90000:
        print(branch)

total = 0
for branch, sales in sales_data:
    total += sales
average = total / len(sales_data)
print("Average:", average)

lowest = sales_data[0]
for branch in sales_data:
    if branch[1] < lowest[1]:
        lowest = branch
print("Lowest:", lowest[0])

sales_list = list(sales_data)
for i in range(len(sales_list)):
    if sales_list[i][0] == "Pune":
        sales_list[i] = ("Pune", 105000)
sales_data = tuple(sales_list)
print("Updated data:", sales_data)

# Bangalore
# Pune
# Delhi
# Average: 91000.0
# Lowest: Hyderabad
# Updated data: (('Chennai', 85000), ('Bangalore', 92000), ('Hyderabad', 78000), ('Pune', 105000), ('Delhi', 98000))