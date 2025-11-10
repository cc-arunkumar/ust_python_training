orders = [
 ("O1001", "Neha", "Bangalore", "Laptop", 2),
 ("O1002", "Arjun", "Chennai", "Mobile", 3),
 ("O1003", "Ravi", "Delhi", "Laptop", 1),
 ("O1004", "Fatima", "Bangalore", "Tablet", 2),
 ("O1005", "Vikram", "Mumbai", "Mobile", 5),
 ("O1006", "Neha", "Bangalore", "Laptop", 1)
]

order_data = {}
for order_id,customer,city,product,qty in orders:
    if order_id not in order_data:
        order_data[order_id]={
            "customer":customer,
            "city":city,
            "product":product,
            "quantity":qty
        }
product_sales ={}
for order in order_data.values():
    product = order["product"]
    qty = order["quantity"]
    product_sales[product] = product_sales.get(product,0)+qty

unique_cities = {order["city"] for order in order_data.values()}

customer_totals={}
for order in order_data.values():
    customer = order["customer"]
    qty = order["quantity"]
    customer_totals[customer] = customer_totals.get(customer,0)+ qty
max_quantity = max(customer_totals.values())
top_customers = [cust for cust, total in customer_totals.items() if total == max_quantity]

print("Total quantity sold:",product_sales)
print("Unique cities:",unique_cities)
print("customer with max total order:",top_customers)
print("max quantity order:",max_quantity)

new_order=("01007","Aarav","Hyderabad","Tablet",4)

for order_id,customer,city,product,qty in [new_order]:
    if order_id not in order_data:
        order_data[order_id] = {"customer":customer,"city":city,"product":product,"quantity":qty}
        product_sales[product] = product_sales.get(product,0)+qty
        unique_cities.add(city)
        customer_totals[customer]=customer_totals.get(customer,0) + qty
        customer_totals[customer] = customer_totals.get(customer,0) + qty

max_quantity = max(customer_totals.values())
top_customers = [cust for cust,total in customer_totals.items() if total == max_quantity]

print("Total quantity sold:",product_sales)
print("Unique cities:",unique_cities)
print("customer with max total order:",top_customers)
print("max quantity order:",max_quantity)

# output
# Total quantity sold: {'Laptop': 4, 'Mobile': 8, 'Tablet': 2}
# Unique cities: {'Chennai', 'Mumbai', 'Bangalore', 'Delhi'}
# customer with max total order: ['Vikram']
# max quantity order: 5
# Total quantity sold: {'Laptop': 4, 'Mobile': 8, 'Tablet': 6}       
# Unique cities: {'Hyderabad', 'Mumbai', 'Chennai', 'Bangalore', 'Delhi'}
# customer with max total order: ['Aarav']
# max quantity order: 8