# Task 4: Daily Sales Dashboard
# Scenario:
# You work on a Sales Dashboard that tracks the daily sales revenue of your
# company’s products



# Step:1 Initialize the sales data list
sales = [1200, 1500, 800, 2200, 1700, 950]

# Step:2 Calculate the total sales
ans = sum(sales)

# Step:3 Calculate the average sales
ans1 = ans / len(sales)

# Step:4 Output total and average sales
print(ans)
print(ans1)

# Step:5 Append a new sales entry
sales.append(1100)

# Step:6 Sort the sales data in ascending order
sales.sort()

# Step:7 Output the sorted sales list
print(sales)

# Step:8 Display the top 3 highest sales values
print("Highest Sales", sales[-3:])

# Step:9 Display the 2 lowest sales values
print("Lowest Sales", sales[:2])

# Step:10 Delete the lowest sales value (first element after sorting)
del sales[0]

# Step:11 Output the updated sales list
print(sales)



# ==============sample output=====================
# 8350
# 1391.6666666666667
# [800, 950, 1100, 1200, 1500, 1700, 2200]
# Highest Sales [1500, 1700, 2200]
# Lowest Sales [800, 950]
# [950, 1100, 1200, 1500, 1700, 2200]