# Task 1: Employee Expense Reimbursement Menu


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



print("===== Employee Expense System =====")
print("1. Add Travel Expense")
print("2. Add Meal Expense")
print("3. Add Miscellaneos Expense")
print("4. View Total Reimbursement")
print("5. Exit")

travel=0
meal=0
miscellaneos=0
choice=int(input("Enter your choice: "))
while choice<=5:
    if choice==1:
        travel=float(input("Enter travel expense amount: "))
        print("Expense added successfully.")
    elif choice==2:
        meal=int(input("Enter meal expense amount: "))
        print("Expense added successfully")
    elif choice==3:
        miscellaneos=int(input("Enter miscellaneos expense amount: "))
        print("Expense added successfully")
    elif choice==4:
        total=travel+meal+miscellaneos
        print(f"Total Reimbursement so fal: ₹{total:.2f}")
    elif choice==5:
        print("Thank you! Have a great day.")
        break
    choice=int(input("Enter your choice: "))

# Sample Output

# ===== Employee Expense System =====
# 1. Add Travel Expense
# 2. Add Meal Expense
# 3. Add Miscellaneos Expense
# 4. View Total Reimbursement
# 5. Exit

# Enter your choice: 1

# Enter travel expense amount: 150
# Expense added successfully.

# Enter your choice: 3
# Enter miscellaneos expense amount: 200
# Expense added successfully

# Enter your choice: 4
# Total Reimbursement so fal: ₹350.00

# Enter your choice: 5
# Thank you! Have a great day.
