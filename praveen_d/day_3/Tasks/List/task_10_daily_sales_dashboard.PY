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
# 3. Add a new late entry of sale worth 1100 using append() .
# 4. Sort the sales in ascending order and print them.
# 5. Display:
# The top 3 highest sales
# The lowest 2 sales
# 6. Remove the smallest sale from the list and display the updated list

sales=[1200, 1500, 800, 2200, 1700, 950]

total_sales=sum(sales)
no_of_sales=len(sales)
average_sales= total_sales/no_of_sales
print(f"Total sales:{total_sales}")
print(f"Average_sales:{average_sales}")

sales.append(1100)
sales.sort()
print(sales)

print(f"Highest sales:{sales[no_of_sales-3:no_of_sales]}")
print(f"Lowest sales:{sales[:2]}")

sales.pop(0)
print(sales)

# EXPECTED OUTPUT:
# PS C:\UST python> & C:/Users/303489/AppData/Local/Programs/Python/Python312/python.exe "c:/UST python/Praveen D/Day 3/Tasks/List/task_10_daily_sales_dashboard.PY"
# Total sales:8350
# Average_sales:1391.6666666666667
# [800, 950, 1100, 1200, 1500, 1700, 2200]
# Highest sales:[1200, 1500, 1700]
# Lowest sales:[800, 950]
# [950, 1100, 1200, 1500, 1700, 2200]
# PS C:\UST python> 




