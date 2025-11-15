# Online Order Fulfilment Report

# Assignment 3 — Online Order Fulfilment Report
# Scenario:
# UST’s e-commerce division tracks daily customer orders.
# Each order record has:
# Order ID
# Customer name
# City
# Product
# Quantity

# Management wants to:
# 1. Store the order data efficiently.
# 2. Prevent duplicate Order IDs.
# 3. Retrieve:
# Total quantity sold per product.
# Unique cities where products were sold.
# Customer(s) who placed the highest total quantity of orders.
# 4. Easily update when a new order is added.
# Sample Input:
# orders = [
#  ("O1001", "Neha", "Bangalore", "Laptop", 2),
#  ("O1002", "Arjun", "Chennai", "Mobile", 3),
#  ("O1003", "Ravi", "Delhi", "Laptop", 1),
#  ("O1004", "Fatima", "Bangalore", "Tablet", 2),
#  ("O1005", "Vikram", "Mumbai", "Mobile", 5),
#  ("O1006", "Neha", "Bangalore", "Laptop", 1)
# ]

# Sample orders data (order_id, customer_name, city, product, quantity)
orders = [
    ("O1001", "Bhargavi", "Bangalore", "Laptop", 2),
    ("O1002", "Meena", "Chennai", "Mobile", 3),
    ("O1003", "Swathi", "Delhi", "Laptop", 1),
    ("O1004", "Rakshi", "Bangalore", "Tablet", 2),
    ("O1005", "Shero", "Mumbai", "Mobile", 5),
    ("O1006", "Chinnu", "Bangalore", "Laptop", 1)
]

# Data structures for tracking
order_ids = set()       # ensures unique order IDs
product_qty = {}        # total quantity per product
customer_qty = {}       # total quantity per customer
cities = set()          # unique cities

# Step 1: Process existing orders
for oid, cust, city, prod, qty in orders:
    if oid in order_ids:        # skip duplicate orders
        continue
    order_ids.add(oid)
    product_qty[prod] = product_qty.get(prod, 0) + qty
    customer_qty[cust] = customer_qty.get(cust, 0) + qty
    cities.add(city)

# Step 2: Identify top customer(s) by quantity
max_qty = max(customer_qty.values())
top_customers = [c for c, q in customer_qty.items() if q == max_qty]

# Step 3: Print results
print("Total quantity per product:", product_qty)
print("Unique cities:", cities)
print("Top customer(s):", top_customers)

# Step 4: Add a new order and update records
new_order = ("O1007", "Meena", "Chennai", "Tablet", 4)
oid, cust, city, prod, qty = new_order
if oid not in order_ids:
    order_ids.add(oid)
    product_qty[prod] = product_qty.get(prod, 0) + qty
    customer_qty[cust] = customer_qty.get(cust, 0) + qty
    cities.add(city)

# Step 5: Print updated results
print("\nAfter adding new order:")
print("Products:", product_qty)
print("Customers:", customer_qty)


#ouput
# Total quantity per product: {'Laptop': 4, 'Mobile': 8, 'Tablet': 2}
# Unique cities: {'Chennai', 'Mumbai', 'Bangalore', 'Delhi'}
# Top customer(s): ['Shero']

# After adding new order:
# Products: {'Laptop': 4, 'Mobile': 8, 'Tablet': 6}
# Customers: {'Bhargavi': 2, 'Meena': 7, 'Swathi': 1, 'Rakshi': 2, 'Shero': 5, 'Chinnu': 1}