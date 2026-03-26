"""
Task 1: Employee Expense Reimbursement Menu

Objective

Simulate a simple Employee Expense Management System used to calculate and track reimbursement claims.
Employees can record travel, meal, and miscellaneous expenses and get total reimbursement."""

print("Employee Expense System")   # Display system title
total_amount=0   # Variable to store total reimbursement amount

while True:   # Infinite loop for continuous menu display
    print("1. Add Travel Expense")
    print("2. Add Meal Expense")
    print("3. Add Miscellaneous Expense")
    print("4. View Total Reimbursement")
    print("5. Exit")

    choice=int(input("Enter Yor Choice: "))   # Take user's menu choice
    match choice:   # Match-case for selecting menu option
        case 1:
            amount=float(input("Enter Travel Expenses Amount: "))   # Input travel expense
            total_amount+=amount   # Add expense to total
            print("Expenses added sucessfully")
        case 2:
            amount=float(input("Enter Meal Expenses Amount: "))   # Input meal expense
            total_amount+=amount   # Add expense to total
            print("Expenses added sucessfully")
        case 3:
            amount=float(input("Enter Miscellaneous Expenses Amount: "))   # Input misc expense
            total_amount+=amount   # Add expense to total
            print("Expenses added sucessfully")
        case 4:
            print(f"Total Reimbursement so far:  {total_amount}")   # Show total reimbursement
        case 5:
            print("Thank You! Have a great day")   # Exit message
            break   # Exit loop
        case _:
            print("Enter options from 1-5")   # Invalid input message


# SAMPLE OUTPUT

"""Employee Enpense System
1. Add Travel Expense
2. Add Meal Expense
3. Add Miscellaneous Expense
4. View Total Reimbursement
5. Exit
Enter Yor Choice: 1
Enter Travel Expenses Amount: 1000
Expenses added sucessfully
1. Add Travel Expense
2. Add Meal Expense
3. Add Miscellaneous Expense
4. View Total Reimbursement
5. Exit
Enter Yor Choice: 2
Enter Meal Expenses Amount: 500
Expenses added sucessfully
1. Add Travel Expense
2. Add Meal Expense
3. Add Miscellaneous Expense
4. View Total Reimbursement
5. Exit
Enter Yor Choice: 4
Total Reimbursement so far:  1500.0
1. Add Travel Expense
2. Add Meal Expense
3. Add Miscellaneous Expense
4. View Total Reimbursement
5. Exit
Enter Yor Choice: 5
Thank You! Have a great day"""
