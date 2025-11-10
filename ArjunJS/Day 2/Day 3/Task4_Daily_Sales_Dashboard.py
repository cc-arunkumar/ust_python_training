#Task 4: Daily Sales Dashboard
sales = [1200, 1500, 800, 2200, 1700, 950]
print(f"Total Sales : {sum(sales)}")
print(f"Average Sales : { round(sum(sales)/len(sales),2)}")
sales.sort()
print(f"Sorted Sales : {sales}")
print(f"Top 3 Sales : {sales[3:6]}")
print(f"Lowest 2 Sales : {sales[:2]}")
sales.pop(0)
print(f"Updated Sales after removing smallest : {sales}")
# Output
# Total Sales : 8350
# Average Sales : 1391.67
# Sorted Sales : [800, 950, 1200, 1500, 1700, 2200]
# Top 3 Sales : [1500, 1700, 2200]
# Lowest 2 Sales : [800, 950]
# Updated Sales after removing smallest : [950, 1200, 1500, 1700, 2200]