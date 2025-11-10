# Assignment 3 — Online Order Fulfilment Report
# UST’s e-commerce division tracks daily customer orders

orders_list = [
    ("O1001", "Neha", "Bangalore", "Laptop", 2),
    ("O1002", "Arjun", "Chennai", "Mobile", 3),
    ("O1003", "Ravi", "Delhi", "Laptop", 1),
    ("O1004", "Fatima", "Bangalore", "Tablet", 2),
    ("O1005", "Vikram", "Mumbai", "Mobile", 5),
    ("O1006", "Neha", "Bangalore", "Laptop", 1)
]

order_ids = set()         
product_totals = {}       
cities = set()            
customer_totals = {}      

for order_id, customer, city, product, qty in orders_list:
    if order_id in order_ids:
        continue
    order_ids.add(order_id)

    if product not in product_totals:
        product_totals[product] = 0
    product_totals[product] += qty

    cities.add(city)

    if customer not in customer_totals:
        customer_totals[customer] = 0
    customer_totals[customer] += qty

def add_order(order_id, customer, city, product, qty):
    if order_id in order_ids:
        print("Order ID already exists")
        return

    order_ids.add(order_id)
    orders_list.append((order_id, customer, city, product, qty))

    if product not in product_totals:
        product_totals[product] = 0
    product_totals[product] += qty

    cities.add(city)

    if customer not in customer_totals:
        customer_totals[customer] = 0
    customer_totals[customer] += qty

def print_report():
    print("\nTotal Quantity Sold per Product:")
    for product, total in product_totals.items():
        print(" -", product, ":", total)
    print("\nUnique Cities Where Products Were Sold:")
    for city in sorted(cities):
        print(" -", city)
    max_qty = max(customer_totals.values())
    print("\nCustomer with Maximum Total Quantity Ordered:")
    for customer, total in customer_totals.items():
        if total == max_qty:
            print(" -", customer, ":", total)

add_order("O1007", "Arjun", "Chennai", "Laptop", 2)  
print_report()


#Sample output

# Total Quantity Sold per Product:
#  - Laptop : 6
#  - Mobile : 8
#  - Tablet : 2

# Unique Cities Where Products Were Sold:
#  - Bangalore
#  - Chennai
#  - Delhi
#  - Mumbai

# Customer with Maximum Total Quantity Ordered:
#  - Arjun : 5
#  - Vikram : 5