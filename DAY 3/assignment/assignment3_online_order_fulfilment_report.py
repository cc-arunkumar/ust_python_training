# Assignment 3 — Online Order Fulfilment Report

"""
Scenario:
UST’s e-commerce division tracks daily customer orders.
Each order record has:
Order ID
Customer name
City
Assignment 3
Product
Quantity
Management wants to:
1. Store the order data efficiently.
2. Prevent duplicate Order IDs.
3. Retrieve:
Total quantity sold per product.
Unique cities where products were sold.
Customer(s) who placed the highest total quantity of orders.
4. Easily update when a new order is added.

"""

# List of orders (Order ID, Customer, City, Product, Quantity)
orders=[
("O1001","Neha","Bangalore","Laptop",2),
("O1002","Arjun","Chennai","Mobile",3),
("O1003","Ravi","Delhi","Laptop",1),
("O1004","Fatima","Bangalore","Tablet",2),
("O1005","Vikram","Mumbai","Mobile",5),
("O1006","Neha","Bangalore","Laptop",1)
]

# Set to track unique order IDs
order_ids=set()

# Dictionary to store total quantity sold per product
product_qty={}

# Dictionary to store total quantity ordered per customer
customer_total={}

# Set to store unique cities
cities=set()

# Process each order
for oid,cust,city,prod,qty in orders:
    # Only process if order ID is unique
    if oid not in order_ids:
        order_ids.add(oid)
        # Update product quantity
        product_qty[prod]=product_qty.get(prod,0)+qty
        # Update total orders per customer
        customer_total[cust]=customer_total.get(cust,0)+qty
        # Add city to unique cities
        cities.add(city)

# Print total quantity sold per product
print("Total Quantity per Product:",product_qty)

# Print unique cities where orders were placed
print("Unique Cities:",cities)

# Find the maximum total quantity ordered by any customer
max_qty=max(customer_total.values())

# Identify customer(s) with highest total quantity
top_customers=[c for c,q in customer_total.items() if q==max_qty]
print("Top Customers:",top_customers)

# Adding a new order
new_order=("O1007","Fatima","Delhi","Tablet",3)
oid,cust,city,prod,qty=new_order

# Process the new order only if order ID is unique
if oid not in order_ids:
    order_ids.add(oid)
    product_qty[prod]=product_qty.get(prod,0)+qty
    customer_total[cust]=customer_total.get(cust,0)+qty
    cities.add(city)

# Print updated product totals
print("Updated Product Totals:",product_qty)

# Print updated top customers based on total quantity
print("Updated Top Customers:",[c for c,q in customer_total.items() if q==max(customer_total.values())])


# sample output

"""
Total Quantity per Product: {'Laptop': 4, 'Mobile': 8, 'Tablet': 2}
Unique Cities: {'Mumbai', 'Delhi', 'Chennai', 'Bangalore'}
Top Customers: ['Vikram']
Updated Product Totals: {'Laptop': 4, 'Mobile': 8, 'Tablet': 5}
Updated Top Customers: ['Fatima', 'Vikram']
"""
