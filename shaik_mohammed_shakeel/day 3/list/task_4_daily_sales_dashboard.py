# Task 4: Daily Sales Dashboard

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
# Day 3 4
# 5. Display:
# The top 3 highest sales
# The lowest 2 sales
# (Hint: use slicing [-3:] and [:2] )
# 6. Remove the smallest sale from the list and display the updated list

sales=[1200, 1500, 800, 2200, 1700, 950]
Total_sales=len(sales)
total=sum(sales)
avg=(total/Total_sales)
print(Total_sales)
print("Total sale: ",total)
print("Average sale: ",avg)
sales.sort()
print("Sorted List: ",sales)
print("Top 3 sales:", sales[-3:])
print("Lowest 2 sales: ",sales[:2])
sales.pop(0)
print("Updated Sales after removing smallest:",sales)

#sample output
# Total sale:  8350
# Average sale:  1391.6666666666667
# Sorted List:  [800, 950, 1200, 1500, 1700, 2200]
# Top 3 sales: [1500, 1700, 2200]
# Lowest 2 sales:  [800, 950]
# Updated Sales after removing smallest: [950, 1200, 1500, 1700, 2200]