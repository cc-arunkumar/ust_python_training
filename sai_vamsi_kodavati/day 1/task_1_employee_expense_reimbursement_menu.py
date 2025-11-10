# TASK 1 - Employee Expense Reimbursement Menu
print("Hello")
total = 0
print("1.Travel Expense")
print("2.Meal Expense")
print("3.Miscellaneous Expense")
print("4.View total Reimbursement ")
print("5.Thank You! Have a nice day")

while True:
    choice = int(input("Enter your choice: "))

    if choice in [1,2,3]:
        expense = int(input("Enter the Expense: "))
        total+=expense
        print("Expense added successfully")

    elif(choice == 4):
        print("Total Expense so far: ", total)

    elif(choice == 5):
        print("Thank You! Have a nice day")
        

    else:
        print("Invalid choice")
        break


# Sample Output

# Hello
# 1.Travel Expense
# 2.Meal Expense
# 3.Miscellaneous Expense
# 4.View total Reimbursement
# 5.Thank You! Have a nice day
# Enter your choice: 1
# Enter the Expense: 100
# Expense added successfully
# Enter your choice: 2
# Enter the Expense: 200
# Expense added successfully
# Enter your choice: 3
# Enter the Expense: 300
# Expense added successfully
# Enter your choice: 4
# Total Expense so far:  600
# Enter your choice: 5
# Thank You! Have a nice day
# Enter your choice: 6
# Invalid choice
         





    




