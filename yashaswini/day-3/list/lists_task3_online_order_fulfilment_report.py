# online Order Fulfilment Report
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
# 4. Easily update when a new order is added


orders = [
    ("O2001", "Deepak", "Delhi", "Laptop", 3),
    ("O2002", "Varsha", "Mumbai", "Mobile", 2),
    ("O2003", "Yashu", "Bangalore", "Laptop", 1),
    ("O2004", "Tej", "Chennai", "Tablet", 4),
    ("O2005", "Arjun", "Delhi", "Mobile", 2),
    ("O2006", "Aadya", "Mumbai", "Laptop", 2)
]
order_ids = set()
order_list = []
for order in orders:
    order_id = order[0]
    if order_id not in order_ids:
        order_ids.add(order_id)
        order_list.append(order)
product_totals = {}
city_set = set()
customer_totals = {}
for order_id, customer, city, product, qty in order_list:
    product_totals[product] = product_totals.get(product, 0) + qty
    city_set.add(city)
    customer_totals[customer] = customer_totals.get(customer, 0) + qty
max_qty = max(customer_totals.values())
top_customers = [cust for cust, total in customer_totals.items() if total == max_qty]
print("Total quantity per product:", product_totals)
print("Unique cities:", city_set)
print("Customer(s) with maximum total orders:", top_customers)
new_order = ("O2007", "Rohit", "Bangalore", "Tablet", 3)
order_id, customer, city, product, qty = new_order
if order_id not in order_ids:
    order_ids.add(order_id)
    order_list.append(new_order)
    product_totals[product] = product_totals.get(product, 0) + qty
    city_set.add(city)
    customer_totals[customer] = customer_totals.get(customer, 0) + qty
max_qty = max(customer_totals.values())
top_customers = [cust for cust, total in customer_totals.items() if total == max_qty]
print("After adding new order:")
print("Total quantity per product:", product_totals)
print("Unique cities:", city_set)
print("Customer(s) with maximum total orders:", top_customers)


#o/p:
# Total quantity per product: {'Laptop': 6, 'Mobile': 4, 'Tablet': 4}
# Unique cities: {'Bangalore', 'Mumbai', 'Delhi', 'Chennai'}
# Customer(s) with maximum total orders: ['Tej']
# After adding new order:
# Total quantity per product: {'Laptop': 6, 'Mobile': 4, 'Tablet': 7}
# Unique cities: {'Bangalore', 'Mumbai', 'Delhi', 'Chennai'}
# Customer(s) with maximum total orders: ['Tej']