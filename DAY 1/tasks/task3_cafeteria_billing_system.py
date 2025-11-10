"""
 Cafeteria Billing System
 
Objective
	Simulate a Cafeteria Menu Ordering System for employees inside the office campus. Employees can order multiple items and get a running total of their bill.
	

"""


print("UST Cafeteria")
total_bill,count=0,0
while True:
    print("1. Coffee ($25)")
    print("2. Sandwich ($50)")
    print("3. Salad ($40)")
    print("4. Juice ($30)")
    print("5. View Bill")
    print("6. Exit")

    choice=int(input("Enter Your Choice: "))
    match choice:
        case 1:
            print("Item Added To Bill")
            total_bill+=25
            count+=1
        case 2:
            print("Item Added To Bill")
            total_bill+=50
            count+=1
        case 3:
            print("Item Added To Bill")
            total_bill+=40
            count+=1
        case 4:
            print("Item Added To Bill")
            total_bill+=30
            count+=1
        case 5:
            print(f"You Ordered {count} items")
            print(f"Total Bill Amount: ${total_bill}")
        case 6:
            print("Thanks For Visiting UST Cafeteria")
            break
        case _:
            print("Enter Number from 1-6")


# SAMPLE OUTPUT

"""
Employee Enpense System
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