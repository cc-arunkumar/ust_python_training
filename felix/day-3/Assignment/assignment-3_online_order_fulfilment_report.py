# online order fulfilment


orders = [
 ("O1001", "Neha", "Bangalore", "Laptop", 2),
 ("O1002", "Arjun", "Chennai", "Mobile", 3),
 ("O1003", "Ravi", "Delhi", "Laptop", 1),
 ("O1004", "Fatima", "Bangalore", "Tablet", 2),
 ("O1005", "Vikram", "Mumbai", "Mobile", 5),
 ("O1006", "Neha", "Bangalore", "Laptop", 1)
]

unique_orders = {}
product = {}
cities = []
for i in orders:
    unique_orders[i[0]] = [i[1],i[2],i[3],i[4]]
    product[i[3]] = product.get(i[3],0) + i[4]
    cities.append(i[2])

print("Total quantity sold per product:")
print(product)
print("\n")
unique_cities = set(cities)
print("Unique cities: ")
print(unique_cities)

max = orders[0][4]
name = orders[0][1]
for i in unique_orders:
    if unique_orders[i][3]>max:
        max = unique_orders[i][3]
        name = unique_orders[i][0]
print("\n")
print("Customer(s) with maximum total order quantity: ")
print(name)


unique_orders["O1007"] = ("Neha", "Bangalore", "Laptop", 1)
print("\n")
print("Updated list:")
print(unique_orders)

# output

# Total quantity sold per product:
# {'Laptop': 4, 'Mobile': 8, 'Tablet': 2}


# Unique cities:
# {'Chennai', 'Bangalore', 'Mumbai', 'Delhi'}


# Customer(s) with maximum total order quantity:
# Vikram


# Updated list:
# {'O1001': ['Neha', 'Bangalore', 'Laptop', 2], 'O1002': ['Arjun', 'Chennai', 'Mobile', 3], 'O1003': ['Ravi', 'Delhi', 'Laptop', 1], 'O1004': ['Fatima', 'Bangalore', 'Tablet', 2], 'O1005': ['Vikram', 'Mumbai', 'Mobile', 5], 'O1006': ['Neha', 'Bangalore', 'Laptop', 1], 'O1007': ('Neha', 'Bangalore', 'Laptop', 1)}