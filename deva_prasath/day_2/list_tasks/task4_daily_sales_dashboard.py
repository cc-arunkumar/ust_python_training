#Daily Sales Dashboard
# You work on a Sales Dashboard that tracks the daily sales revenue of your
# company’s products

# List of sales figures
sales = [1200, 1500, 800, 2200, 1700, 950]

# Print the total sales (sum of the list)
print("Total sales:", sum(sales))

# Calculate and print the average sales
average = float(sum(sales) / len(sales))
print("Average sales:", round(average, 2))

# Add a new sale to the list
sales.append(1100)

# Sort the sales list in ascending order
sales.sort()

# Print the sorted sales list
print("Sorted sales:", sales)

# Print the top 3 highest sales
print("Top 3 sales:", sales[-3:])

# Print the lowest 2 sales
print("Lowest 2 sales: ", sales[:2])

# Remove the smallest sale (first element in the sorted list)
sales.remove(sales[0])

# Print the updated sales list after removal
print("Updated Sales after removing smallest:", sales)


#Sample output

# Total sales: 8350
# Average sales: 1391.67
# Sorted sales: [800, 950, 1100, 1200, 1500, 1700, 2200]
# Top 3 sales: [1500, 1700, 2200]
# Lowest 2 sales:  [800, 950]
#  Updated Sales after removing smallest: [950, 1100, 1200, 1500, 1700, 2200]