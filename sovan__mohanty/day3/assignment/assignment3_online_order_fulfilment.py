#Task3 Online Order Fulfilment

orders = [
 ("O1001", "Neha", "Bangalore", "Laptop", 2),
 ("O1002", "Arjun", "Chennai", "Mobile", 3),
 ("O1003", "Ravi", "Delhi", "Laptop", 1),
 ("O1004", "Fatima", "Bangalore", "Tablet", 2),
 ("O1005", "Vikram", "Mumbai", "Mobile", 5),
 ("O1006", "Neha", "Bangalore", "Laptop", 1)
]
order={}
set_unique_cities=set()
name_list=[]
for order_id,name,cities,prod,quantity in orders:
    name_list.append(name)

    if(set in set_unique_cities):
        continue
    set_unique_cities.add(cities)
    if(order_id not in order):
        order[order_id]={name,cities,prod,quantity}
print("The order summary: ",order)

q_laptop=0
q_mobile=0
q_tablet=0
print("Total Quantity sold per product")
for order_id,name,cities,prod,quantity in orders:
    if(prod=="Laptop"):
        q_laptop+=quantity
    if(prod=="Mobile"):
        q_mobile+=quantity
    if(prod=="Tablet"):
        q_tablet+=quantity
print("Laptop----->",q_laptop)
print("Mobile----->",q_mobile)
print("Tablet----->",q_tablet)
print("Set of unique cities: ",set_unique_cities)
cout=0
for name in name_list:
    if(name_list.count(name)>cout):
        cout=name_list.count(name)
for name in name_list:
    if(name_list.count(name)==cout):
        print("Customer with maximum orders ",name)
        break

#Sample Executions
# The order summary:  {'O1001': {'Laptop', 2, 'Bangalore', 'Neha'}, 'O1002': {3, 'Mobile', 'Chennai', 'Arjun'}, 'O1003': {'Ravi', 'Laptop', 'Delhi', 1}, 'O1004': {2, 'Fatima', 'Tablet', 'Bangalore'}, 'O1005': {'Mobile', 5, 'Vikram', 'Mumbai'}, 'O1006': {'Laptop', 'Bangalore', 'Neha', 1}}
# Total Quantity sold per product
# Laptop-----> 4
# Mobile-----> 8
# Tablet-----> 2
# Set of unique cities:  {'Delhi', 'Bangalore', 'Chennai', 'Mumbai'}
# Customer with maximum orders  Neha


    








