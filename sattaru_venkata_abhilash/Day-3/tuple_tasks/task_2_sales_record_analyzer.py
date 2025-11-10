# Task 2: Sales Record Analyzer
# Scenario:
# The company stores weekly sales data as tuples: (branch_name, total_sales_amount)

sales_data = (
    ("Chennai", 85000),
    ("Bangalore", 92000),
    ("Hyderabad", 78000),
    ("Pune", 102000),
    ("Delhi", 98000)
)

# 1. Print all branches with sales above ₹90,000
print("Branches with sales above ₹90,000:")
for branch, sales in sales_data:
    if sales > 90000:
        print(f"- {branch} (₹{sales})")

# 2. Find the average sales across all branches
total_sales = 0
for branch, sales in sales_data:
    total_sales += sales
average_sales = total_sales / len(sales_data)
print(f"\nAverage sales across all branches: ₹{average_sales:.2f}")

# 3. Identify and print the branch with the lowest sales
lowest_branch, lowest_sales = sales_data[0]
for branch, sales in sales_data:
    if sales < lowest_sales:
        lowest_sales = sales
        lowest_branch = branch
print(f"\nBranch with lowest sales: {lowest_branch} (₹{lowest_sales})")

# 4. Convert tuple to list, update Pune’s sales, and convert back to tuple
sales_list = list(sales_data)
for i in range(len(sales_list)):
    branch, sales = sales_list[i]
    if branch == "Pune":
        sales_list[i] = ("Pune", 105000)

updated_sales_data = tuple(sales_list)

# Print updated data
print("\nUpdated sales data:")
for branch, sales in updated_sales_data:
    print(f"- {branch}: ₹{sales}")


# Sample Output:
# Branches with sales above ₹90,000:
# - Bangalore (₹92000)
# - Pune (₹102000)
# - Delhi (₹98000)
#
# Average sales across all branches: ₹91000.00
#
# Branch with lowest sales: Hyderabad (₹78000)
#
# Updated sales data:
# - Chennai: ₹85000
# - Bangalore: ₹92000
# - Hyderabad: ₹78000
# - Pune: ₹105000
# - Delhi: ₹98000
