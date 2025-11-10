#Task 1: Employee Reimbursement Menu

#Code ...
print("====Employee Expence System=====")
print("1. Add Travel Expense")
print("2. Add Meal Expense")
print("3. Add Miscellaneous Expense")
print("4. View Total Reimbursement")
print("5. Exit")

choice = int(input("Enter Your Choice : "))
total_reimbursement=0

while(True):
    if(choice==1):
        travel_exp=int(input("Enter Your travel Expense : "))
        total_reimbursement=total_reimbursement+travel_exp
        print("Expense added successfully")
    elif(choice ==2):
        meal_exp=int(input("Enter Your meal Expense : "))
        total_reimbursement=total_reimbursement+meal_exp
        print("Expense added successfully")
    elif(choice==3):
        miscellaneous_exp=int(input("Enter Your Miscellaneous Expense : "))
        total_reimbursement=total_reimbursement+miscellaneous_exp
        print("Expense added successfully")
    elif(choice==4):
        print("Total Reimbursement",total_reimbursement)
    else:
        break
    choice= int(input("Enter Your Choice : "))

print("Stop the program!!!")

#Sample Output
# ====Employee Expence System=====
# 1. Add Travel Expense
# 2. Add Meal Expense
# 3. Add Miscellaneous Expense
# 4. View Total Reimbursement
# 5. Exit

# Enter Your Choice : 1
# Enter Your travel Expense : 300
# Expense added successfully
# Enter Your Choice : 3
# Enter Your Miscellaneous Expense : 300
# Expense added successfully
# Enter Your Choice : 2
# Enter Your meal Expense : 200
# Expense added successfully
# Enter Your Choice : 4
# Total Reimbursement 800
# Enter Your Choice : 5
# Stop the program!!!
        
