#Task 1: Employee Expense Reimbursement Menu
#Simulate a simple Employee Expense Management System used to calculate and track reimbursement claims.
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
	
# Sample Execution:
# =================
# ====== Employee Expense System ======
# 1. Add Travel Expense
# 2. Add Meal Expense
# 3. Add Miscellaneous Expense
# 4. View Total Reimbursement
# 5. Exit
# Enter your choice: 1
# Enter travel expense amount: 800
# Expense added successfully.

# Enter your choice: 2
# Enter meal expense amount: 250
# Expense added successfully.

# Enter your choice: 4
# Total Reimbursement so far: ₹1050.00

# Enter your choice: 5
# Thank you! Have a great day.

print("===== Employee Expense System =====")
print("1.Add Travel Expense")
print("2.Add Meal Expense")
print("3.Add Miscellaneous Expense")
print("4. View Total Reimbursement")
print("5. Exit")
total_amount =0
while(True):

    value = int(input("Enter your choice: "))
    
    if value==1:
        travel_amount = int(input("Enter the Travel Amount:"))
        total_amount += travel_amount 
        print(f"Travel Amount of {travel_amount} Sucessfully Added!")
    elif value==2:
        meals_amount = int(input("Enter the Meals Amount:"))
        total_amount += meals_amount
        print(f"Meals Amount of {meals_amount} Sucessfully Added!")
    elif value==3:
        small_expenses_amount = int(input("Enter Other Small Expense Amount:"))
        total_amount += small_expenses_amount
        print(f"Miscellaneous Amount of {small_expenses_amount} Sucessfully Added!")
    elif value==4:
        print("Total Reimbursement so far: Rs." + str(float(total_amount)))
    elif value==5:
        print("Thank you! Have a Great Day")
        break 
    else:
        print("Invalid Response!  Please Enter Correct Option")


# Sample Output:
# ===== Employee Expense System =====
# 1.Add Travel Expense
# 2.Add Meal Expense
# 3.Add Miscellaneous Expense
# 4. View Total Reimbursement
# 5. Exit

# Enter your choice: 1
# Enter the Travel Amount:250
# Travel Amount of 250 Sucessfully Added!

# Enter your choice: 2
# Enter the Meals Amount:250
# Meals Amount of 250 Sucessfully Added!

# Enter your choice: 4
# Total Reimbursement so far: Rs.500.0

# Enter your choice: 5
# Thank you! Have a Great Day