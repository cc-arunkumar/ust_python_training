# Assignment 3 — Online Order Fulfilment Report
orders = [
 ("O1001", "Neha", "Bangalore", "Laptop", 2),
 ("O1002", "Arjun", "Chennai", "Mobile", 3),
 ("O1003", "Ravi", "Delhi", "Laptop", 1),
 ("O1004", "Fatima", "Bangalore", "Tablet", 2),
 ("O1005", "Vikram", "Mumbai", "Mobile", 5),
 ("O1006", "Neha", "Bangalore", "Laptop", 1)
]

orders_list={}
unique_product=set()

for order_id,name,city,product,quanity in orders:
    orders_list[product]=orders_list.get(product,0)+quanity
    unique_product.add(city)

print("Order List:",orders_list)
print("Unique cities",unique_product)
customer_name={}
for order_id,name,city,product,quanity in orders:
    customer_name[name]=customer_name.get(name,0)+quanity
max=0
for key,val in customer_name.items():
    if val>max:
        max=val
        name=key
print(f"Maximum total order: {name}->{max}")
orders_list={}
for order_id, name, city, product, quantity in orders:
    orders_list[order_id] = {
        "name": name,
        "city": city,
        "product": product,
        "quantity": quantity
    }
print("Before adding new list:",orders_list)
order_id = "O1007"
name = "Sai"
city = "Hyderabad"
product = "Laptop"
quantity = 3

if order_id not in orders_list:
    orders_list[order_id] = {
        "name": name,
        "city": city,
        "product": product,
        "quantity": quantity
    }
    print(f"Adding new list dynamically: {orders_list}")




# Sample output

# Order List: {'Laptop': 4, 'Mobile': 8, 'Tablet': 2}


# Unique cities {'Bangalore', 'Delhi', 'Mumbai', 'Chennai'}

# Maximum total order: Vikram->5

# Before adding new list: {'O1001': {'name': 'Neha', 'city': 'Bangalore', 'product': 'Laptop', 'quantity': 2}, 
# 'O1002': {'name': 'Arjun', 'city': 'Chennai', 'product': 'Mobile', 'quantity': 3}, 
# 'O1003': {'name': 'Ravi', 'city': 'Delhi', 'product': 'Laptop', 'quantity': 1}, 
# 'O1004': {'name': 'Fatima', 'city': 'Bangalore', 'product': 'Tablet', 'quantity': 2}, 
# 'O1005': {'name': 'Vikram', 'city': 'Mumbai', 'product': 'Mobile', 'quantity': 5}, 
# 'O1006': {'name': 'Neha', 'city': 'Bangalore', 'product': 'Laptop', 'quantity': 1}}



# Adding new list dynamically: {'O1001': {'name': 'Neha', 'city': 'Bangalore', 'product': 'Laptop', 'quantity': 2}, 
# 'O1002': {'name': 'Arjun', 'city': 'Chennai', 'product': 'Mobile', 'quantity': 3}, 
# 'O1003': {'name': 'Ravi', 'city': 'Delhi', 'product': 'Laptop', 'quantity': 1}, 
# 'O1004': {'name': 'Fatima', 'city': 'Bangalore', 'product': 'Tablet', 'quantity': 2}, 
# 'O1005': {'name': 'Vikram', 'city': 'Mumbai', 'product': 'Mobile', 'quantity': 5}, 
# 'O1006': {'name': 'Neha', 'city': 'Bangalore', 'product': 'Laptop', 'quantity': 1},
#  'O1007': {'name': 'Sai', 'city': 'Hyderabad', 'product': 'Laptop', 'quantity': 3}}

