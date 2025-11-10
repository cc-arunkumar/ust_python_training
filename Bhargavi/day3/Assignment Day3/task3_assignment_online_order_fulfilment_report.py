# Online Order Fulfilment Report
orders = [
    ("O1001", "Bhargavi", "Bangalore", "Laptop", 2),
    ("O1002", "Meena", "Chennai", "Mobile", 3),
    ("O1003", "Swathi", "Delhi", "Laptop", 1),
    ("O1004", "Rakshi", "Bangalore", "Tablet", 2),
    ("O1005", "Shero", "Mumbai", "Mobile", 5),
    ("O1006", "Chinnu", "Bangalore", "Laptop", 1)
]
order_ids = set()
product_qty = {}
customer_qty = {}
cities = set()

for oid, cust, city, prod, qty in orders:
    if oid in order_ids:
        continue
    order_ids.add(oid)
    product_qty[prod] = product_qty.get(prod, 0) + qty
    customer_qty[cust] = customer_qty.get(cust, 0) + qty
    cities.add(city)

max_qty = max(customer_qty.values())
top_customers = [c for c, q in customer_qty.items() if q == max_qty]

print("Total quantity per product:", product_qty)
print("Unique cities:", cities)
print("Top customer(s):", top_customers)


new_order = ("O1007", "Meena", "Chennai", "Tablet", 4)
oid, cust, city, prod, qty = new_order
if oid not in order_ids:
    order_ids.add(oid)
    product_qty[prod] = product_qty.get(prod, 0) + qty
    customer_qty[cust] = customer_qty.get(cust, 0) + qty
    cities.add(city)

print("\nAfter adding new order:")
print("Products:", product_qty)
print("Customers:", customer_qty)

# Total quantity per product: {'Laptop': 4, 'Mobile': 8, 'Tablet': 2}
# Unique cities: {'Chennai', 'Mumbai', 'Bangalore', 'Delhi'}
# Top customer(s): ['Shero']

# After adding new order:
# Products: {'Laptop': 4, 'Mobile': 8, 'Tablet': 6}
# Customers: {'Bhargavi': 2, 'Meena': 7, 'Swathi': 1, 'Rakshi': 2, 'Shero': 5, 'Chinnu': 1}