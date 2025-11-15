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
# Your Task:
# 1. Design the proper data structures to store this order data and prevent
# duplicates.
# 2. Generate:
# Total quantity sold per product.
# Set of unique cities.
# Customer(s) with maximum total order quantity.
# 3. Add a new order dynamically and update your report.


# Sample order data: (Order ID, Customer Name, City, Product, Quantity)
orders = [
    ("01001", "Neha", "Bangalore", "Laptop", 2),
    ("01002", "Arjun", "Chennai", "Mobile", 3),
    ("01003", "Ravi", "Delhi", "Laptop", 1),
    ("01004", "Fatima", "Bangalore", "Tablet", 2),
    ("01005", "Vikram", "Mumbai", "Mobile", 5),
    ("01006", "Neha", "Bangalore", "Laptop", 1)
]

order_data = {}

# Process orders to ensure unique Order IDs
for oid, cname, city, product, qty in orders:
    if oid not in order_data:
        order_data[oid] = (cname, city, product, qty)


product_qty = {}
# Calculate total quantity per product
for  cname, city, prod, qty in order_data.values():
    product_qty[prod] = product_qty.get(prod, 0) + qty

cities = set()
# Identify unique cities from orders
for cname in order_data.values():
    cities.add(cname)

customer_qty = {}
# Calculate total quantity ordered per customer
for cname, city, prod, qty in order_data.values():
    customer_qty[cname] = customer_qty.get(cname, 0) + qty

max_qty = 0
# Find the maximum quantity ordered by any customer
for  qty in customer_qty.values():
    if qty > max_qty:
        max_qty = qty

top_customers = []
# Identify customer(s) with the highest quantity ordered
for cname,  qty in customer_qty.items():
    if qty == max_qty:
        top_customers.append(cname)

# Function to add a new order ensuring unique Order ID
def add_order(oid, cname, city, product, qty):
    if oid not in order_data:
        order_data[oid] = (cname, city, product, qty)
        print("Order added:", oid)
    else:
        print("Duplicate Order ID")

add_order("01007", "Meena", "Pune", "Mobile", 4)

print("\nTotal Quantity per Product:", product_qty)
print("Unique Cities:", cities)
print("Top Customer(s):", top_customers)


# Order added: 01007

# Total Quantity per Product: {'Laptop': 4, 'Mobile': 8, 'Tablet': 2}
# Unique Cities: {('Fatima', 'Bangalore', 'Tablet', 2), ('Neha', 'Bangalore', 'Laptop', 2), ('Ravi', 'Delhi', 'Laptop', 1), ('Neha', 'Bangalore', 'Laptop', 1), ('Vikram', 'Mumbai', 'Mobile', 5), ('Arjun', 'Chennai', 'Mobile', 3)}
# Top Customer(s): ['Vikram']