# # Task 1: Employee Expense Reimbursement Menu
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
	
# Sample Execution:
# =================
# ====== Employee Expense System ======
# 1. Add Travel Expense
# 2. Add Meal Expense
# 3. Add Miscellaneous Expense
# 4. View Total Reimbursement
# 5. Exit
# Enter your choice: 1
# Enter travel expense amount: 800
# Expense added successfully.

# Enter your choice: 2
# Enter meal expense amount: 250
# Expense added successfully.

# Enter your choice: 4
# Total Reimbursement so far: ₹1050.00

# Enter your choice: 5
# Thank you! Have a great day.

# Code Logic

# Initialize expense categories
travel = 0
meals = 0
other = 0

# Run the program until user chooses to exit
while True:
    # Display menu options
    print("Employee Expense System")
    print("1. Enter Travel cost")
    print("2. Enter Meals cost")
    print("3. Enter Other cost")
    print("4. Total cost as of now")
    print("5. Exit")

    # Take user choice
    choice = int(input("Enter your choice (1-5): "))

    # Match-case handles different options
    match choice:
        case 1:  # Travel expense
            amount = float(input("Enter the travel cost: "))
            travel = travel + amount
            print("Expenses added successfully")
        case 2:  # Meals expense
            amount = float(input("Enter the meals cost: "))
            meals = meals + amount
            print("Meals cost added successfully")
        case 3:  # Other expense
            amount = float(input("Enter other costs: "))
            other = other + amount
            print("Miscellaneous cost added successfully")
        case 4:  # Show total so far
            amount = travel + meals + other
            print(f"Total amount so far: {amount:.2f}")
        case 5:  # Exit program
            print("Thank you! Have a great day")
            break
        case default:  # Default case for invalid input
            print("Invalid choice, try between 1-5")



#output
# Employee Expense System
# 1.Enter Travel cost:
# 2.Enter meals cost:
# 3.Enter other cost:
# 4.Total cost as of now:
# 5.Exit
# Enter your choice(1-5)3
# Enter other costs:400
# miscell is added sucessfull
# Employee Expense System
# 1.Enter Travel cost:
# 2.Enter meals cost:
# 3.Enter other cost:
# 4.Total cost as of now:
# 5.Exit
# Enter your choice(1-5)4
# Total amount so far:1000.00
# Employee Expense System
# 1.Enter Travel cost:
# 2.Enter meals cost:
# 3.Enter other cost:
# 4.Total cost as of now:
# 5.Exit
# Enter your choice(1-5)5
# ThankYou have a Great day
# PS C:\Users\303379\day1_training> 