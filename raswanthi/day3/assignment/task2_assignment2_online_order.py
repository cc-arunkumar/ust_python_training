#Online Order
orders_list = [
    ("O1001", "Neha", "Bangalore", "Laptop", 2),
    ("O1002", "Arjun", "Chennai", "Mobile", 3),
    ("O1003", "Ravi", "Delhi", "Laptop", 1),
    ("O1004", "Fatima", "Bangalore", "Tablet", 2),
    ("O1005", "Vikram", "Mumbai", "Mobile", 5),
    ("O1006", "Neha", "Bangalore", "Laptop", 1)
]


orders_dict = {}
for order in orders_list:
    order_id = order[0]
    if order_id not in orders_dict:
        orders_dict[order_id] = order

def generate_reports():
    product_totals = {}
    city_set = []
    customer_totals = {}

    for order_id in orders_dict:
        order = orders_dict[order_id]
        customer = order[1]
        city = order[2]
        product = order[3]
        quantity = order[4]

        if product in product_totals:
            product_totals[product] += quantity
        else:
            product_totals[product] = quantity
        if city not in city_set:
            city_set.append(city)

        if customer in customer_totals:
            customer_totals[customer] += quantity
        else:
            customer_totals[customer] = quantity

    max_qty = 0
    top_customers = []
    for customer in customer_totals:
        qty = customer_totals[customer]
        if qty > max_qty:
            max_qty = qty
            top_customers = [customer]
        elif qty == max_qty:
            top_customers.append(customer)

    
    print("\nTotal quantity sold per product:")
    for product in product_totals:
        print(product, ":", product_totals[product])

    print("\nUnique cities where products were sold:")
    print(city_set)

    print("\nCustomer(s) with highest total order quantity:")
    print(top_customers)

def add_order(order):
    order_id = order[0]
    if order_id in orders_dict:
        print("Order ID", order_id, "already exists. Skipping.")
    else:
        orders_dict[order_id] = order
        print("Order", order_id, "added successfully.")

print("Initial Report:")
generate_reports()

new_order = ("O1007", "Arjun", "Chennai", "Tablet", 4)
add_order(new_order)

print("Updated Report:")
generate_reports()

'''
output:
Initial Report:

Total quantity sold per product:
Laptop : 4
Mobile : 8
Tablet : 2

Unique cities where products were sold:
['Bangalore', 'Chennai', 'Delhi', 'Mumbai']

Customer(s) with highest total order quantity:
['Vikram']
Order O1007 added successfully.
Updated Report:

Total quantity sold per product:
Laptop : 4
Mobile : 8
Tablet : 6

Unique cities where products were sold:
['Bangalore', 'Chennai', 'Delhi', 'Mumbai']

Customer(s) with highest total order quantity:
['Arjun']
'''