#Assignment 1 — Expense Reimbursement Tracker
from datetime import date
claims_data = [
 ("E101", "C001", 3200, "Travel", "2025-11-02"),
 ("E101", "C002", 1800, "Food", "2025-11-03"),
 ("E102", "C003", 4500, "Hotel", "2025-11-02"),
 ("E103", "C004", 1200, "Travel", "2025-11-02"),
 ("E102", "C005", 2200, "Travel", "2025-11-04"),
 ("E101", "C006", 4200, "Hotel", "2025-11-05")
]
ch='Y'
count=7
while(ch=='Y' or ch=='y'):
    print("====== Employee Expense System ======")
    print("1. Add Claims")
    print("2. Total Claim")
    print("3. Display")
    print("4. Exit")
    n=int(input("Choose choice:"))
    if(n==1):
        emp_id = input("Enter EMP ID: ")
        amount = int(input("Enter the amount: "))
        category = input("Category (Travel, Hotel, Food, etc.) : ")
        claims_data.append((emp_id,"C00"+str(count),amount,category,date.today()))
        count+=1
        print("Added Successfully")
    elif(n==2):
        emp_id = input("Enter the EMP ID to check : ")
        total=0
        for i in claims_data:
            if(i[0]==emp_id):
                total+=i[2]
        print(f"Total for {emp_id} is {total}")
    elif(n==3):
        L={}
        category=[]
        for i in claims_data:
            if(i[3] not in category):
                category.append(i[3])
            if(i[0] not in L):
                L[i[0]]=0
            L[i[0]]+=i[2]
        emp=[]
        for i in L:
            print(f"For Employee {i} total is {L.get(i)}")
            if(L.get(i)>10000):
                emp.append(i)
        print(f"List of employee having total >10000 : {emp}")
        print(f"Unique Categories : {category}")     
    elif(n==4):
        print("Thank you! Have a great day.")
        break
    else:
        print("Provide a number within range!!")
    ch=input("\nDo you wish to continue(Y/N)")
#Output
# ====== Employee Expense System ======
# 1. Add Claims 
# 2. Total Claim
# 3. Display    
# 4. Exit       
# Choose choice:1
# Enter EMP ID: E101
# Enter the amount: 5000
# Category (Travel, Hotel, Food, etc.) : Travel
# Added Successfully

# Do you wish to continue(Y/N)y
# ====== Employee Expense System ======
# 1. Add Claims
# 2. Total Claim
# 3. Display
# 4. Exit
# Choose choice:2
# Enter the EMP ID to check : E102
# Total for E102 is 6700

# Do you wish to continue(Y/N)y
# ====== Employee Expense System ======
# 1. Add Claims
# 2. Total Claim
# 3. Display
# 4. Exit
# Choose choice:3
# For Employee E101 total is 14200
# For Employee E102 total is 6700
# For Employee E103 total is 1200
# List of employee having total >10000 : ['E101']
# Unique Categories : ['Travel', 'Food', 'Hotel']

# Do you wish to continue(Y/N)y
# ====== Employee Expense System ======
# 1. Add Claims
# 2. Total Claim
# 3. Display
# 4. Exit
# Choose choice:4
# Thank you! Have a great day.