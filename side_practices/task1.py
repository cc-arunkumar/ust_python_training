# task-1 employee expense reimbursement
print("====== Employee Expense System ======")
print("1. Add Travel Expense")
print("2. Add Meal Expense")
print("3. Add Miscellaneous Expense")
print("4. View Total Reimbursement")
print("5. Exit")
tot = 0
while True:

    choice = int(input("Enter Your Choice:"))
    if(choice==1):
        travel_amount = int(input("Enter travel expense amount:"))
        tot += travel_amount
        print("Expense added successfully.\n")
    elif(choice==2):
        meal_amount = int(input("Enter meal expense amount:"))
        tot += meal_amount
        print("Expense added successfully.\n")
    elif(choice==3):
        Miscellaneous_amount = int(input("Enter Miscellaneous expense amount:"))
        tot += Miscellaneous_amount
        print("Expense added successfully.\n")
    elif(choice==4):
        print(f"Total Reimbursement so far: ₹{tot:.2f}")
    elif(choice==5):
        print("Thank you! Have a great day.\n")
        break
    else:
        print("!Enter valid option\n")
     
     

