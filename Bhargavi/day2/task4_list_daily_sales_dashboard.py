#Daily Sales Dashboard

# Task 4: Daily Sales Dashboard
# Scenario:
# You work on a Sales Dashboard that tracks the daily sales revenue of your
# company’s products.

# Instructions:
# 1. Create a list named sales :
# [1200, 1500, 800, 2200, 1700, 950]
# 2. Calculate and print:
# Total sales for the day
# Average sales per transaction
# (Hint: use sum() and len() )
# 3. Add a new late entry of sale worth 1100 using append() .
# 4. Sort the sales in ascending order and print them.
# Day 3 4
# 5. Display:
# The top 3 highest sales
# The lowest 2 sales
# (Hint: use slicing [-3:] and [:2] )
# 6. Remove the smallest sale from the list and display the updated list.

# Initial sales data list
sales = [1200, 1500, 800, 2200, 1700, 950]

# Calculate total sales
total = sum(sales)
print("Total Sales:", total)

# Calculate average sales
average = total / len(sales)
print("Average Sale:", round(average, 2))  # rounded to 2 decimals

# Add a new sale entry
sales.append(1100)

# Sort sales in ascending order
sales.sort()
print("Sorted Sales:", sales)

# Print top 3 highest sales
print("Top 3 Sales:", sales[-3:])

# Print lowest 2 sales
print("Lowest 2 Sales:", sales[:2])

# Remove the smallest sale value
sales.remove(min(sales))
print("Updated Sales after removing smallest:", sales)

# Output:
# Total Sales: 8350
# Average Sale: 1391.67
# Sorted Sales: [800, 950, 1100, 1200, 1500, 1700, 2200]
# Top 3 Sales: [1500, 1700, 2200]
# Lowest 2 Sales: [800, 950]
# Updated Sales after removing smallest: [950, 1100, 1200, 1500, 1700, 2200]
