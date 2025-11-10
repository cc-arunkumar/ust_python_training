# Online Order Fulfilment Report

orders = [
    ("O1001", "Neha", "Bangalore", "Laptop", 2),
    ("O1002", "Arjun", "Chennai", "Mobile", 3),
    ("O1003", "Ravi", "Delhi", "Laptop", 1),
    ("O1004", "Fatima", "Bangalore", "Tablet", 2),
    ("O1005", "Vikram", "Mumbai", "Mobile", 5),
    ("O1006", "Neha", "Bangalore", "Laptop", 1)
]


unique_order_ids = set()
total_quantity_per_product = {}
unique_cities = set()
customer_total_quantity = {}


for order_id, customer_name, city, product_name, quantity in orders:
    
    if order_id not in unique_order_ids:
        unique_order_ids.add(order_id)
        
        
        if product_name not in total_quantity_per_product:
            total_quantity_per_product[product_name] = 0
        total_quantity_per_product[product_name] += quantity
        
        
        unique_cities.add(city)
        
        
        if customer_name not in customer_total_quantity:
            customer_total_quantity[customer_name] = 0
        customer_total_quantity[customer_name] += quantity


add_new = input("Do you want to add a new order? (Y/N): ")
if add_new.lower() == "y":
    new_order_id = input("Enter new Order ID: ")
    if new_order_id in unique_order_ids:
        print("Duplicate Order ID! Not added.")
    else:
        new_customer_name = input("Enter Customer Name: ")
        new_city = input("Enter City: ")
        new_product_name = input("Enter Product Name: ")
        new_quantity = int(input("Enter Quantity: "))

        
        orders.append((new_order_id, new_customer_name, new_city, new_product_name, new_quantity))
        unique_order_ids.add(new_order_id)
        unique_cities.add(new_city)
        
        total_quantity_per_product[new_product_name] = total_quantity_per_product.get(new_product_name, 0) + new_quantity
        customer_total_quantity[new_customer_name] = customer_total_quantity.get(new_customer_name, 0) + new_quantity
        
        print("Order added successfully!\n")


print("Total quantity sold per product:")
for product_name, total_qty in total_quantity_per_product.items():
    print(product_name, ":", total_qty)

print("\nUnique cities where products were sold:")
print(unique_cities)


max_quantity = max(customer_total_quantity.values())
print("\nCustomer(s) with the highest total order quantity:")
for customer_name, total_qty in customer_total_quantity.items():
    if total_qty == max_quantity:
        print(customer_name)


#sample output
# Do you want to add a new order? (Y/N): y
# Enter new Order ID: O1007
# Enter Customer Name: Neha
# Enter City: Bangalore
# Enter Product Name: Mobile
# Enter Quantity: 4
# Order added successfully!

# Total quantity sold per product:
# Laptop : 4
# Mobile : 12
# Tablet : 2

# Unique cities where products were sold:
# {'Chennai', 'Delhi', 'Bangalore', 'Mumbai'}

# Customer(s) with the highest total order quantity:
# Neha