# Assignment 2 — Corporate Skill Matrix System
# Scenario:
# UST’s L&D team wants to maintain a skill matrix for all employees.
# Every employee can have multiple skills at different proficiency levels.
# For example:
# Arjun → Python (Advanced), SQL (Intermediate)
# Neha → Excel (Expert), PowerBI (Advanced)
# They want to:
# 1. Store skill information efficiently.
# 2. Ensure no duplicate skill names for the same employee.
# 3. Retrieve:
# All employees who know a given skill (e.g., “Python”).
# All unique skills across the company.
# Assignment 2
# Employees having 3 or more skills.
# 4. Be able to add or update new skills dynamically.

#Code

# List of orders: each tuple contains
# (Order ID, Customer Name, City, Product, Quantity)
orders = [
    ("O1001", "Neha", "Bangalore", "Laptop", 2),
    ("O1002", "Arjun", "Chennai", "Mobile", 3),
    ("O1003", "Ravi", "Delhi", "Laptop", 1),
    ("O1004", "Fatima", "Bangalore", "Tablet", 2),
    ("O1005", "Vikram", "Mumbai", "Mobile", 5),
    ("O1006", "Neha", "Bangalore", "Laptop", 1)
]

# Initialize data structures
order_ids = set()          # To track unique order IDs (avoid duplicates)
product_quantity = {}      # To store total quantity sold per product
cities = set()             # To store unique cities
customer_quantity = {}     # To store total quantity purchased per customer

# Process each order
for oid, customer, city, product, qty in orders:
    # Skip duplicate order IDs
    if oid in order_ids:
        continue
    
    # Add order ID to the set
    order_ids.add(oid)
    
    # Add city to the set of unique cities
    cities.add(city)
    
    # Update product quantity
    if product not in product_quantity:
        product_quantity[product] = 0
    product_quantity[product] += qty
    
    # Update customer quantity
    if customer not in customer_quantity:
        customer_quantity[customer] = 0
    customer_quantity[customer] += qty

# Find the maximum quantity purchased by any customer
max_qty = max(customer_quantity.values())

# Identify customer(s) with the highest total quantity
top_customers = []
for cust, qty in customer_quantity.items():
    if qty == max_qty:
        top_customers.append(cust)

# Print results
print("Total quantity sold per product:", product_quantity)
print("Unique cities:", cities)
print("Customer(s) with highest total quantity:", top_customers)

# Add a new order
new_order = ("O1007", "Ravi", "Delhi", "Tablet", 3)
oid, customer, city, product, qty = new_order

# Process the new order if not duplicate
if oid not in order_ids:
    order_ids.add(oid)
    cities.add(city)
    
    # Update product quantity
    if product not in product_quantity:
        product_quantity[product] = 0
    product_quantity[product] += qty
    
    # Update customer quantity
    if customer not in customer_quantity:
        customer_quantity[customer] = 0
    customer_quantity[customer] += qty

# Recalculate top customers after new order
max_qty = max(customer_quantity.values())
top_customers = []
for cust, qty in customer_quantity.items():
    if qty == max_qty:
        top_customers.append(cust)

# Print updated results
print("\nAfter adding new order:")
print("Total quantity sold per product:", product_quantity)
print("Unique cities:", cities)
print("Customer(s) with highest total quantity:", top_customers)

#output
# g/Ass3_OnlineOrder_Fulfilment_Report.py
# Total quantity sold per product: {'Laptop': 4, 'Mobile': 8, 'Tablet': 2}
# Unique cities: {'Delhi', 'Chennai', 'Bangalore', 'Mumbai'}
# Customer(s) with highest total quantity: ['Vikram']

# After adding new order:
# Total quantity sold per product: {'Laptop': 4, 'Mobile': 8, 'Tablet': 5}
# Unique cities: {'Delhi', 'Chennai', 'Bangalore', 'Mumbai'}
# Customer(s) with highest total quantity: ['Vikram']
# PS C:\Users\303379\day3_training> 