#Simulate a simple Employee Expense Management System used to calculate and track reimbursement claims.
#Employees can record travel, meal, and miscellaneous expenses and get total reimbursement.


total_reimbursement = 0.0
while True:
    print("\n====== Employee Expense System ======")
    print("1. Add Travel Expense")
    print("2. Add Meal Expense")
    print("3. Add Miscellaneous Expense")
    print("4. View Total Reimbursement")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        amount = float(input("Enter travel expense amount: "))
        total_reimbursement += amount
        print("Expense added successfully.")
    elif choice == '2':
        amount = float(input("Enter meal expense amount: "))
        total_reimbursement += amount
        print("Expense added successfully.")
    elif choice == '3':
        amount = float(input("Enter miscellaneous expense amount: "))
        total_reimbursement += amount
        print("Expense added successfully.")
    elif choice == '4':
        print(f"Total Reimbursement so far: ₹{total_reimbursement:.2f}")
    elif choice == '5':
        print("Thank you! Have a great day.")
        break
    else:
        print("Invalid choice. Please try again.")

# ====== Employee Expense System ======
# 1. Add Travel Expense
# 2. Add Meal Expense
# 3. Add Miscellaneous Expense
# 4. View Total Reimbursement
# 5. Exit
# Enter your choice: 2
# Enter meal expense amount: 400
# Expense added successfully.

# ====== Employee Expense System ======
# 1. Add Travel Expense
# 2. Add Meal Expense
# 3. Add Miscellaneous Expense
# 4. View Total Reimbursement
# 5. Exit
# Enter your choice: 1
# Enter travel expense amount: 300
# Expense added successfully.

# ====== Employee Expense System ======
# 1. Add Travel Expense
# 2. Add Meal Expense
# 3. Add Miscellaneous Expense
# 4. View Total Reimbursement
# 5. Exit
# Enter your choice: 4
# Total Reimbursement so far: ₹700.00

# ====== Employee Expense System ======
# 1. Add Travel Expense
# 2. Add Meal Expense
# 3. Add Miscellaneous Expense
# 4. View Total Reimbursement
# 5. Exit
# Enter your choice: