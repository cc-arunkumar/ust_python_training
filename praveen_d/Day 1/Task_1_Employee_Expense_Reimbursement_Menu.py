# Task_1_Employee_Expense_Reimbursement_Menu

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

total_expence=0
isOk=True
while isOk:
    print("1. Add Travel Expense")
    print("2. Add Meal Expense")
    print("3. Add Miscellaneous Expense")
    print("4. View Total Reimbursement")
    print("5. Exit")
    print("Enter your choice:")
    option= int(input())

    match option:
        case 1:
            total_expence+=int(input("Enter travel expence:"))
            print("Added Sucessfully")
        case 2:
            total_expence+=int(input("Enter Meal Expense:"))
            print("Added Sucessfully")
        case 3:
            total_expence+=int(input("Enter Miscellaneous expence:"))
            print("Added Sucessfully")
        case 4:
            print(f"Total Reimbursement so far: ₹{total_expence}")
        case 5:
            print("Ending.....")
            isOk=False

# Employee_Expense_Reimbursement_Menu.py"
# 1. Add Travel Expense
# 2. Add Meal Expense
# 3. Add Miscellaneous Expense
# 4. View Total Reimbursement
# 5. Exit
# Enter your choice:
# 1
# Enter travel expence:100
# Added Sucessfully
# 1. Add Travel Expense
# 2. Add Meal Expense
# 3. Add Miscellaneous Expense
# 4. View Total Reimbursement
# 5. Exit
# Enter your choice:
# 2
# Enter Meal Expense:200
# Added Sucessfully
# 1. Add Travel Expense
# 2. Add Meal Expense
# 3. Add Miscellaneous Expense
# 4. View Total Reimbursement
# 5. Exit
# Enter your choice:
# 3
# Enter Miscellaneous expence:100
# Added Sucessfully
# 1. Add Travel Expense
# 2. Add Meal Expense
# 3. Add Miscellaneous Expense
# 4. View Total Reimbursement
# 5. Exit
# Enter your choice:
# 4
# Total Reimbursement so far: ₹400
# 1. Add Travel Expense
# 2. Add Meal Expense
# 3. Add Miscellaneous Expense
# 4. View Total Reimbursement
# 5. Exit
# Enter your choice:
# 5
# Ending.....
