#Task 1 Employee Expense Reimbursement System
print("========Employee Expense System========")
print("1. Add Travel Expense")
print("2. Add Meal Expense")
print("3. Add Miscellaneous Expense")
print("4. View Total Reimbursement")
print("5. Exit")
total=0
choice=int(input("Enter your choice: "))
while(True):
    if(choice==1):
        travel_expense=float(input("Enter travel expense amount: "))
        total=total+travel_expense
        print("Expense added successfully")
    elif(choice==2):
        meal_expense=float(input("Enter meal expense amount: "))
        total=total+meal_expense
        print("Expense added successfully")
    elif(choice==3):
        miscellenous_amount=float(input("Enter Miscellaneous Expense: "))
        total=total+miscellenous_amount
        print("Expense added successfully")
    elif(choice==4):
        print("Total Reimbursement so far: ",total)
    else:
        break
    choice=int(input("Enter your choice: "))

print("Thank you! Have a great day.")

#sample execution
#========Employee Expense System========
#1. Add Travel Expense
#2. Add Meal Expense
#3. Add Miscellaneous Expense
#4. View Total Reimbursement
#5. Exit
#Enter your choice: 1
#Enter travel expense amount: 445
#Expense added successfully
#Enter your choice: 2
#Enter meal expense amount: 556
#Expense added successfully
#Enter your choice: 4
#Total Reimbursement so far:  1001.0
#Enter your choice: 5
#Thank you! Have a great day.

