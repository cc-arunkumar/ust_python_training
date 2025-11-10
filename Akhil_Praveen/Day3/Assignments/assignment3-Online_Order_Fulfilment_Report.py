
orders = [
 ("O1001", "Neha", "Bangalore", "Laptop", 2),
 ("O1002", "Arjun", "Chennai", "Mobile", 3),
 ("O1003", "Ravi", "Delhi", "Laptop", 1),
 ("O1004", "Fatima", "Bangalore", "Tablet", 2),
 ("O1005", "Vikram", "Mumbai", "Mobile", 5),
 ("O1006", "Neha", "Bangalore", "Laptop", 1)
]
id=1007

def add_order():
    global orders
    global id
    id+=1
    name = input("Enter the employee name: ")
    city = input("Enter the city: ")
    product = input("Enter the product : ")
    quantity = int(input("Enter the quantity : "))
    orders.append(("O"+str(id),name,city,product,quantity))
    print("Order added successfully!")

def total_quantity():
    prod={}
    for i in orders:
        if i[3] in prod:
            prod[i[3]]+=i[4]
        else:
            prod[i[3]]=i[4]
    for i in prod:
        print(f"{i}->{prod[i]}")
def unique_cities():
    uniq_city=set()
    for i in orders:
        uniq_city.add(i[2])
    print(uniq_city)
def cust_max_order():
    max_quant=0
    max_name=""
    for i in orders:
        if i[-1] >max_quant:
            max_quant=i[-1]
            max_name=i[1]
    print(f"{max_name} -> {max_quant}")

def display():
    for i in orders:
        print(i)
        print("")



print("=====   Corporate Skill Matrix System =====")
print("1. Add a new order")
print("2. Total quantity sold per product")
print("3. Set of unique cities.")
print("4. Customer(s) with maximum total order quantity")
print("5. Display all")
print("6. Exit")

while True:
    choice = int(input("Enter your choice: "))
    if(choice==1):
        add_order()
    elif(choice==2):
        total_quantity()
    elif(choice==3):
        unique_cities()
    elif(choice==4):
        cust_max_order()
    elif(choice==5):
        display()
    elif(choice==6):
        print("Thank you!")
        break
    else:
        print("Invalid choice please enter valid choice.")
    print("")

# =====   Corporate Skill Matrix System =====
# 1. Add a new order
# 2. Total quantity sold per product
# 3. Set of unique cities.
# 4. Customer(s) with maximum total order quantity
# 5. Display all
# 6. Exit
# Enter your choice: 1
# Enter the employee name: Akhil
# Enter the city: Kollam
# Enter the product : Laptop
# Enter the quantity : 2
# Order added successfully!

# Enter your choice: 2
# Laptop->6
# Mobile->8
# Tablet->2

# Enter your choice: 3
# {'Bangalore', 'Mumbai', 'Delhi', 'Chennai', 'Kollam'}

# Enter your choice: 4
# Vikram -> 5

# Enter your choice: 5
# ('O1001', 'Neha', 'Bangalore', 'Laptop', 2)

# ('O1002', 'Arjun', 'Chennai', 'Mobile', 3)

# ('O1003', 'Ravi', 'Delhi', 'Laptop', 1)

# ('O1004', 'Fatima', 'Bangalore', 'Tablet', 2)

# ('O1005', 'Vikram', 'Mumbai', 'Mobile', 5)

# ('O1006', 'Neha', 'Bangalore', 'Laptop', 1)

# ('O1008', 'Akhil', 'Kollam', 'Laptop', 2)


# Enter your choice: 6
# Thank you!