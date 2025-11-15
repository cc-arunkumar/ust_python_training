# Task 1: Employee Expense Reimbursement Menu
# Objective

# Simulate a simple Employee Expense Management System used to calculate and track reimbursement claims.
# Employees can record travel, meal, and miscellaneous expenses and get total reimbursement.

print("============Employee Expense System==============")
print("1. Add Travel Expense")
print("2. Add Meal Expense")
print("3. Add Miscellaneous Expense")
print("4. View Total Reimbursement ")
print("5. Exit")


sum=0
while(True):
    choice=int(input("enter the choice: "))
    
    if(choice<1 or choice >5):
        print("Enter the number between 1 to 5")
        
    elif (choice==1):
        Travel_expense=int(input("enter Travel expenses: "))
        sum+=Travel_expense
        
    elif(choice==2):
        Meal_expense=int(input("enter Teal expense: "))
        sum+=Meal_expense
        
    elif(choice==3):
        Misc_expense=int(input("enter Miscellaneous expenses: "))
        sum+=Misc_expense
        
    elif(choice==4):
        print(sum)
        
    elif(choice==5):
        break

#     ============Employee Expense System==============
# 1. Add Travel Expense
# 2. Add Meal Expense
# 3. Add Miscellaneous Expense
# 4. View Total Reimbursement 
# 5. Exit
# enter the choice: 1
# enter Travel expenses: 100
# enter the choice: 2
# enter Teal expense: 100
# enter the choice: 3
# enter Miscellaneous expenses: 100
# enter the choice: 4
# 300
# enter the choice: 5
    

