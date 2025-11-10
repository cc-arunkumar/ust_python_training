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
# Your Task:
# 1. Design the proper data structures to store this order data and prevent
# duplicates.
# 2. Generate:
# Total quantity sold per product.
# Set of unique cities.
# Customer(s) with maximum total order quantit
# 3. Add a new order dynamically and update your report.

orders = [
 ("O1001", "Neha", "Bangalore", "Laptop", 2),
 ("O1002", "Arjun", "Chennai", "Mobile", 3),
 ("O1003", "Ravi", "Delhi", "Laptop", 1),
 ("O1004", "Fatima", "Bangalore", "Tablet", 2),
 ("O1005", "Vikram", "Mumbai", "Mobile", 5),
 ("O1006", "Neha", "Bangalore", "Laptop", 1)
]

order_ids = set()
product_qty = {}
customer_qty = {}
cities = set()

for o_id, cust, city, prod, qty in orders:
    if o_id in order_ids:
        continue
    order_ids.add(o_id)
    product_qty[prod] = product_qty.get(prod, 0) + qty
    customer_qty[cust] = customer_qty.get(cust, 0) + qty
    cities.add(city)

max_qty = max(customer_qty.values())
top_customers = [customer for customer, quantity in customer_qty.items() if quantity == max_qty]

print("Total quantity per product:", product_qty)
print("Unique cities:", cities)
print("Top customers:", top_customers)


new_order = ("O1007", "Ravi", "Chennai", "Mobile", 3)
o_id, cust, city, prod, qty = new_order
if o_id not in order_ids:
    order_ids.add(o_id)
    product_qty[prod] = product_qty.get(prod, 0) + qty
    customer_qty[cust] = customer_qty.get(cust, 0) + qty
    cities.add(city)

print("After adding new order:")
print("Products:", product_qty)
print("Customers:", customer_qty)

# output
# Total quantity per product: {'Laptop': 4, 'Mobile': 8, 'Tablet': 2}
# Unique cities: {'Mumbai', 'Bangalore', 'Delhi', 'Chennai'}
# Top customers: ['Vikram']
# After adding new order:
# Products: {'Laptop': 4, 'Mobile': 11, 'Tablet': 2}
# Customers: {'Neha': 3, 'Arjun': 3, 'Ravi': 4, 'Fatima': 2, 'Vikram': 5}