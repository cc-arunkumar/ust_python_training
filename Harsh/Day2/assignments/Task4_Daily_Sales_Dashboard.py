# Task 4: Daily Sales Dashboard
# Scenario:
# You work on a Sales Dashboard that tracks the daily sales revenue of your
# company’s products

# Daily Sales Dashboard
sales = [1200, 1500, 800, 2200, 1700, 950]

# Calculate total and average sales
total_sales = sum(sales)
average_sales = total_sales / len(sales)
print("Total sales for the day:", total_sales)
print("Average sales per transaction:", average_sales)

# Add a new sales entry
sales.append(1100)

# Sort sales and identify top 3 and lowest 2 sales
sales.sort()
print("Sorted Sales:", sales)
top_3 = sales[-3:]      
lowest_2 = sales[:2]    
print("Top 3 highest sales:", top_3)
print("Lowest 2 sales:", lowest_2)

# Remove the smallest sale
sales.remove(min(sales))
print("Updated Sales after removing smallest:", sales)


# Total sales for the day: 8350
# Average sales per transaction: 1391.6666666666667
# Sorted Sales: [800, 950, 1100, 1200, 1500, 1700, 2200]
# Top 3 highest sales: [1500, 1700, 2200]
# Lowest 2 sales: [800, 950]
# Updated Sales after removing smallest: [950, 1100, 1200, 1500, 1700, 2200]
