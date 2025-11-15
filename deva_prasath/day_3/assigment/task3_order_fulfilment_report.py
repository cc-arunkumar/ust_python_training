# Assignment 3 — Online Order Fulfilment Report
# UST’s e-commerce division tracks daily customer orders
# Sample orders data with order ID, customer, city, product, and quantity
orders_list = [
    ("O1001", "Neha", "Bangalore", "Laptop", 2),
    ("O1002", "Arjun", "Chennai", "Mobile", 3),
    ("O1003", "Ravi", "Delhi", "Laptop", 1),
    ("O1004", "Fatima", "Bangalore", "Tablet", 2),
    ("O1005", "Vikram", "Mumbai", "Mobile", 5),
    ("O1006", "Neha", "Bangalore", "Laptop", 1)
]

# Initialize necessary data structures
order_ids = set()          # Set to track unique order IDs
product_totals = {}        # Dictionary to track total quantity sold per product
cities = set()             # Set to track unique cities where products were sold
customer_totals = {}       # Dictionary to track total quantity ordered by each customer

# Process the orders data
for order_id, customer, city, product, qty in orders_list:
    if order_id in order_ids:  # Skip duplicate orders
        continue
    order_ids.add(order_id)    # Add the order ID to the set
    
    # Update product totals
    if product not in product_totals:
        product_totals[product] = 0
    product_totals[product] += qty
    
    # Add city to the set of cities
    cities.add(city)
    
    # Update customer totals
    if customer not in customer_totals:
        customer_totals[customer] = 0
    customer_totals[customer] += qty

# Function to add a new order and update relevant data structures
def add_order(order_id, customer, city, product, qty):
    if order_id in order_ids:  # Check if order ID already exists
        print("Order ID already exists")
        return

    order_ids.add(order_id)    # Add new order ID
    orders_list.append((order_id, customer, city, product, qty))  # Append the new order

    # Update product totals
    if product not in product_totals:
        product_totals[product] = 0
    product_totals[product] += qty

    cities.add(city)           # Add new city to the cities set

    # Update customer totals
    if customer not in customer_totals:
        customer_totals[customer] = 0
    customer_totals[customer] += qty

# Function to print the report with various details
def print_report():
    print("\nTotal Quantity Sold per Product:")
    for product, total in product_totals.items():
        print(" -", product, ":", total)
    
    print("\nUnique Cities Where Products Were Sold:")
    for city in sorted(cities):  # Print cities in sorted order
        print(" -", city)
    
    # Find the customer with the maximum quantity ordered
    max_qty = max(customer_totals.values())
    print("\nCustomer with Maximum Total Quantity Ordered:")
    for customer, total in customer_totals.items():
        if total == max_qty:  # Display the customer(s) with the highest order total
            print(" -", customer, ":", total)

# Adding a new order
add_order("O1007", "Arjun", "Chennai", "Laptop", 2)

# Print the report with the latest data
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