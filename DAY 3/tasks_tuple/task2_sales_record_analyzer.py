"""
Task 2: Sales Record Analyzer

Scenario:
Your company stores weekly sales data as tuples
Each tuple has:
(branch_name, total_sales_amount)
"""

sales_data = (
 ("Chennai", 85000),
 ("Bangalore", 92000),
 ("Hyderabad", 78000),
 ("Pune", 102000),
 ("Delhi", 98000)
)

total_sales=0

# Sales above ₹90,000
for city, sales in sales_data:
    total_sales += sales
    if sales > 90000:
        print(f"City has sales above 90,000: {city}")

# Average sales
avg_sales = total_sales / len(sales_data)
print("Average Sales:", avg_sales)

# Branch with the lowest sales
low_sales = float("inf")
low_sales_branch = ""

for branch, sales in sales_data:
    if sales < low_sales:
        low_sales = sales
        low_sales_branch = branch

print("Branch with the lowest sales:", low_sales_branch)

# Update Pune sales and convert to tuple
sales_list = list(sales_data)

for i in range(len(sales_list)):
    branch, sales = sales_list[i]
    if branch == "Pune":
        sales_list[i] = ("Pune", 105000)

latest_sales_tuple = tuple(sales_list)
print(latest_sales_tuple)

# sample output

"""
City has sales above 90,000: Bangalore
City has sales above 90,000: Pune
City has sales above 90,000: Delhi
Average Sales: 91000.0
Branch with the lowest sales: Hyderabad
(('Chennai', 85000), ('Bangalore', 92000), ('Hyderabad', 78000), ('Pune', 105000), ('Delhi', 98000))
"""
