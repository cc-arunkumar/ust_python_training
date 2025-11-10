
#Task 1: Employee Expense Reimbursement Menu
# Objective

# Simulate a simple Employee Expense Management System used to calculate and track reimbursement claims.
# Employees can record travel, meal, and miscellaneous expenses and get total reimbursement.

print("===== Employee Expense System =====")
total=0
while True:
    print("1. Add Travel Expense")
    print("2. Add Meal Expense")
    print("3. Add Miscellaneous")
    print("4. View Total")
    print("5. Exit")
    a=int(input("Enter Your Choice: "))
   
    if a in [1,2,3]:
        expense=int(input("Enter Your Expense: "))
        total+=expense
        print("Expense added successfuly")

    elif(a==4):
        print(total,"Thank You")
        break
    elif(a==5):
        print("Thank You Have a good day")
    else:
        print("Invalid Number")




#Sample Output
# ===== Employee Expense System =====
# 1. Add Travel Expense
# 2. Add Meal Expense
# 3. Add Miscellaneous
# 4. View Total
# 5. Exit
# Enter Your Choice: 2
# Enter Your Expense: 300
# Expense added successfuly
# 1. Add Travel Expense
# 2. Add Meal Expense
# 3. Add Miscellaneous
# 4. View Total
# 5. Exit
# Enter Your Choice: 2
# Enter Your Expense: 200
# Expense added successfuly
# 1. Add Travel Expense
# 2. Add Meal Expense
# 3. Add Miscellaneous
# 4. View Total
# 5. Exit
# Enter Your Choice: 4
# 500 Thank You


