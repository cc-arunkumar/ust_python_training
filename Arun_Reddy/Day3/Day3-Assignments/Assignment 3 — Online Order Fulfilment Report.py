orders = [
 ("O1001", "Neha", "Bangalore", "Laptop", 2),
 ("O1002", "Arjun", "Chennai", "Mobile", 3),
 ("O1003", "Ravi", "Delhi", "Laptop", 1),
 ("O1004", "Fatima", "Bangalore", "Tablet", 2),
 ("O1005", "Vikram", "Mumbai", "Mobile", 5),
 ("O1006", "Neha", "Bangalore", "Laptop", 1)
]
# Order ID
# Customer name
# City
# Assignment 3
# Product
# Quantity
Order={}
for orderid,name,city,product,quantity in orders:
    if orderid not in Order:
        Order[orderid]=[]
    Order[orderid].append((name,city,product,quantity))
my_dict1={}

cities=set()
customers=set()

for k,v in Order.items():
    for d in v:
        name,city,product,quantity=d
        cities.add(city)
        if product in my_dict1:
            my_dict1[product]+=quantity
        else:
            my_dict1[product]=0
for k,v in my_dict1.items():
    print(f"{k} =={v}")

print(cities)
my_dict2={}
mx=0
nme=""
for k,v in Order.items():
    for d in v:
        name,city,product,quantity=d
        if name in my_dict2:
            my_dict2[name]+=quantity
        else:
            my_dict2[name]=quantity
# for k,v in my_dict2.items():
#     if v>mx:
#         mx=v
#         nme=k
# print(nme)
print(max(my_dict2,key=my_dict2.get))

# ===========sample Execution==========
# Laptop ==2
# Mobile ==5
# Tablet ==0
# {'Chennai', 'Mumbai', 'Bangalore', 'Delhi'}
# Vikram



    
