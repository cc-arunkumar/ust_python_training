#Task 2: Sales Record Analyzer

sales_data =(("Chennai", 85000),("Bangalore", 92000),("Hyderabad", 78000),("Pune", 102000),("Delhi", 98000))
sales=0
print("Total Sales > 90000: ")
for branch_name, total_sales_amt in sales_data:
    if (total_sales_amt>90000):
        print(branch_name)
    

for branch_name, total_sales_amt in sales_data:
    sales=sales+total_sales_amt
    avg_sales = sales/len(sales_data)
print("Average Sales: ",avg_sales)

low_sales_branch = min(sales_data,key=lambda x:x[1])
print(f"Branch with the lowest sales: {low_sales_branch[0]}")

sales_list = list(sales_data)

for i in range(len(sales_list)):
    if sales_list[i][0] == "Pune":
        sales_list[i] = ("Pune", 105000)
        break
updated_sales_data = tuple(sales_list)
print(updated_sales_data)


#Sample Execution
# Total Sales > 90000:
# Bangalore
# Pune
# Delhi
# Average Sales:  91000.0
# Branch with the lowest sales: Hyderabad
# (('Chennai', 85000), ('Bangalore', 92000), ('Hyderabad', 78000), ('Pune', 105000), ('Delhi', 98000))