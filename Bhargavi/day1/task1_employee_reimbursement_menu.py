#Employee Expense Reimbursement Menu
print(" Welcome to Expense Reimbursement ")
total = 0
while True:
    print("1. Add Travel Expense")
    print("2. Add Meal Expense")
    print("3. Add Misc Expense")
    print("4. View Total")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        amt = float(input("Travel amount: ₹"))
        total += amt
    elif choice == '2':
        amt = float(input("Meal amount: ₹"))
        total += amt
    elif choice == '3':
        amt = float(input("Misc amount: ₹"))
        total += amt
    elif choice == '4':
        print("Total Reimbursement: ₹", total)
    elif choice == '5':
        print("Thank you! Exiting now.")
        break
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
