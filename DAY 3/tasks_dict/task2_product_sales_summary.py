"""
Task 2: Product Sales Summary

Scenario:
You work in the Sales Analytics team.
You receive a list of daily sales transactions — each as a tuple: (product, quantity) .

"""

# List of sales transactions (Product, Quantity)
sales=[
("Laptop",3),
("Mobile",5),
("Tablet",2),
("Mobile",4),
("Laptop",1)
]

# Dictionary to store total quantity sold per product
sales_summary={}

# Variables to track highest selling product
high_selling_key=0
high_selling_value=""

# Aggregate sales quantities per product
for key,value in sales:
    if key in sales_summary:
        sales_summary[key]+=value  # Add to existing quantity
    else:
        sales_summary[key]=value   # Initialize quantity for new product

# Print summary and identify highest selling product
for product,quantity in sales_summary.items():
    print(f"{product} → {quantity}")
    if quantity>high_selling_key:
        high_selling_key=quantity       # Update highest quantity
        high_selling_value=product     # Update highest selling product name

# Print the highest selling product
print(f"Highest Selling Product {high_selling_value}")


# sample output

"""
Laptop → 4
Mobile → 9
Tablet → 2
Highest Selling Product Mobile

"""
