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




