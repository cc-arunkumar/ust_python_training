def reimbursement():
    print(''' Travel Expense Reimbursement Form
          1.Add Travel Expense
          2.Add Meal Expense
          3.Add Miscellaneos Expense
          4.View Report
          5.Exit''')
    Choice = int(input("Enter your choice: "))
    total=0
    while(True):
        if Choice == 1:
            total+=int(input("Enter Travel Expense Amount: "))
        if Choice == 2:
            total+=int(input("Enter Meal Expense Amount: "))
        if Choice == 3:
            total+=int(input("Enter Miscellaneos Expense Amount: "))
        if Choice == 4:
         print(f"Total Expense Amount: {total}")
        if Choice == 5:
            print("Exiting the form.Thank you!")
            break
        Choice = int(input("Enter your choice: "))
    return
reimbursement()

#  Travel Expense Reimbursement Form
#           1.Add Travel Expense
#           2.Add Meal Expense
#           3.Add Miscellaneos Expense
#           4.View Report
#           5.Exit
# Enter your choice: 1
# Enter Travel Expense Amount: 12123
# Enter your choice: 3
# Enter Miscellaneos Expense Amount: 23424
# Enter your choice: 2
# Enter Meal Expense Amount: 32
# Enter your choice: 4
# Total Expense Amount: 35579
# Enter your choice: 5
# Exiting the form.Thank you!
