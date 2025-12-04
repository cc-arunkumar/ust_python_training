#Task 2: Sales Record Analyzer
sales_data = (
    ("Chennai", 85000),
    ("Bangalore", 92000),
    ("Hyderabad", 78000),
    ("Pune", 102000),
    ("Delhi", 98000)
)


for branch, sales in sales_data:
    if sales > 90000:
        print(f"{branch}: {sales}")

total_sales = 0
count = 0
for branch, sales in sales_data:
    total_sales += sales
    count += 1

average_sales = total_sales / count
print(f"Average sales across all branches: {average_sales}")

def get_sales(item):
    return item[1]

lowest_branch = min(sales_data, key=get_sales)
print(f"Branch with the lowest sales: {lowest_branch[0]} ({lowest_branch[1]})")


sales_data = (("Mumbai", 95000), ("Delhi", 88000), ("Pune", 91000), ("Chennai", 87000))
sales_list = list(sales_data)

for i in range(len(sales_list)):
    if sales_list[i][0] == "Pune":
        sales_list[i] = ("Pune", 105000)

updated_sales_data = tuple(sales_list)
print(updated_sales_data)

'''
output:
Bangalore: 92000
Pune: 102000
Delhi: 98000
Average sales across all branches: 91000.0
Branch with the lowest sales: Hyderabad (78000)
(('Mumbai', 95000), ('Delhi', 88000), ('Pune', 105000), ('Chennai', 87000))
'''