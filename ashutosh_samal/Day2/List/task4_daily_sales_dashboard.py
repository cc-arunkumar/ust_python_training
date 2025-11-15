#Task 4: Daily Sales Dashboard

# List of sales for the period
sales = [1200, 1500, 800, 2200, 1700, 950]

# Printing the total sales using the sum() function
print("Total sales: ", sum(sales))

# Printing the average sales by dividing the total sales by the number of elements
print("Average sales: ", sum(sales) / len(sales))

# Adding a new sales value (1100) to the list
sales.append(1100)

# Sorting the sales list in ascending order
sales.sort()
print("Sorted Sales: ", sales)

# Printing the top 3 highest sales (last 3 elements after sorting)
print("Top 3 sales: ", sales[-3:])

# Printing the lowest 2 sales (first 2 elements after sorting)
print("Lowest 2 sales: ", sales[:2])

# Removing the smallest sales value (first element after sorting)
sales.remove(sales[0])
print("Updated Sales after removing smallest: ", sales)


#Sample Output
# Total sales:  8350
# Average sales:  1391.6666666666667
# Sorted Sales:  [800, 950, 1100, 1200, 1500, 1700, 2200]
# Top 3 sales:  [1500, 1700, 2200]
# Lowest 2 sales:  [800, 950]
# Updated Sales after removing smallest:  [950, 1100, 1200, 1500, 1700, 2200]