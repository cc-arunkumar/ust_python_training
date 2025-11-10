sales = [1200, 1500, 800, 2200, 1700, 950]

total_sales = sum(sales)
average_sales = total_sales / len(sales)
print("Total sales for the day:", total_sales)
print("Average sales per transaction:", average_sales)

sales.append(1100)

sales.sort()
print("Sorted Sales:", sales)

top_3 = sales[-3:]      
lowest_2 = sales[:2]    
print("Top 3 highest sales:", top_3)
print("Lowest 2 sales:", lowest_2)

sales.remove(min(sales))
print("Updated Sales after removing smallest:", sales)


# Total sales for the day: 8350
# Average sales per transaction: 1391.6666666666667
# Sorted Sales: [800, 950, 1100, 1200, 1500, 1700, 2200]
# Top 3 highest sales: [1500, 1700, 2200]
# Lowest 2 sales: [800, 950]
# Updated Sales after removing smallest: [950, 1100, 1200, 1500, 1700, 2200]
