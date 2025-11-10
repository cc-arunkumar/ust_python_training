# Task 1: Employee Expense Reimbursement Menu
# Objective

# Simulate a simple Employee Expense Management System used to calculate and track reimbursement claims.
# Employees can record travel, meal, and miscellaneous expenses and get total reimbursement.

# ====== Employee Expense System ======
# 1. Add Travel Expense
# 2. Add Meal Expense
# 3. Add Miscellaneous Expense
# 4. View Total Reimbursement
# 5. Exit
# Enter your choice:


# Functional Rules
# ================
# Travel Expense:
# 	User enters the travel amount (e.g., 1200.50).
# 	Add it to the total.

# Meal Expense:
# 	User enters the meal amount.
# 	Add it to the total.

# Miscellaneous Expense:
# 	User enters other small expenses (e.g., internet, local transport).
# 	Add to total.

# View Total Reimbursement:
# 	Display total expenses recorded so far with a thank-you message.

# Exit:
# 	Stop the program.

total=0.0
while True:
    print("1.add travel expense")
    print("2.add meal expense")
    print("3.add miscellaneous expense")
    print("4.view total reimbursement")
    print("5.exit")
    choice =input("Enter your choice:")
    if choice=='1':
        amount=float(input("enter travel expense amount:"))
        print("expense added successfully")
        total+=amount
    elif choice=='2':
        amount=float(input("Enter meal expense amount:"))
        print("expense added successfully")
        total+=amount
    elif choice=='3':
        amount=float(input("Enter miscellaneous expense amount:"))
        print("expense added successfully")
        total+=amount
    elif choice=='4':
        print("total reimburesement so far:",total)
    elif choice=='5':
        print("thank you! have a great day")
        break
    else:
        print("invalid")


#o/p:
# 1.add travel expense
# 2.add meal expense
# 3.add miscellaneous expense
# 4.view total reimbursement
# 5.exit
# Enter your choice:1
# enter travel expense amount:1000
# expense added successfully
# 1.add travel expense
# 2.add meal expense
# 3.add miscellaneous expense
# 4.view total reimbursement
# 5.exit
# Enter your choice:3  
# Enter miscellaneous expense amount:300 
# expense added successfully
# 1.add travel expense
# 2.add meal expense
# 3.add miscellaneous expense
# 4.view total reimbursement
# 5.exit
# Enter your choice:4
# total reimburesement so far: 1300.0
# 1.add travel expense
# 2.add meal expense
# 3.add miscellaneous expense
# 4.view total reimbursement
# 5.exit
# Enter your choice:5
# thank you! have a great day