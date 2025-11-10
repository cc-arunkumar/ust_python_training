#Employee Expense Reimbursement Menu
print("Employee Expense Reimbursement Menu")

print("\nOptions:")
print("1.Add travel expense")
print("2.Add meal expense")
print("3.Add miscellaneous expense")
print("4.View total Reimbursement")
print("5.Exit")

travel_expense = 0
meal_expense = 0
miscellaneous_expense = 0

while True:
    choice = input("Enter your choice: ")
    match choice:
        case "1":
            amt = float(input("Enter travel expense amount: "))
            travel_expense += amt
            print("Expense added successfully")
                
        case "2":                    
            amt = float(input("Enter meal expense amount: "))
            meal_expense += amt
            print("Expense added successfully")
    
        case "3":
            amount = float(input("Enter miscellaneous expense amount: "))
            miscellaneous_expense += amt
            print("Expense added successfully")
                
        case "4":
            total = travel_expense + meal_expense + miscellaneous_expense
            print(f"\nTotal Reimbursement so far: ₹{total}\n")
        case "5":
            print("Thankyou! have a great day!")
            break
        case "_":
            print("Invalid input")

'''
output:
Employee Expense Reimbursement Menu

Options:
1.Add travel expense
2.Add meal expense
3.Add miscellaneous expense
4.View total Reimbursement
5.Exit
Enter your choice: 1
Enter travel expense amount: 1200
Expense added successfully
Enter your choice: 2 
Enter meal expense amount: 1500
Expense added successfully
Enter your choice: 3
Enter miscellaneous expense amount: 245
Expense added successfully
Enter your choice: 4

Total Reimbursement so far: ₹4200.0

Enter your choice: 5
Thankyou! have a great day!
'''