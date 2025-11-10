# Assignment 3 — Online Order Fulfilment Report
# Scenario:
# UST’s e-commerce division tracks daily customer orders.
# Each order record has:
# Order ID
# Customer name
# City
# Assignment 3
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
# Customer(s) with maximum total order quantity.
# Assignment 4
# 3. Add a new order dynamically and update your report.

orders = [
 ("O1001", "Neha", "Bangalore", "Laptop", 2),
 ("O1002", "Arjun", "Chennai", "Mobile", 3),
 ("O1003", "Ravi", "Delhi", "Laptop", 1),
 ("O1004", "Fatima", "Bangalore", "Tablet", 2),
 ("O1005", "Vikram", "Mumbai", "Mobile", 5),
 ("O1006", "Neha", "Bangalore", "Laptop", 1)
]

unique_orders=[]
seen =set()
product_quantity={}
cities_set=set()
customer_totals={}
for order_id,name,city,product,count in orders:
    key=(name,city,product)
    if key not in seen:
        seen.add(key)
        unique_orders.append((order_id,name,city,product,count))
    
    cities_set.add(city)

   
for order_id,name,city,product,count in unique_orders:
    product_quantity[product]=product_quantity.get(product,0)+count

    customer_totals[name] = customer_totals.get(name, 0) + count

new_order=["O1007", "jana", "Bangalore", "Mobile", 1]
order_id,name,city,product,count = new_order

if order_id not in unique_orders:
    unique_orders.append(new_order)
    product_quantity[product]=product_quantity.get(product,0)+count
    customer_totals[name]=customer_totals.get(name,0)+count



print(unique_orders)
print(product_quantity)
print(customer_totals)

# EXPECTED OUTPUT:
# [('O1001', 'Neha', 'Bangalore', 'Laptop', 2), ('O1002', 'Arjun', 'Chennai', 'Mobile', 3), ('O1003', 'Ravi', 'Delhi', 'Laptop', 1), ('O1004', 'Fatima', 'Bangalore', 'Tablet', 2), ('O1005', 'Vikram', 'Mumbai', 'Mobile', 5), ['O1007', 'jana', 'Bangalore', 'Mobile', 1]]
# {'Laptop': 3, 'Mobile': 9, 'Tablet': 2}
# {'Neha': 2, 'Arjun': 3, 'Ravi': 1, 'Fatima': 2, 'Vikram': 5, 'jana': 1}