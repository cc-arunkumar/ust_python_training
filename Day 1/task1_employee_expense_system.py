# Task 1: Employee Expense Reimbursement Menu
# Objective

# Simulate a simple Employee Expense Management System used to calculate and track reimbursement claims.
# Employees can record travel, meal, and miscellaneous expenses and get total reimbursement.

print("====== Employee Expense System ======")
print("1.Add Travel Expense")
print("2.Add Meal Expense")
print("3.Add Miscellaneous Expense")
print("4.View Total Reimbursement")
print("5.Exit")

tot = 0.0

while True:
    n = int(input("Enter your Choice:"))
    if(n==1):
        travelAmount  = float(input("Enter Travel Expense Amount:"))
        print("Expense Amount Added Successfully.\n")
        tot += travelAmount
    elif(n==2):
        mealExpense = float(int(input("Enter Meal Expense Amount:")))
        print("Expense Amount Added Successfully.\n")
        tot += mealExpense
    elif(n==3):
        miscExpense = float(int(input("Enter misc Expense Amount:")))
        print("Expense Amount Added Successfully.\n")
        tot += miscExpense
    elif(n==4):
        print(f"total Reimbursement so far: {tot:.2f}\n")
    elif(n==5):
        print("Thank you! Have a Great Day")
        break

    else:
        print("Invalid Choice1")

# sample output

# ====== Employee Expense System ======
# 1.Add Travel Expense
# 2.Add Meal Expense
# 3.Add Miscellaneous Expense
# 4.View Total Reimbursement
# 5.Exit
# Enter your Choice:1
# Enter Travel Expense Amount:234
# Expense Amount Added Successfully.

# Enter your Choice:2
# Enter Meal Expense Amount:345
# Expense Amount Added Successfully.

# Enter your Choice:3
# Enter misc Expense Amount:345
# Expense Amount Added Successfully.

# Enter your Choice:4
# total Reimbursement so far: 924.00

# Enter your Choice:5
# Thank you! Have a Great Day



      