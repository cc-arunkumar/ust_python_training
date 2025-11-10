# Task 1: Employee Expense Reimbursement Menu

total_exp = 0.0

print("====== Employee Expense System ======")
print("1. Add Travel Expense")
print("2. Add Meal Expense")
print("3. Add Miscellaneous Expense")
print("4. View Total Reimbursement")
print("5. Exit")

while True:
    choice = int(input("\nEnter your choice: "))

    match choice:
        case 1:
            amount = float(input("Enter travel expense amount: "))
            total_exp += amount
            print("Expense added successfully.")
            
        case 2:
            amount = float(input("Enter meal expense amount: "))
            total_exp += amount
            print("Expense added successfully.")
            
        case 3:
            amount = float(input("Enter miscellaneous expense amount: "))
            total_exp += amount
            print("Expense added successfully.")
            
        case 4:
            print(f"Total Reimbursement so far: ₹{total_exp:.2f}")
            
        case 5:
            print("Thank you! Have a great day.")
            break

# sample output
# ====== Employee Expense System ======
# 1. Add Travel Expense
# 2. Add Meal Expense
# 3. Add Miscellaneous Expense
# 4. View Total Reimbursement
# 5. Exit

# Enter your choice: 1
# Enter travel expense amount: 800
# Expense added successfully.

# Enter your choice: 2
# Enter meal expense amount: 250
# Expense added successfully.

# Enter your choice: 4
# Total Reimbursement so far: ₹1050.00

# Enter your choice: 5
# Thank you! Have a great day.