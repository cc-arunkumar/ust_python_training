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
#   1. Store the order data efficiently.
#   2. Prevent duplicate Order IDs.
#   3. Retrieve:
# Total quantity sold per product.
# Unique cities where products were sold.
# Customer(s) who placed the highest total quantity of orders.
# 4. Easily update when a new order is added.





# Step 1: Sample order data
orders = [
    ("O1001", "Neha", "Bangalore", "Laptop", 2),
    ("O1002", "Arjun", "Chennai", "Mobile", 3),
    ("O1003", "Ravi", "Delhi", "Laptop", 1),
    ("O1004", "Fatima", "Bangalore", "Tablet", 2),
    ("O1005", "Vikram", "Mumbai", "Mobile", 5),
    ("O1006", "Neha", "Bangalore", "Laptop", 1)
]

# Step 2: Initialize data structures
order_records = {}      # Stores unique orders by ID
product_totals = {}     # Tracks total quantity sold per product
customer_totals = {}    # Tracks total quantity ordered per customer
unique_cities = set()   # Tracks all cities where orders were placed

# Step 3: Process initial orders
for order_id, customer, city, product, quantity in orders:
    if order_id in order_records:
        continue  # Skip duplicate order IDs
    order_records[order_id] = (customer, city, product, quantity)

    # Update product quantity
    product_totals[product] = product_totals.get(product, 0) + quantity

    # Update customer order quantity
    customer_totals[customer] = customer_totals.get(customer, 0) + quantity

    # Add city to unique set
    unique_cities.add(city)

# Step 4: Function to add new orders dynamically
def add_order(order_id, customer, city, product, quantity):
    if order_id in order_records:
        print(f"Order ID {order_id} already exists. Skipping.")
        return

    order_records[order_id] = (customer, city, product, quantity)
    product_totals[product] = product_totals.get(product, 0) + quantity
    customer_totals[customer] = customer_totals.get(customer, 0) + quantity
    unique_cities.add(city)

# Step 5: Add a new order
add_order("O1007", "Neha", "Bangalore", "Tablet", 3)

# Step 6: Report total quantity sold per product
print(" Total quantity sold per product:")
for product, total in product_totals.items():
    print(f"{product}: {total}")

# Step 7: Report unique cities
print("\n Unique cities where products were sold:")
print(unique_cities)

# Step 8: Identify top customer(s) by total quantity
max_quantity = max(customer_totals.values())
top_customers = [cust for cust, qty in customer_totals.items() if qty == max_quantity]
print("\n Customer(s) with highest total order quantity:")
print(top_customers)

# =========sample output==================
# Total quantity sold per product:
# Laptop: 4
# Mobile: 8
# Tablet: 5

#  Unique cities where products were sold:
# {'Delhi', 'Mumbai', 'Chennai', 'Bangalore'}

#  Customer(s) with highest total order quantity:
# ['Neha']