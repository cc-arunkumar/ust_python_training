total = 0.0
print("=====Employee Expense System ====")
print("1. Add Travel Expense")
print("2. Add Meal Expense")
print("3. Add Miscellaneous Expense")
print("4. View Total Reimbursement")
print("5. Exit ")
while True:
    

    n=int(input("Enter your choice:"))

    if n==1:
        travel=float(input("Enter travel expense amouny: "))
        total += travel
        print("Expense added successfully.")
    elif n==2:
        meal = float(input("Enter meal expense amount: "))
        total += meal
        print("Expense added successfully.")
    elif n == 3:
        miss = float(input("Enter miscellaneous expense amount:"))
        total += miss
    elif n == 4:
        print("Total Reimbursement so far: ₹", total)
    elif n == 51:
        print("Thank you! Have a great day.")
        break

# =====Employee Expense System ====
# 1. Add Travel Expense
# 2. Add Meal Expense
# 3. Add Miscellaneous Expense
# 4. View Total Reimbursement
# 5. Exit
# Enter your choice:1
# Enter travel expense amouny: 3456
# Expense added successfully.
# Enter your choice:2
# Enter meal expense amount: 345
# Expense added successfully.
# Enter your choice:3
# Enter miscellaneous expense amount:45
# Enter your choice:4
# Total Reimbursement so far: ₹ 3846.0
# Enter your choice:5
# Thank you! Have a great day.