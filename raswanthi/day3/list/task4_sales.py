#Task 4:Daily Sales Dashboard

sales=[1200,1500,800,2200,1700,950]
sum_of_sales=sum(sales)
print("Total Sales:",sum_of_sales)
avg_sales=sum_of_sales//len(sales)
print("Average Sales:",avg_sales)
sales.append(1100)
sales.sort()
print("Sorted Sales:",sales)
print("Top 3 Sales:",sales[-3:])
print("Lowest 2 Sales:",sales[:2])
sales.remove(sales[0])
print("Updated Sales after removing smallest:",sales)

'''
Total Sales: 6
Average Sales: 1391
Sorted Sales: [800, 950, 1100, 1200, 1500, 1700, 2200]
Top 3 Sales: [1500, 1700, 2200]
Lowest 2 Sales: [800, 950]
Updated Sales after removing smallest: [950, 1100, 1200, 1500, 1700, 2200]
'''
