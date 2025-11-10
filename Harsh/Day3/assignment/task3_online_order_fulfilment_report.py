orders = [
    ("01001", "Neha", "Bangalore", "Laptop", 2),
    ("01002", "Arjun", "Chennai", "Mobile", 3),
    ("01003", "Ravi", "Delhi", "Laptop", 1),
    ("01004", "Fatima", "Bangalore", "Tablet", 2),
    ("01005", "Vikram", "Mumbai", "Mobile", 5),
    ("01006", "Neha", "Bangalore", "Laptop", 1)
]

order_data = {}
for oid, cname, city, product, qty in orders:
    if oid not in order_data:
        order_data[oid] = (cname, city, product, qty)

product_qty = {}
for  cname, city, prod, qty in order_data.values():
    product_qty[prod] = product_qty.get(prod, 0) + qty

cities = set()
for cname in order_data.values():
    cities.add(cname)

customer_qty = {}
for cname, city, prod, qty in order_data.values():
    customer_qty[cname] = customer_qty.get(cname, 0) + qty

max_qty = 0
for  qty in customer_qty.values():
    if qty > max_qty:
        max_qty = qty

top_customers = []
for cname,  qty in customer_qty.items():
    if qty == max_qty:
        top_customers.append(cname)

def add_order(oid, cname, city, product, qty):
    if oid not in order_data:
        order_data[oid] = (cname, city, product, qty)
        print("Order added:", oid)
    else:
        print("Duplicate Order ID")

add_order("01007", "Meena", "Pune", "Mobile", 4)

print("\nTotal Quantity per Product:", product_qty)
print("Unique Cities:", cities)
print("Top Customer(s):", top_customers)


# Order added: 01007

# Total Quantity per Product: {'Laptop': 4, 'Mobile': 8, 'Tablet': 2}
# Unique Cities: {('Fatima', 'Bangalore', 'Tablet', 2), ('Neha', 'Bangalore', 'Laptop', 2), ('Ravi', 'Delhi', 'Laptop', 1), ('Neha', 'Bangalore', 'Laptop', 1), ('Vikram', 'Mumbai', 'Mobile', 5), ('Arjun', 'Chennai', 'Mobile', 3)}
# Top Customer(s): ['Vikram']