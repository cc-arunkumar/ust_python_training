# Task 3: Cafeteria Billing System
# Objective
# Simulate a Cafeteria Menu Ordering System for employees inside the office campus. Employees can order multiple items and get a running total of their bill.

#ust_cafeteria
print("====== UST Cafeteria ======")
print("1.Coffe (₹25)")
print("2.Sandwich (₹50)")
print("3.salad (₹30)")
print("4.Juice (₹75)")
print("5.View Bill")
print("6.Exit")
tot = 0
count = 0

while True:
    n = int(input("Enter Your Choice:"))
    if(n==1):
        print("Item Added to Bill!\n")
        tot += 25
        count += 1
    elif(n==2):
        print("Item Added to Bill!\n")
        tot += 50
        count += 1
    elif(n==3):
        print("Item Added to Bill!\n")
        tot += 30
        count += 1
    elif(n==4):
        print("Item Added to Bill!\n")
        tot += 75
        count += 1
    elif(n==5):
        print(f"You Ordered {count} Items.")
        print(f"Total Bill Amount is:₹{tot :.2f}")
    elif(n==6):
        print("ThankYou for Visiting Cafeteria")
        break
    else:
        print("!Enter V1alid Option")

# sample output:
# ====== UST Cafeteria ======
# 1.Coffe (₹25)
# 2.Sandwich (₹50)
# 3.salad (₹30)
# 4.Juice (₹75)
# 5.View Bill
# 6.Exit
# Enter Your Choice:1
# Item Added to Bill!

# Enter Your Choice:2
# Item Added to Bill!

# Enter Your Choice:3
# Item Added to Bill!

# Enter Your Choice:4
# Item Added to Bill!

# Enter Your Choice:5
# You Ordered 4 Items.
# Total Bill Amount is:₹180.00
# Enter Your Choice:6
# ThankYou for Visiting Cafeteria
