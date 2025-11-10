
print("===========Employee Expense System============")
print("Add travel expense enter 1")
print("Add Meal expense enter 2")
print("Add MiscellaneousExpense enter 3")
print("Total reimbursement 4")
print("Exit 5")
print("Choose between 1 to 5")

sum=0
while True:
    n = int(input("Enter the number "))
    if n==1:
         travelExpense = int(input("Enter travel expense "))
         sum+=travelExpense

    if n==2:
          MealExpense = int(input("Enter Meal expense "))
          sum+=MealExpense
    if n==3:
         MiscellaneousExpense = int(input("Enter Miscellaneous expense "))
         sum+=MiscellaneousExpense
    if n==4:
         print(sum)
    if n==5:
         break
    if n>5 or n<1:
         print("please choose between 1 to 5")

         


    
    
# ===========sample output================
# ===========Employee Expense System============
# Add travel expense enter 1      
# Add Meal expense enter 2        
# Add MiscellaneousExpense enter 3
# Total reimbursement 4
# Exit 5
# Choose between 1 to 5
# Enter the number 1
# Enter travel expense 2300
# Enter the number 1    
# Enter travel expense 2340
# Enter the number 2
# Enter Meal expense 345
# Enter the number 3
# Enter Miscellaneous expense 457
# Enter the number 4
# 5442
# Enter the number 5