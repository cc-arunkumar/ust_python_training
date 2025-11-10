# #Assignment 3 — Online Order Fulfilment Report
# Scenario:
# UST’s e-commerce division tracks daily customer orders.
# Each order record has:
# Order ID
# Customer name
# City
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
orders = [
 ("O1001", "Neha", "Bangalore", "Laptop", 2),
 ("O1002", "Arjun", "Chennai", "Mobile", 3),
 ("O1003", "Ravi", "Delhi", "Laptop", 1),
 ("O1004", "Fatima", "Bangalore", "Tablet", 2),
 ("O1005", "Vikram", "Mumbai", "Mobile", 5),
 ("O1006", "Neha", "Bangalore", "Laptop", 1)
]


unique_orders = {}
product_totals = {}
customer_totals = {}
unique_cities = set()

for order_id,customer,city,product,quantity in orders:
    if order_id not in unique_orders:
        unique_orders[order_id]=(customer,city,product,quantity)
        product_totals[product]=product_totals.get(product,0)+quantity
        customer_totals[customer]=customer_totals.get(customer,0)+quantity
        unique_cities.add(city)

print("Total quantity ordered for each product:")
for product, total in product_totals.items():
    print(f"{product}: {total}")

print("Unique cities : ",unique_cities)

max=0
name=""
for(customer, total) in customer_totals.items():
    if total>max:
        max=total
        name=customer
print("Customer with highest order quantity: ",name)

order_id=input("Enter Order ID: ")
customer=input("Enter Customer Name: ")
city=input("Enter City: ")
product=input("Enter Product Name: ")
quantity=int(input("Enter Quantity: "))

if order_id not in unique_orders:
    unique_orders[order_id]=(customer,city,product,quantity)
    product_totals[product]=product_totals.get(product,0)+quantity
    customer_totals[customer]=customer_totals.get(customer,0)+quantity
    unique_cities.add(city)
    print("Order added successfully.")

#Sample output
# Total quantity ordered for each product:
# Laptop: 4
# Mobile: 8
# Tablet: 2
# Unique cities :  {'Delhi', 'Chennai', 'Bangalore', 'Mumbai'}
# Customer with highest order quantity:  Vikram
# Enter Order ID: 01007
# Enter Customer Name: shyam
# Enter City: Hyderabad
# Enter Product Name: Mobile
# Enter Quantity: 5
# Order added successfully.