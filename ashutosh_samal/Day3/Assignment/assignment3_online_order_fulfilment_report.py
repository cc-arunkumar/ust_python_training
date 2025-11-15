#Assignment 3 — Online Order Fulfilment Report

# List of orders, each containing order ID, customer name, city, product, and quantity
orders = [
    ("O1001", "Neha", "Bangalore", "Laptop", 2),
    ("O1002", "Arjun", "Chennai", "Mobile", 3),
    ("O1003", "Ravi", "Delhi", "Laptop", 1),
    ("O1004", "Fatima", "Bangalore", "Tablet", 2),
    ("O1005", "Vikram", "Mumbai", "Mobile", 5),
    ("O1006", "Neha", "Bangalore", "Laptop", 1)
]

# Dictionary to store the order summary by order ID
order = {}

# Set to store unique cities
set_unique_cities = set()

# List to store all customer names
name_list = []

# Processing each order
for order_id, name, cities, prod, quantity in orders:
    # Adding the customer's name to the name list
    name_list.append(name)

    # If the city is not in the set of unique cities, add it
    if cities not in set_unique_cities:
        set_unique_cities.add(cities)
    
    # If the order ID is not in the dictionary, add it
    if order_id not in order:
        order[order_id] = {name, cities, prod, quantity}

# Printing the order summary
print("The order summary: ", order)

# Initializing quantities for each product type
q_laptop = 0
q_mobile = 0
q_tablet = 0

# Calculating the total quantity sold per product
print("Total Quantity sold per product")
for order_id, name, cities, prod, quantity in orders:
    if prod == "Laptop":
        q_laptop += quantity
    elif prod == "Mobile":
        q_mobile += quantity
    elif prod == "Tablet":
        q_tablet += quantity

# Printing the total quantities sold per product
print("Laptop----->", q_laptop)
print("Mobile----->", q_mobile)
print("Tablet----->", q_tablet)

# Printing the set of unique cities
print("Set of unique cities: ", set_unique_cities)

# Finding the customer with the maximum orders
customer_order_count = {}
for name in name_list:
    customer_order_count[name] = customer_order_count.get(name, 0) + 1

# Finding the name of the customer with the maximum orders
max_orders = max(customer_order_count.values())
for name, count in customer_order_count.items():
    if count == max_orders:
        print("Customer with maximum orders: ", name)
        break

#Sample Executions
# The order summary:  {'O1001': {'Laptop', 2, 'Bangalore', 'Neha'}, 'O1002': {3, 'Mobile', 'Chennai', 'Arjun'}, 'O1003': {'Ravi', 'Laptop', 'Delhi', 1}, 'O1004': {2, 'Fatima', 'Tablet', 'Bangalore'}, 'O1005': {'Mobile', 5, 'Vikram', 'Mumbai'}, 'O1006': {'Laptop', 'Bangalore', 'Neha', 1}}
# Total Quantity sold per product
# Laptop-----> 4
# Mobile-----> 8
# Tablet-----> 2
# Set of unique cities:  {'Delhi', 'Bangalore', 'Chennai', 'Mumbai'}
# Customer with maximum orders  Neha
