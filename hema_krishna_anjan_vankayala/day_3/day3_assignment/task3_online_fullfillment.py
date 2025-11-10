#Assignment 3 — Online Order Fulfilment Report

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

product_set = {}
cities_set=set()
for order in orders:
    cities_set.add(order[2])
    if order[3] not in product_set:
        product_set[order[3]] = order[4]
    else:
        product_set[order[3]] = order[4] + product_set.get(order[3])

print("Total Quantity Sold per Product:",product_set)

print("Unique Cities:",cities_set)

customer_set = {}
for order in orders:
    if order[1] not in customer_set.keys():
        customer_set[order[1]] = order[4]
    else:
        customer_set[order[1]] = order[4]+ customer_set.get(order[1])
        
print("Customer with Highest Total Quantity of orders:",max(customer_set,key=customer_set.get))

#Sample Output
# Total Quantity Sold per Product: {'Laptop': 4, 'Mobile': 8, 'Tablet': 2}
# Unique Cities: {'Mumbai', 'Chennai', 'Bangalore', 'Delhi'}
# Customer with Highest Total Quantity of orders: Vikram