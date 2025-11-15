#Task 2: Sales Record Analyzer

# Tuple representing sales data for each branch (Branch Name, Total Sales Amount)
sales_data = (("Chennai", 85000), ("Bangalore", 92000), ("Hyderabad", 78000), ("Pune", 102000), ("Delhi", 98000))

# Variable to hold the total sales amount across all branches
sales = 0

# Printing branches with sales greater than 90,000
print("Total Sales > 90000: ")
for branch_name, total_sales_amt in sales_data:
    if total_sales_amt > 90000:
        print(branch_name)

# Calculating the total sales and average sales across all branches
for branch_name, total_sales_amt in sales_data:
    sales += total_sales_amt  # Add the sales of the current branch to the total sales

# Calculate the average sales by dividing the total sales by the number of branches
avg_sales = sales / len(sales_data)
print("Average Sales: ", avg_sales)

# Finding the branch with the lowest sales using min() and lambda function
low_sales_branch = min(sales_data, key=lambda x: x[1])
print(f"Branch with the lowest sales: {low_sales_branch[0]}")

# Convert sales_data to a list so we can modify it (tuples are immutable)
sales_list = list(sales_data)

# Update the sales data for the "Pune" branch
for i in range(len(sales_list)):
    if sales_list[i][0] == "Pune":
        sales_list[i] = ("Pune", 105000)  # Update the sales for Pune
        break

# Convert the updated sales list back to a tuple
updated_sales_data = tuple(sales_list)

# Printing the updated sales data
print(updated_sales_data)



#Sample Execution
# Total Sales > 90000:
# Bangalore
# Pune
# Delhi
# Average Sales:  91000.0
# Branch with the lowest sales: Hyderabad
# (('Chennai', 85000), ('Bangalore', 92000), ('Hyderabad', 78000), ('Pune', 105000), ('Delhi', 98000))