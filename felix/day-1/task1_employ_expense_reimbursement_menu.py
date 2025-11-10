# Employee Expense system

total = 0.0
print("=====Employee Expense system=====")
while(True):
    print("1. Add Travel Expense\n2. Add Meal Expense\n3. Add Miscellaneous Expense\n4. View Total Reimbursement\n5. Exit")
    choice = int(input("Enter choice: "))
    if(choice == 1):
        total += float(input("Enter travel expense amount: "))
        print("Expense added successfully.")
    elif(choice == 2):
        total += float(input("Enter meal expense amount: "))
        print("Expense added successfully.")
    elif(choice == 3):
        total += float(input("Enter Miscellaneous Expense amount: "))
        print("Expense added successfully.")
    elif(choice == 4):
        print("Totla Reimbursement so far: ",total)
    elif(choice == 5):
        break
    else:
        print("Invalid choice")
    print("\n")
print("Thanku have a great day.")

# output

# =====Employee Expense system=====
# 1. Add Travel Expense
# 2. Add Meal Expense
# 3. Add Miscellaneous Expense
# 4. View Total Reimbursement
# 5. Exit
# Enter choice: 1
# Enter travel expense amount: 200
# Expense added successfully.


# 1. Add Travel Expense
# 2. Add Meal Expense
# 3. Add Miscellaneous Expense
# 4. View Total Reimbursement
# 5. Exit
# Enter choice: 2
# Enter meal expense amount: 300
# Expense added successfully.


# 1. Add Travel Expense
# 2. Add Meal Expense
# 3. Add Miscellaneous Expense
# 4. View Total Reimbursement
# 5. Exit
# Enter choice: 3
# Enter Miscellaneous Expense amount: 267
# Expense added successfully.


# 1. Add Travel Expense
# 2. Add Meal Expense
# 3. Add Miscellaneous Expense
# 4. View Total Reimbursement
# 5. Exit
# Enter choice: 4
# Totla Reimbursement so far:  767.0


# 1. Add Travel Expense
# 2. Add Meal Expense
# 3. Add Miscellaneous Expense
# 4. View Total Reimbursement
# 5. Exit
# Enter choice: 5
# Thanku have a great day.

