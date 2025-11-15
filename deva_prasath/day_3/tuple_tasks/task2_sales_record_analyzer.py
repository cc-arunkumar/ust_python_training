# Sales Record Analyzer

# Your company stores weekly sales data as tuples.


# Tuple storing sales data with branch name and sales amount
sales_data = (
    ("Chennai", 85000),
    ("Bangalore", 92000),
    ("Hyderabad", 78000),
    ("Pune", 102000),
    ("Delhi", 98000)
)

# Initialize variables to calculate total sales and count of branches
sum, count = 0, 0

# Loop through sales data and print branches with sales above 90000
for i, j in sales_data:
    if j > 90000:
        print("Sales above 90000:", i)
    sum += j  # Add sales amount to total sum
    count += 1  # Increment branch count

# Calculate and print the average sales across all branches
print("Average sales across all branches: ", (sum / count) * 100)

# Find the branch with the lowest sales
lowest = sales_data[0]  # Assume first entry as lowest initially
for branch in sales_data:
    if branch[1] < lowest[1]:
        lowest = branch  # Update if a lower sales branch is found

# Print the branch with the lowest sales
print(f"Branch with the lowest sales: {lowest[0]}")

# Create a list of sales data and update the sales for Pune branch
li1 = list(sales_data)
for i in li1:
    li2 = list(i)  # Convert tuple to list for modification
    if li2[0] == "Pune":
        li2[1] = 105000  # Update Pune branch sales to 105000
    print(tuple(li2))  # Print the updated branch data as a tuple



#Sample output

# Sales above 90000: Bangalore
# Sales above 90000: Pune
# Sales above 90000: Delhi
# Average sales across all branches:  9100000.0
# Branch with the lowest sales: Hyderabad
# ('Chennai', 85000)
# ('Bangalore', 92000)
# ('Hyderabad', 78000)
# ('Pune', 105000)
# ('Delhi', 98000)