# Assignment 3 — Online Order Fulfilment Report

orders = [
    ("O1001", "Neha", "Bangalore", "Laptop", 2),
    ("O1002", "Arjun", "Chennai", "Mobile", 3),
    ("O1003", "Ravi", "Delhi", "Laptop", 1),
    ("O1004", "Fatima", "Bangalore", "Tablet", 2),
    ("O1005", "Vikram", "Mumbai", "Mobile", 5),
    ("O1006", "Neha", "Bangalore", "Laptop", 1)
]
order_ids = set()
product_quantity = {}
cities = set()
customer_quantity = {}
for oid, customer, city, product, qty in orders:
    if oid in order_ids:
        continue
    order_ids.add(oid)
    cities.add(city)
    if product not in product_quantity:
        product_quantity[product] = 0
    product_quantity[product] += qty
    if customer not in customer_quantity:
        customer_quantity[customer] = 0
    customer_quantity[customer] += qty
max_qty = max(customer_quantity.values())
top_customers = []
for cust, qty in customer_quantity.items():
    if qty == max_qty:
        top_customers.append(cust)
print("Total quantity sold per product:", product_quantity)
print("Unique cities:", cities)
print("Customer(s) with highest total quantity:", top_customers)
new_order = ("O1007", "Ravi", "Delhi", "Tablet", 3)
oid, customer, city, product, qty = new_order
if oid not in order_ids:
    order_ids.add(oid)
    cities.add(city)
    if product not in product_quantity:
        product_quantity[product] = 0
    product_quantity[product] += qty
    if customer not in customer_quantity:
        customer_quantity[customer] = 0
    customer_quantity[customer] += qty
max_qty = max(customer_quantity.values())
top_customers = []
for cust, qty in customer_quantity.items():
    if qty == max_qty:
        top_customers.append(cust)
print("\nAfter adding new order:")
print("Total quantity sold per product:", product_quantity)
print("Unique cities:", cities)
print("Customer(s) with highest total quantity:", top_customers)

#sample output

# Total quantity sold per product: {'Laptop': 4, 'Mobile': 8, 'Tablet': 2}
# Unique cities: {'Bangalore', 'Chennai', 'Delhi', 'Mumbai'}
# Customer(s) with highest total quantity: ['Vikram']

# After adding new order:
# Total quantity sold per product: {'Laptop': 4, 'Mobile': 8, 'Tablet': 5}
# Unique cities: {'Bangalore', 'Chennai', 'Delhi', 'Mumbai'}
# Customer(s) with highest total quantity: ['Vikram']