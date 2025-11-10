# Task_1_Employee_Expense_Reimbursement_Menu


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
