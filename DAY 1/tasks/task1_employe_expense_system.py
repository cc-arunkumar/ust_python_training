"""
Task 1: Employee Expense Reimbursement Menu

Objective

Simulate a simple Employee Expense Management System used to calculate and track reimbursement claims.
Employees can record travel, meal, and miscellaneous expenses and get total reimbursement."""

print("Employee Expense System")
total_amount=0

while True:
    print("1. Add Travel Expense")
    print("2. Add Meal Expense")
    print("3. Add Miscellaneous Expense")
    print("4. View Total Reimbursement")
    print("5. Exit")

    choice=int(input("Enter Yor Choice: "))
    match choice:
        case 1:
            amount=float(input("Enter Travel Expenses Amount: "))
            total_amount+=amount
            print("Expenses added sucessfully")
        case 2:
            amount=float(input("Enter Meal Expenses Amount: "))
            total_amount+=amount
            print("Expenses added sucessfully")
        case 3:
            amount=float(input("Enter Miscellaneous Expenses Amount: "))
            total_amount+=amount
            print("Expenses added sucessfully")
        case 4:
            print(f"Total Reimbursement so far:  {total_amount}")
        case 5:
            print("Thank You! Have a great day")
            break
        case _:
            print("Enter options from 1-5")


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