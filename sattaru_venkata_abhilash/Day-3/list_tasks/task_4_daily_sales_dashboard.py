# Task 4: Daily Sales Dashboard
# Scenario:
# You work on a Sales Dashboard that tracks the daily sales revenue of your company’s products.

# Step 1: Create a list of daily sales
sales = [1200, 1500, 800, 2200, 1700, 950]

# Step 2: Calculate total and average sales
total = sum(sales)
print("Total Sales:", total)

average = total / len(sales)
print(f"Average Sale: {average:.2f}")

# Step 3: Add a new late entry sale
sales.append(1100)

# Step 4: Sort sales in ascending order
sales.sort()
print("Sorted Sales:", sales)

# Step 5: Display top 3 and lowest 2 sales
print("Top 3 Sales:", sales[-3:])
print("Lowest 2 Sales:", sales[:2])

# Step 6: Remove the smallest sale and display updated list
sales.pop(0)
print("Updated Sales after removing smallest:", sales)


# Sample Output:
# Total Sales: 8350
# Average Sale: 1391.67
# Sorted Sales: [800, 950, 1100, 1200, 1500, 1700, 2200]
# Top 3 Sales: [1500, 1700, 2200]
# Lowest 2 Sales: [800, 950]
# Updated Sales after removing smallest: [950, 1100, 1200, 1500, 1700, 2200]
