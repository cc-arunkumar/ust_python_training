"""
Scenario:
You work on a Sales Dashboard that tracks the daily sales revenue of your
company’s product

"""

# List of daily sales revenue
sales=[1200,1500,800,2200,1700,950]

# Calculate the total sales
total=sum(sales)

# Calculate the average sale
avg=total/len(sales)

# Print total sales
print("Total Sales:",total)

# Print average sale rounded to 2 decimal places
print("Average Sale:",round(avg,2))

# Add a new sale value to the list
sales.append(1100)

# Sort the sales list in ascending order
sales.sort()

# Print the sorted sales list
print("Sorted Sales:",sales)

# Print the top 3 sales
print("Top 3 Sales:",sales[-3:])

# Print the lowest 2 sales
print("Lowest 2 Sales:",sales[:2])

# Remove the smallest sale from the list
sales.remove(min(sales))

# Print the updated sales list after removing the smallest value
print("Updated Sales after removing smallest:",sales)


# sample output

"""
Total Sales: 8350
Average Sale: 1391.67
Sorted Sales: [800, 950, 1100, 1200, 1500, 1700, 2200]
Top 3 Sales: [1500, 1700, 2200]
Lowest 2 Sales: [800, 950]
Updated Sales after removing smallest: [950, 1100, 1200, 1500, 1700, 2200]

"""
