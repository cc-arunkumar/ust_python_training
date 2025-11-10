#Task 4: Daily Sales Dashboard

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

# Expected Output(sample):
# Total Sales: 8350
# Average Sale: 1391.67
# Sorted Sales: [800, 950, 1100, 1200, 1500, 1700, 2200]
# Top 3 Sales: [1500, 1700, 2200]
# Lowest 2 Sales: [800, 950]
# Updated Sales after removing smallest: [950, 1100, 1200, 1500, 1700, 2200]

sales=[1200, 1500, 800, 2200, 1700, 950]
total_sales = sum(sales)
print("Total Sales:",total_sales)
avg_sales = total_sales/len(sales)
print("Average Sales:",avg_sales)
sales.append(1100)
sorted_sales = sorted(sales)
print("Sorted Sales:",sorted_sales)
top_three_sales = sorted_sales[-3:]
print("Top Three Sales:",top_three_sales)
print("Lowest 2 Sales:",sorted(sales)[:2])
lowest_sale = min(sales)
sorted_sales.remove(lowest_sale)
print("Updated Sales after removing smallest: ",sorted_sales)

#Sample Output
# Total Sales: 8350
# Average Sales: 1391.6666666666667
# Sorted Sales: [800, 950, 1100, 1200, 1500, 1700, 2200]
# Top Three Sales: [1500, 1700, 2200]
# Lowest 2 Sales: [800, 950]
# Updated Sales after removing smallest:  [950, 1100, 1200, 1500, 1700, 2200]

