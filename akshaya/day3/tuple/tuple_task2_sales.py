# Task 2: Sales Record Analyzer

sales_data = (
    ("Chennai", 85000),
    ("Bangalore", 92000),
    ("Hyderabad", 78000),
    ("Pune", 102000),
    ("Delhi", 98000)
)


print("Branches with sales above ₹90,000:")
for branch, sales in sales_data:
    if sales > 90000:
        print(branch)


total_sales = 0
for branch, sales in sales_data:
    total_sales += sales
average_sales = total_sales / len(sales_data)
print(f"\nAverage sales across all branches: ₹{average_sales}")


lowest_sales = float('inf')
lowest_branch = ""
for branch, sales in sales_data:
    if sales < lowest_sales:
        lowest_sales = sales
        lowest_branch = branch
print(f"\nBranch with lowest sales: {lowest_branch} (₹{lowest_sales})")


sales_list = list(sales_data)
for i in range(len(sales_list)):
    branch, sales = sales_list[i]
    if branch == "Pune":
        sales_list[i] = ("Pune", 105000) 

updated_sales_data = tuple(sales_list)
print("\nUpdated sales data:", updated_sales_data)


#sample output
#Branches with sales above ₹90,000:
#Bangalore
#Pune
#Delhi

#Average sales across all branches: ₹91000.0

#Branch with lowest sales: Hyderabad (₹78000)

#Updated sales data: (('Chennai', 85000), ('Bangalore', 92000), ('Hyderabad', 78000), ('Pune', 105000), ('Delhi', 98000))
