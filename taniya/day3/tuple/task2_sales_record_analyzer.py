# Tuple containing branch names and their total sales
tuple1 = (
    ("Chennai", 85000),
    ("Bangalore", 92000),
    ("Hyderabad", 78000),
    ("Pune", 102000),
    ("Delhi", 98000)
)

# Print branches with sales above 90,000
for branch_name, total_sales_amount in tuple1:
    if total_sales_amount > 90000:
        print("branch with sale above 90000:", branch_name)

# ⚠️ Issue: sum is updated only once with the last value of total_sales_amount (98000).
# Correct way would be: sum = sum(x[1] for x in tuple1)
sum = 0
sum += total_sales_amount   # This only adds Delhi’s sales (98000)
count = len(tuple1)

# Average calculation (incorrect because sum is not total of all branches)
average = sum / count
print("total average of sales:", average)

# Print branches with sales below 90,000
for branch_name, total_sales_amount in tuple1:
    if total_sales_amount < 90000:
        print("branch with lowest sales:", branch_name)

# Convert tuple to list to allow modification
sales_list = list(tuple1)

# Update Pune’s sales to 105000
for i in range(len(sales_list)):
    if sales_list[i][0] == "Pune":
        sales_list[i] = ("Pune", 105000)

# Convert back to tuple after modification
tuple2 = tuple(sales_list)
print("Updated branch data:", tuple2)

# -------------------------
# Expected Output (with your current logic):
# total average of sales: 19600.0
# branch with lowest sales: Chennai
# branch with lowest sales: Hyderabad
# Updated branch data: (('Chennai', 85000), ('Bangalore', 92000), ('Hyderabad', 78000), ('Pune', 105000), ('Delhi', 98000))