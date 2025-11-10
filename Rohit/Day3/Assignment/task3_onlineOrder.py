# Sample order data
orders = [
    ("O1001", "Neha", "Bangalore", "Laptop", 2),
    ("O1002", "Arjun", "Chennai", "Mobile", 3),
    ("O1003", "Ravi", "Delhi", "Laptop", 1),
    ("O1004", "Fatima", "Bangalore", "Tablet", 2),
    ("O1005", "Vikram", "Mumbai", "Mobile", 5),
    ("O1006", "Neha", "Bangalore", "Laptop", 1)
]

# Step 1: Store orders efficiently and prevent duplicate Order IDs
order_records = {}  # {order_id: (customer, city, product, quantity)}
product_totals = {}  # {product: total_quantity}
customer_totals = {}  # {customer: total_quantity}
unique_cities = set()

for order_id, customer, city, product, quantity in orders:
    if order_id in order_records:
        continue  # Skip duplicate orders
    order_records[order_id] = (customer, city, product, quantity)

    # Update product totals
    product_totals[product] = product_totals.get(product, 0) + quantity

    # Update customer totals
    customer_totals[customer] = customer_totals.get(customer, 0) + quantity

    # Track unique cities
    unique_cities.add(city)

# Step 2: Add new order dynamically
def add_order(order_id, customer, city, product, quantity):
    if order_id in order_records:
        print(f"Order ID {order_id} already exists. Skipping.")
        return

    order_records[order_id] = (customer, city, product, quantity)
    product_totals[product] = product_totals.get(product, 0) + quantity
    customer_totals[customer] = customer_totals.get(customer, 0) + quantity
    unique_cities.add(city)

# Example dynamic update
add_order("O1007", "Neha", "Bangalore", "Tablet", 3)

# Step 3: Generate reports
print(" Total quantity sold per product:")
for product, total in product_totals.items():
    print(f"{product}: {total}")

print("\n Unique cities where products were sold:")
print(unique_cities)

max_quantity = max(customer_totals.values())
top_customers = [cust for cust, qty in customer_totals.items() if qty == max_quantity]
print("\n Customer(s) with highest total order quantity:")
print(top_customers)

# =========sample output==================
# Total quantity sold per product:
# Laptop: 4
# Mobile: 8
# Tablet: 5

#  Unique cities where products were sold:
# {'Delhi', 'Mumbai', 'Chennai', 'Bangalore'}

#  Customer(s) with highest total order quantity:
# ['Neha']