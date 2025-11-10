# #Task 4: Daily Sales Dashboard
# Scenario:
# You work on a Sales Dashboard that tracks the daily sales revenue of your
# company’s products.
# Instructions:
# 1. Create a list named sales :
# [1200, 1500, 800, 2200, 1700, 950]
# 2. Calculate and print:
# Total sales for the day
# Average sales per transaction
# (Hint: use sum() and len() )
# 3. Add a new late entry of sale worth 1100 using append() .
# 4. Sort the sales in ascending order and print them.
# 5. Display:
# The top 3 highest sales
# The lowest 2 sales
# (Hint: use slicing [-3:] and [:2] )
# 6. Remove the smallest sale from the list and display the updated list.

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
