# Task 1: Employee Expense Reimbursement Menu
total=0
ch='Y'
while(ch=='Y' or ch=='y'):
    print("====== Employee Expense System ======")
    print("1. Add Travel Expense")
    print("2. Add Meal Expense")
    print("3. Add Miscellaneous Expense")
    print("4. View Total Reimbursement")
    print("5. Exit")
    n=int(input("Choose choice:"))
    if(n==1):
        travel_amount=float(input("Enter the Travel amount : "))
        total+=travel_amount
        print("Expense added successfully")
    elif(n==2):
        meal_amount=float(input("Enter the Meal amount : "))
        total+=meal_amount
        print("Expense added successfully")
    elif(n==3):
        additional_amount=float(input("Enter the Miscellaneous amount : "))
        total+=additional_amount
        print("Expense added successfully")
    elif(n==4):
        print("Total Reimbursement so far:",total)
    elif(n==5):
        print("Thank you! Have a great day.")
        break
    else:
        print("Provide a number within range!!")
    ch=input("\nDo you wish to continue(Y/N)")
#Output
# ====== Employee Expense System ======
# 1. Add Travel Expense
# 2. Add Meal Expense
# 3. Add Miscellaneous Expense
# 4. View Total Reimbursement
# 5. Exit
# Choose choice:1
# Enter the Travel amount : 1000
# Expense added successfully

# Do you wish to continue(Y/N)y
# ====== Employee Expense System ======
# 1. Add Travel Expense
# 2. Add Meal Expense
# 3. Add Miscellaneous Expense
# 4. View Total Reimbursement
# 5. Exit
# Choose choice:2
# Enter the Meal amount : 100
# Expense added successfully

# Do you wish to continue(Y/N)y
# ====== Employee Expense System ======
# 1. Add Travel Expense
# 2. Add Meal Expense
# 3. Add Miscellaneous Expense
# 4. View Total Reimbursement
# 5. Exit
# Choose choice:3
# Enter the Miscellaneous amount : 10
# Expense added successfully

# Do you wish to continue(Y/N)y
# ====== Employee Expense System ======
# 1. Add Travel Expense
# 2. Add Meal Expense
# 3. Add Miscellaneous Expense
# 4. View Total Reimbursement
# 5. Exit
# Choose choice:4
# Total Reimbursement so far: 1110.0

# Do you wish to continue(Y/N)y
# ====== Employee Expense System ======
# 1. Add Travel Expense
# 2. Add Meal Expense
# 3. Add Miscellaneous Expense
# 4. View Total Reimbursement
# 5. Exit
# Choose choice:5
# Thank you! Have a great day.