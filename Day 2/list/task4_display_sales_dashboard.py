# Task 4: Daily Sales Dashboard
# Scenario:
# You work on a Sales Dashboard that tracks the daily sales revenue of your
# company’s products.


sales=[1200,1500,800,2200,1700,950]
total=sum(sales)
avg=total/len(sales)
print("Total Sales:",total)
print("Average Sale:",round(avg,2))
sales.append(1100)
sales.sort()
print("Sorted Sales:",sales)
print("Top 3 Sales:",sales[-3:])
print("Lowest 2 Sales:",sales[:2])
sales.remove(min(sales))
print("Updated Sales after removing smallest:",sales)


# sample output:

# Total Sales: 8350
# Average Sale: 1391.67
# Sorted Sales: [800, 950, 1100, 1200, 1500, 1700, 2200]
# Top 3 Sales: [1500, 1700, 2200]
# Lowest 2 Sales: [800, 950]
# Updated Sales after removing smallest: [950, 1100, 1200, 1500, 1700, 2200]