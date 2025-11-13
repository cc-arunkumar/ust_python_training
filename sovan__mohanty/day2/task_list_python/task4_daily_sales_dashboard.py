#Task 4 Daily Sales Dashboard
sales=[1200, 1500, 800, 2200, 1700, 950]
print("Total Sales: ",sum(sales))
average_sales=sum(sales)/len(sales)
print("Average Sales: ",average_sales)
sales.append(1100)
sales.sort()
print("Sorted Sales: ",sales)
print("Top 3 sales: ",sales[-3:])
print("Top 2 sales: ",sales[:2])
sales.pop(0)
print("Updated Sales after removing smallest: ",sales)

#Sample Executions
# Total Sales:  8350
# Average Sales:  1391.6666666666667
# Sorted Sales:  [800, 950, 1100, 1200, 1500, 1700, 2200]
# Top 3 sales:  [1500, 1700, 2200]
# Top 2 sales:  [800, 950]
# Updated Sales after removing smallest:  [950, 1100, 1200, 1500, 1700, 2200]