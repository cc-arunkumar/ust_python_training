#Daily Sales Dashboard
# You work on a Sales Dashboard that tracks the daily sales revenue of your
# company’s products

sales= [1200, 1500, 800, 2200, 1700, 950]
print("Total sales:",sum(sales))
average=float(sum(sales)/len(sales))
print("Average sales:",round(average,2))
sales.append(1100)
sales.sort()
print("Sorted sales:",sales)
print("Top 3 sales:",sales[-3:])
print("Lowest 2 sales: ",sales[:2])
sales.remove(sales[0])
print(" Updated Sales after removing smallest:",sales)



#Sample output

# Total sales: 8350
# Average sales: 1391.67
# Sorted sales: [800, 950, 1100, 1200, 1500, 1700, 2200]
# Top 3 sales: [1500, 1700, 2200]
# Lowest 2 sales:  [800, 950]
#  Updated Sales after removing smallest: [950, 1100, 1200, 1500, 1700, 2200]