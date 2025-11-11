# Task 4: Daily Sales Dashboard
sales=[1200, 1500, 800, 2200, 1700, 950]
total=sum(sales)
print("Total Sales:",total)
average=total/len(sales)
print(f"Average Sale: {average:.2f}")
sales.append(1100)
sales.sort()
print("Sorted Sales:",sales)
print("Top 3 Sales:",sales[-3:])
print("Lowest 2 Sales:",sales[:2])
sales.pop(0)
print("Updated Sales after removing smallest:",sales)
# Sample output
# Total Sales: 8350
# Average Sale: 1391.67
# Sorted Sales: [800, 950, 1100, 1200, 1500, 1700, 2200]
# Top 3 Sales: [1500, 1700, 2200]
# Lowest 2 Sales: [800, 950]
# Updated Sales after removing smallest: [950, 1100, 1200, 1500, 1700, 2200]
