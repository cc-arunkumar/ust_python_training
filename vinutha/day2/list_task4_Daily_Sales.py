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
# 6. Remove the smallest sale from the list and display the updated list.

#Code

sales = [1200, 1500, 800, 2200, 1700, 950]

print("Total Sales:", sum(sales))
print("Average Sale:", round(sum(sales)/len(sales), 2))

sales.append(1100)
sales.sort()
print("Sorted Sales:", sales)
print("Top 3 Sales:", sales[-3:])
print("Lowest 2 Sales:", sales[:2])

sales.pop(0)
print("Updated Sales:", sales)

# output
# PS C:\Users\303379\day3_training> & C:/Users/303379/AppData/Local/Microsoft/WindowsApps/python3.13.exe c:/Users/303379/day3_training/task4_Daily_Sales
# Total Sales: 8350
# Average Sale: 1391.67
# Sorted Sales: [800, 950, 1100, 1200, 1500, 1700, 2200]
# Top 3 Sales: [1500, 1700, 2200]
# Lowest 2 Sales: [800, 950]
# Updated Sales: [950, 1100, 1200, 1500, 1700, 2200]
# PS C:\Users\303379\day3_training> 

