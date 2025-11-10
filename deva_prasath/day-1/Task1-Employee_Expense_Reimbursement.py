## Task 1: Employee Expense Reimbursement Menu

reimbursement=0.0
while(True):
    print("\n===Employee Expense System===")
    print("1.Add Travel expense")
    print("2.Add Meal expense")
    print("3.Add Miscellaneous expense")
    print("4.View Total reimbursement")
    print("5.Exit")
    chc=input("Enter your choice: ")
    if chc== '1':
        amt=float(input("Enter travel expense amount:"))
        reimbursement+=amt
        print("Expense added successfully")
    elif chc=='2':
        amt=float(input("Enter meal expense amount:"))
        reimbursement+=amt
        print("Expense added successfully")
    elif chc=='3':
        amt=float(input("Enter miscellaneous expense:"))
        reimbursement+=amt
        print("Expense added successfully")
    elif chc=='4':
        print(f"Total reimbursement so far: {reimbursement:.2f}")
    elif chc=='5':
        print("Thank You! Have a great day")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5")

# Sample Execution

# ===Employee Expense System===
# 1.Add Travel expense
# 2.Add Meal expense
# 3.Add Miscellaneous expense
# 4.View Total reimbursement
# 5.Exit
# Enter your choice: 1
# Enter travel expense amount:1000
# Expense added successfully

# ===Employee Expense System===
# 1.Add Travel expense
# 2.Add Meal expense
# 3.Add Miscellaneous expense
# 4.View Total reimbursement
# 5.Exit
# Enter your choice: 2
# Enter meal expense amount:1000
# Expense added successfully

# ===Employee Expense System===
# 1.Add Travel expense
# 2.Add Meal expense
# 3.Add Miscellaneous expense
# 4.View Total reimbursement
# 5.Exit
# Enter your choice: 3
# Enter miscellaneous expense:1000
# Expense added successfully

# ===Employee Expense System===
# 1.Add Travel expense
# 2.Add Meal expense
# 3.Add Miscellaneous expense
# 4.View Total reimbursement
# 5.Exit
# Enter your choice: 4
# Total reimbursement so far: 3000.00

# ===Employee Expense System===
# 1.Add Travel expense
# 2.Add Meal expense
# 3.Add Miscellaneous expense
# 4.View Total reimbursement
# 5.Exit
# Enter your choice: 5
# Thank You! Have a great day