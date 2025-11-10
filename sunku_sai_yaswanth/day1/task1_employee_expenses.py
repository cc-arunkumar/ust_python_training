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
travel=0
meal=0
miscellaneous=0
while True:
    print("=====Employee Expense System======")
    print("1.Add Travel Expense.")
    print("2.Add Meal Expense.")
    print("3.Add Miscellaneous Expenses")
    print("4.view Total Reimbursement")
    print("5.Exit")
    
    choice=int(input("Enter your choise: "))
    if choice==1:
        travel=float(input("Enter the travel expense amount: "))
            
    elif choice==2:
        meal=float(input("Enter the meal amount:"))
            
    elif choice==3:
        miscellaneous=float(input("enter the miscellaneous amount:"))
            
    elif choice==4:
        total=travel+meal+miscellaneous
        print("total expenses:",total)
    elif choice==5:
        print("Exit")
        break


#sample output
# =====Employee Expense System======
# 1.Add Travel Expense.
# 2.Add Meal Expense.
# 3.Add Miscellaneous Expenses
# 4.view Total Reimbursement
# 5.Exit
# Enter your choise: 1
# Enter the travel expense amount: 100
# =====Employee Expense System======
# 1.Add Travel Expense.
# 2.Add Meal Expense.
# 3.Add Miscellaneous Expenses
# 4.view Total Reimbursement
# 5.Exit
# Enter your choise: 2
# Enter the meal amount:200
# =====Employee Expense System======
# 1.Add Travel Expense.
# 2.Add Meal Expense.
# 3.Add Miscellaneous Expenses
# 4.view Total Reimbursement
# 5.Exit
# Enter your choise: 3
# enter the miscellaneous amount:800
# =====Employee Expense System======
# 1.Add Travel Expense.
# 2.Add Meal Expense.
# 3.Add Miscellaneous Expenses
# 4.view Total Reimbursement
# 5.Exit
# Enter your choise: 4  
# total expenses: 1100.0
# =====Employee Expense System======
# 1.Add Travel Expense.
# 2.Add Meal Expense.
# 3.Add Miscellaneous Expenses
# 4.view Total Reimbursement
# 5.Exit
# Enter your choise: 5
# Exit