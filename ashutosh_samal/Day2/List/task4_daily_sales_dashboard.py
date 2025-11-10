#Task 4: Daily Sales Dashboard

sales = [1200,1500,800,2200,1700,950]

print("Total sales: ",sum(sales))
print("Average sales: ",sum(sales)/len(sales))

sales.append(1100)
sales.sort()
print("Sorted Sales: ",sales)

print("Top 3 sales: ",sales[-3:])
print("Lowest 2 sales: ",sales[:2])

sales.remove(sales[0])
print("Updated Sales after removing smallest: ",sales)

#Sample Output
# Total sales:  8350
# Average sales:  1391.6666666666667
# Sorted Sales:  [800, 950, 1100, 1200, 1500, 1700, 2200]
# Top 3 sales:  [1500, 1700, 2200]
# Lowest 2 sales:  [800, 950]
# Updated Sales after removing smallest:  [950, 1100, 1200, 1500, 1700, 2200]