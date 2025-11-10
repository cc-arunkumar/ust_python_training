#Assignment 3 — Online Order Fulfilment Report
orders = [
 ("O1001", "Neha", "Bangalore", "Laptop", 2),
 ("O1002", "Arjun", "Chennai", "Mobile", 3),
 ("O1003", "Ravi", "Delhi", "Laptop", 1),
 ("O1004", "Fatima", "Bangalore", "Tablet", 2),
 ("O1005", "Vikram", "Mumbai", "Mobile", 5),
 ("O1006", "Neha", "Bangalore", "Laptop", 1)
 ]
ch='Y'
count=7
while(ch=='Y' or ch=='y'):
    print("====== Order System ======")
    print("1. Add Order")
    print("2. Generate Report")
    print("3. Exit")
    n=int(input("Choose choice:"))
    if(n==1):
        name= input("Enter the name : ")
        location = input("Enter the location : ")
        product= input("Enter the product name : ")
        qty = int(input("Enter the qty : "))
        orders.append(("O100"+str(count),name,location,product,qty))        
        print("Order Created Successfully")
    elif(n==2):
        products={}
        cities=[]
        maxi=0
        maxi_cust=""
        for i in orders:
            if(i[4]>maxi):
                maxi=i[4]
                maxi_cust=i[1]
            if(i[2] not in cities):
                cities.append(i[2])
            if(i[3] not in products):
                products[i[3]]=0
            products[i[3]]+=i[4]
        for j in products:
            print(f"Product {j} was sold {products.get(j)} times")
        print(f"Unique cities are : {cities}")
        print(f"Customer {maxi_cust} has the maximum order of {maxi}")
    elif(n==3):
        print("Thank you! Have a great day.")
        break
    else:
        print("Provide a number within range!!")
    ch=input("\nDo you wish to continue(Y/N)")
#Output
# ====== Order System ======
# 1. Add Order      
# 2. Generate Report
# 3. Exit
# Choose choice:1   
# Enter the name : Arjun
# Enter the location : Trivandrum
# Enter the product name : Mobile
# Enter the qty : 1
# Order Created Successfully

# Do you wish to continue(Y/N)y
# ====== Order System ======
# 1. Add Order
# 2. Generate Report
# 3. Exit
# Choose choice:2
# Product Laptop was sold 4 times
# Product Mobile was sold 9 times
# Product Tablet was sold 2 times
# Unique cities are : ['Bangalore', 'Chennai', 'Delhi', 'Mumbai', 'Trivandrum']
# Customer Vikram has the maximum order of 5

# Do you wish to continue(Y/N)y
# ====== Order System ======
# 1. Add Order
# 2. Generate Report
# 3. Exit
# Choose choice:3
# Thank you! Have a great day.