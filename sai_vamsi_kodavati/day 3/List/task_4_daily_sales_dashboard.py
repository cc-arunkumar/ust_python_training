# TASK 4 - Daily Sales Dashboard

sales = [1200, 1500, 800, 2200, 1700, 950]
total = sum(sales)
print("Total Sales: ",total)

avg = total//len(sales)
print("Average sales per transaction: ",avg)

sales.append(1100)
sales.sort()

print("Top 3 Sales: ",sales[-3:])
print("Lowest 2 Sales: ",sales[:2])
sales.pop(0)

print("Updated Sales after removing smallest: ",sales)

# Sample Output
# Total Sales:  8350
# Average sales per transaction:  1391
# Top 3 Sales:  [1500, 1700, 2200]
# Lowest 2 Sales:  [800, 950]
# Updated Sales after removing smallest:  [950, 1100, 1200, 1500, 1700, 2200]