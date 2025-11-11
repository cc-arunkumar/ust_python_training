print("=============EMPLOYEE EXPENSE SYSTEM=================")
print("1.Add Travel Expense")
print("2.Add Meal Expense")
print("3.Add Miscellaneous Expense")
print("4.View Total Reimbursement")
print("5.Exit")
total = 0
while True:
    Choice = int(input("Enter Your Choice : "))
    if (Choice == 1):
        travel_expense = int(input("Enter Travel Amount : "))
        total = total + travel_expense
    elif(Choice == 2):
        meal_expense = int(input("Enter Meal Expense : "))
        total = total + meal_expense
    elif(Choice == 3):
        misslaneous = int(input("Enter Misslaneous Expense : "))
        total = total + misslaneous
    elif(Choice == 4):
        print("Total Expense : " ,total)
    else:
        print("Thank You!")
        break
print("Thank you!")

    

