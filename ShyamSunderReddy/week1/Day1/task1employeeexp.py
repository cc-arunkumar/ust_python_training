#Task 1: Employee Expense Reimbursement Menu

#Code
total=0.0
print("====== Employee Expense System ======")
print("1. Add Travel Expense")
print("2. Add Meal Expense")
print("3. Add Miscellaneous Expense")
print("4. View Total Reimbursement")
print("5. Exit")
while(True):
    
    n=int(input("Enter your choice: "))
    
    if(n==1):
        amount=int(input("Enter travel expense amount: "))
        total=total+amount
        print("Expene added successfully.")
    elif(n==2):
        amount=int(input("Enter Meal expense amount: "))
        total=total+amount
        print("Expene added successfully.")
    elif(n==3):
        amount=int(input("Enter Miscellaneous expense amount: "))
        total=total+amount
        print("Expene added successfully.")
    elif(n==4):
        print(f"Total Reimbursement so far: ₹{total}")
    elif(n==5):
        print("Thank you! Have a great day.")
        break
    else:
        print("Enter proper choice")

#Sample output
#====== Employee Expense System ======
# 1. Add Travel Expense
# 2. Add Meal Expense
# 3. Add Miscellaneous Expense
# 4. View Total Reimbursement
# 5. Exit
# Enter your choice: 1
# Enter travel expense amount: 500
# Expene added successfully.
# Enter your choice: 2
# Enter Meal expense amount: 400
# Expene added successfully.
# Enter your choice: 4
# Total Reimbursement so far: ₹900.0
# Enter your choice: 5
# Thank you! Have a great day.