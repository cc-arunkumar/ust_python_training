def employee_expns_systm():
    print("===== Employee Expense System =====")
    print("1. Add travel expense")
    print("2. Add meal expense")
    print("3. Add miscellaneous expense")
    print("4. View total reimbursement")
    print("5. Exit")
    total=0
    while True:
        choice = int(input("Enter your choice: "))
        amount=0
        if(choice==1):
            amount=float(input("Enter travel expense amount: "))
            print("Expense added successfully.")
        elif(choice==2):
            amount=float(input("Enter meal expense amount: "))
            print("Expense added successfully.")
        elif(choice==3):
            amount=float(input("Enter miscellaneous expense amount: "))
            print("Expense added successfully.")
        elif(choice==4):
            print("Total reimbursement so far =  ",total)
        elif(choice==5):
            print("Thank you! Have a nice day.")
            break
        else:
            print("Invalid choice please enter valid choice.")
        total+=amount
        print("")

employee_expns_systm()

# Output

# ===== Employee Expense System =====
# 1. Add travel expense
# 2. Add meal expense
# 3. Add miscellaneous expense
# 4. View total reimbursement
# 5. Exit
# Enter your choice: 1
# Enter travel expense amount: 800
# Expense added successfully.

# Enter your choice: 2
# Enter meal expense amount: 567
# Expense added successfully.

# Enter your choice: 3
# Enter miscellaneous expense amount: 687
# Expense added successfully.

# Enter your choice: 4
# Total reimbursement so far =   2054.0

# Enter your choice: 5
# Thank you! Have a nice day.