#Task 4: Daily Sales Dashboard
sales=[1200, 1500, 800, 2200, 1700, 950]
print("Total Sales: ",sum(sales))
print("Average Sale: ",sum(sales)/len(sales))
sales.append(1100)
print("Sorted Sales: ",sales.sort())
print("Top 3 Sales: ",sales[:3:-1])
print("Lowest 2 Sales: ",sales[:2])
del sales[0]
print("Updated Sales after removing smallest: ",sales)

#Sample output
# Total Sales:  8350
# Average Sale:  1391.6666666666667
# Sorted Sales:  None
# Top 3 Sales:  [2200, 1700, 1500]
# Lowest 2 Sales:  [800, 950]
# Updated Sales after removing smallest:  [950, 1100, 1200, 1500, 1700, 2200]
