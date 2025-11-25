# Sample orders data: (OrderID, Customer, City, Product, Quantity)
orders = [
    ("O1001", "Neha", "Bangalore", "Laptop", 2),
    ("O1002", "Arjun", "Chennai", "Mobile", 3),
    ("O1003", "Ravi", "Delhi", "Laptop", 1),
    ("O1004", "Fatima", "Bangalore", "Tablet", 2),
    ("O1005", "Vikram", "Mumbai", "Mobile", 5),
    ("O1006", "Neha", "Bangalore", "Laptop", 1)
]

# Dictionary to store order details keyed by order_id
order_data = {}
for order_id, customer, city, product, qty in orders:
    if order_id not in order_data:
        order_data[order_id] = {
            "customer": customer,
            "city": city,
            "product": product,
            "quantity": qty
        }

# Calculate total quantity sold per product
product_sales = {}
for order in order_data.values():
    product = order["product"]
    qty = order["quantity"]
    product_sales[product] = product_sales.get(product, 0) + qty

# Collect all unique cities from orders
unique_cities = {order["city"] for order in order_data.values()}

# Calculate total quantity ordered per customer
customer_totals = {}
for order in order_data.values():
    customer = order["customer"]
    qty = order["quantity"]
    customer_totals[customer] = customer_totals.get(customer, 0) + qty

# Find maximum quantity ordered by any customer
max_quantity = max(customer_totals.values())
top_customers = [cust for cust, total in customer_totals.items() if total == max_quantity]

# Print summary before adding new order
print("Total quantity sold:", product_sales)
print("Unique cities:", unique_cities)
print("Customer with max total order:", top_customers)
print("Max quantity order:", max_quantity)

# Add a new order
new_order = ("01007", "Aarav", "Hyderabad", "Tablet", 4)

for order_id, customer, city, product, qty in [new_order]:
    if order_id not in order_data:
        # Add new order details
        order_data[order_id] = {"customer": customer, "city": city, "product": product, "quantity": qty}
        # Update product sales
        product_sales[product] = product_sales.get(product, 0) + qty
        # Add new city
        unique_cities.add(city)
        # Update customer totals (⚠️ Note: qty is added twice here in your code)
        customer_totals[customer] = customer_totals.get(customer, 0) + qty
        customer_totals[customer] = customer_totals.get(customer, 0) + qty

# Recalculate max quantity and top customers after new order
max_quantity = max(customer_totals.values())
top_customers = [cust for cust, total in customer_totals.items() if total == max_quantity]

# Print updated summary
print("Total quantity sold:", product_sales)
print("Unique cities:", unique_cities)
print("Customer with max total order:", top_customers)
print("Max quantity order:", max_quantity)

# -------------------------
# Expected Output:
# Total quantity sold: {'Laptop': 4, 'Mobile': 8, 'Tablet': 2}
# Unique cities: {'Chennai', 'Mumbai', 'Bangalore', 'Delhi'}
# Customer with max total order: ['Vikram']
# Max quantity order: 5
#
# Total quantity sold: {'Laptop': 4, 'Mobile': 8, 'Tablet': 6}
# Unique cities: {'Hyderabad', 'Mumbai', 'Chennai', 'Bangalore', 'Delhi'}
# Customer with max total order: ['Aarav']
# Max quantity order: 8