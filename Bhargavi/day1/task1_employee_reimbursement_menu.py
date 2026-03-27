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
	
# Employee Expense Reimbursement Menu Program

# Welcome message
print(" Welcome to Expense Reimbursement ")

# Variable to store total expenses
total = 0

# Infinite loop to keep showing menu until user exits
while True:
    # Display menu options
    print("1. Add Travel Expense")
    print("2. Add Meal Expense")
    print("3. Add Misc Expense")
    print("4. View Total")
    print("5. Exit")

    # Take user choice
    choice = input("Enter choice: ")

    # Add travel expense
    if choice == '1':
        amt = float(input("Travel amount: ₹"))
        total += amt

    # Add meal expense
    elif choice == '2':
        amt = float(input("Meal amount: ₹"))
        total += amt

    # Add miscellaneous expense
    elif choice == '3':
        amt = float(input("Misc amount: ₹"))
        total += amt

    # View total reimbursement
    elif choice == '4':
        print("Total Reimbursement: ₹", total)

    # Exit program
    elif choice == '5':
        print("Thank you! Exiting now.")
        break

    # Handle invalid input
    else:
        print("Invalid choice. Try again.")


# Welcome to Expense Reimbursement 
# 1. Add Travel Expense
# 2. Add Meal Expense
# 3. Add Misc Expense
# 4. View Total
# 5. Exit
# Enter choice: 1
# Travel amount: ₹100
# 1. Add Travel Expense
# 2. Add Meal Expense
# 3. Add Misc Expense
# 4. View Total
# 5. Exit
# Enter choice: 2
# Meal amount: ₹500
# 1. Add Travel Expense
# 2. Add Meal Expense
# 3. Add Misc Expense
# 4. View Total
# 5. Exit
# Enter choice: 3
# Misc amount: ₹500
# 1. Add Travel Expense
# 2. Add Meal Expense
# 3. Add Misc Expense
# 4. View Total
# 5. Exit
# Enter choice: 4
# Total Reimbursement: ₹ 1100.0
# 1. Add Travel Expense
# 2. Add Meal Expense
# 3. Add Misc Expense
# 4. View Total
# 5. Exit
# Enter choice: 5
# Thank you! Exiting now.
