#Task 2: Product Sales Summary

# List of sales with product names and quantities sold
sales = [("Laptop", 3), ("Mobile", 5), ("Tablet", 2), ("Mobile", 4), ("Laptop", 1)]

# Dictionary to store the total quantity sold for each product
sales_summary = {}

# Iterating through the sales data to aggregate the total quantities for each product
for product, quantity in sales:
    # Use the `get()` method to get the current quantity (default 0 if not present) and add the new quantity
    sales_summary[product] = sales_summary.get(product, 0) + quantity

# Printing the total quantity sold for each product
for product, quantity in sales_summary.items():
    print(f"{product} → {quantity}")

# Finding the product with the highest sales (quantity) using the `max()` function
highest_sell_prod = max(sales_summary.items(), key=lambda x: x[1])

# Printing the product with the highest sales quantity
print(f"Highest selling product is: {highest_sell_prod[0]} and {highest_sell_prod[1]} quantity")


#Sample Execution
# Laptop→4
# Mobile→9
# Tablet→2
# Highest selling product is: Mobile and 9 quantity