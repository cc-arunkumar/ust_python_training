# Assignment 3 — Online Order Fulfilment Report
# Scenario:
# UST’s e-commerce division tracks daily customer orders.
# Each order record has: Order ID, Customer Name, City, Product, Quantity.
# Requirements:
# 1. Store order data efficiently and prevent duplicate Order IDs.
# 2. Retrieve:
#    - Total quantity sold per product.
#    - Unique cities where products were sold.
#    - Customer(s) who placed the highest total quantity of orders.
# 3. Allow adding new orders dynamically and update the report.

orders = [
    ("O1001", "Neha", "Bangalore", "Laptop", 2),
    ("O1002", "Arjun", "Chennai", "Mobile", 3),
    ("O1003", "Ravi", "Delhi", "Laptop", 1),
    ("O1004", "Fatima", "Bangalore", "Tablet", 2),
    ("O1005", "Vikram", "Mumbai", "Mobile", 5),
    ("O1006", "Neha", "Bangalore", "Laptop", 1)
]

# Store data efficiently & prevent duplicate Order IDs
order_ids = set()
product_sales = {}
customer_orders = {}
cities = set()

for oid, cust, city, prod, qty in orders:
    if oid not in order_ids:
        order_ids.add(oid)
        product_sales[prod] = product_sales.get(prod, 0) + qty
        customer_orders[cust] = customer_orders.get(cust, 0) + qty
        cities.add(city)

# Customer(s) with maximum total order quantity
max_qty = max(customer_orders.values())
top_customers = [c for c, q in customer_orders.items() if q == max_qty]

# Function to add new order dynamically
def add_order(oid, cust, city, prod, qty):
    if oid in order_ids:
        print("Duplicate Order ID! Not added.")
    else:
        order_ids.add(oid)
        product_sales[prod] = product_sales.get(prod, 0) + qty
        customer_orders[cust] = customer_orders.get(cust, 0) + qty
        cities.add(city)

# Example: Add a new order
add_order("O1007", "Arjun", "Chennai", "Laptop", 2)

# Print results
print("Total quantity sold per product:", product_sales)
print("Unique cities:", cities)
print("Customer(s) with highest total quantity:", top_customers)


# Sample Output:
# Total quantity sold per product: {'Laptop': 5, 'Mobile': 8, 'Tablet': 2}
# Unique cities: {'Delhi', 'Mumbai', 'Bangalore', 'Chennai'}
# Customer(s) with highest total quantity: ['Vikram']