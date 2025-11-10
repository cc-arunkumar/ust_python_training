#Assignment 3 — Online Order Fulfilment Report

#Code 
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
for order_id, name, city , product_name, quantity in orders:
    name_list.append(name)

    if(set in set_unique_cities):
        continue
    set_unique_cities.add(city)
    if(order_id not in order):
        order[order_id]={name,city,product_name,quantity}

print("The order Summary : ",order)
print("Set of unique cities : ",set_unique_cities)

q_laptop=0
q_mobile=0
q_tablet=0
print("Total quantity sold per product : ")
for order_id,name,city,product_name,quantity in orders:
    if(product_name=="Laptop"):
        q_laptop+=quantity
    if(product_name=="Mobile"):
        q_mobile+=quantity
    if(product_name=="Tablet"):
        q_tablet+=quantity
print("Laptop -->",q_laptop)
print("Mobile -->",q_mobile)
print("Tablet -->",q_tablet)
count =0
for name in name_list:
    if(name_list.count(name)>count):
        count+=name_list.count(name)
for name in name_list:
    if(name_list.count(name)==count):
        print("Customer with maximum orders :",name)
        break
#Output
# The order Summary :  {'O1001': {2, 'Neha', 'Laptop', 'Bangalore'}, 'O1002': {'Mobile', 3, 'Chennai', 'Arjun'}, 'O1003': {'Delhi', 1, 'Laptop', 'Ravi'}, 'O1004': {'Fatima', 2, 'Tablet', 'Bangalore'}, 'O1005': {'Vikram', 'Mumbai', 'Mobile', 5}, 'O1006': {1, 'Neha', 'Laptop', 'Bangalore'}}
# Set of unique cities :  {'Delhi', 'Mumbai', 'Bangalore', 'Chennai'}
# Total quantity sold per product :
# Laptop --> 4
# Mobile --> 8
# Tablet --> 2
# Customer with maximum orders : Neha

