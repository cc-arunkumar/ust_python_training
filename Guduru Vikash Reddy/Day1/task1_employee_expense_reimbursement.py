
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




total=0
while True:
   print("1.Enter Travel Expense")
   print("2.enter meal expense")
   print("3.Miscellaneous expense")
   print("4.view totals reimbursement")
   print("5.exit")
   choice=int(input("Enter a choice"))
   if choice==1:
      amount=float(input("Enter a Travel expense"))
      total+=amount
      print("Expenses addes successfully")
   elif choice==2:
      amount=float(input("enter a meal expense"))
      total+=amount
      print("Expenses addes successfully")
   elif choice==3:
      amount=float(input("enter a miscellaneous fee"))
      total+=amount
      print("Expenses addes successfully")
   elif choice==4:
      print(f"Total Reimbursement so far:{total:.2f}")
   elif choice==5:
      print("Thank you! have a great day.")
# sample output
# 1.Enter Travel Expense
# 2.enter meal expense
# 3.Miscellaneous expense
# 4.view totals reimbursement
# 5.exit
# Enter a choice: 1
# Enter a Travel expense: 1200.50
# Expenses addes successfully

# 1.Enter Travel Expense
# 2.enter meal expense
# 3.Miscellaneous expense
# 4.view totals reimbursement
# 5.exit
# Enter a choice: 2
# enter a meal expense: 350.75
# Expenses addes successfully

# 1.Enter Travel Expense
# 2.enter meal expense
# 3.Miscellaneous expense
# 4.view totals reimbursement
# 5.exit
# Enter a choice: 3
# enter a miscellaneous fee: 150.00
# Expenses addes successfully

# 1.Enter Travel Expense
# 2.enter meal expense
# 3.Miscellaneous expense
# 4.view totals reimbursement
# 5.exit
# Enter a choice: 4
# Total Reimbursement so far:1701.25

# 1.Enter Travel Expense
# 2.enter meal expense
# 3.Miscellaneous expense
# 4.view totals reimbursement
# 5.exit
# Enter a choice: 5
# Thank you! have a great day.