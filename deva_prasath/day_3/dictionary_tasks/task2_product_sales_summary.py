# product_sales_summary
# You work in the Sales Analytics team.
# You receive a list of daily sales transactions — each as a tuple: (product, quantity) .

# List of sales data with product and quantity sold
sales = [
    ("Laptop", 3),
    ("Mobile", 5),
    ("Tablet", 2),
    ("Mobile", 4),
    ("Laptop", 1)
]

# Initialize dictionary to store total sales for each product
sales_summary = {}

# Summing up quantities sold for each product
for product, qty in sales:
    sales_summary[product] = sales_summary.get(product, 0) + qty

# Print the sales summary (product-wise total sales)
print(sales_summary)

# Iterate through sales summary and print each product and its total quantity sold
for key, value in sales_summary.items():
    print(f"{key} --> {value}")

# Find the product with the highest quantity sold
max_key = None
max_value = float('-inf')
for key, value in sales_summary.items():
    if value > max_value:
        max_value = value
        max_key = key

# Print the highest selling product
print("Highest Selling product name: ", max_key)


#Sample output

# {'Laptop': 4, 'Mobile': 9, 'Tablet': 2}
# Laptop-->4
# Mobile-->9
# Tablet-->2
# Highest Selling product name:  Mobile