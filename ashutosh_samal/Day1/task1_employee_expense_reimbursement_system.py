#Task1: Employee Expense Reimbursement System

#Code
print("====== Employee Expense System ======")
print("1. Add Travael Expense")
print("2. Add Meal Expense")
print("3. Add Miscellaneous Expense")
print("4. View Total Reimbursement")
print("5. Exit")
total_reimbursement = 0

while True:
    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            trav_exp = float(input("Enter travel expense amount: "))
            total_reimbursement=total_reimbursement+trav_exp
            print("Expense added seccessfully.")
        case 2:
            meal_exp = float(input("Enter meal expense amount: "))
            total_reimbursement=total_reimbursement+meal_exp
            print("Expense added seccessfully.")
        case 3:
            misc_exp = float(input("Enter miscellaneous expense amount: "))
            total_reimbursement=total_reimbursement+misc_exp
            print("Expense added seccessfully.")
        case 4:
            print("Total Reimbursement so far: ",total_reimbursement)
        case 5:
            print("Thank you! Have a great day.")
            break
        case _:
            print("Wrong Choice")



#Sample Execution

# ====== Employee Expense System ======
# 1. Add Travael Expense
# 2. Add Meal Expense
# 3. Add Miscellaneous Expense
# 4. View Total Reimbursement
# 5. Exit
# Enter your choice: 1
# Enter travel expense amount: 5000
# Expense added seccessfully.
# Enter your choice: 2
# Enter meal expense amount: 600
# Expense added seccessfully.
# Enter your choice: 3
# Enter miscellaneous expense amount: 400
# Expense added seccessfully.
# Enter your choice: 4
# Total Reimbursement so far:  6000.0
# Enter your choice: 5
# Thank you! Have a great day