# Task 3: Cafeteria Billing System
total_bill=0
menu={
    "coffee":{"price":25,"count":0},
    "sandwich":{"price":50,"count":0},
    "salad":{"price":40,"count":0},
    "juice":{"price":30,"count":0}
}
ch='Y'
while(ch=='Y' or ch=='y'):
    print("====== UST Cafeteria ======")
    print("1. Coffee (Rs.25)")
    print("2. Sandwich (Rs.50)")
    print("3. Salad (Rs.40)")
    print("4. Juice (Rs.30)")
    print("5. View Bill")
    print("6. Exit")
    n=int(input("Choose choice:"))
    if(n==1):
        total_bill+=menu["coffee"]["price"]
        menu["coffee"]["count"]+=1
        print("Item added to bill!")
    elif(n==2):
        total_bill+=menu["sandwich"]["price"]
        menu["sandwich"]["count"]+=1
        print("Item added to bill!")
    elif(n==3):
        total_bill+=menu["salad"]["price"]
        menu["salad"]["count"]+=1
        print("Item added to bill!")
    elif(n==4):
        total_bill+=menu["juice"]["price"]
        menu["juice"]["count"]+=1
        print("Item added to bill!")
    elif(n==5):
        print("You Ordered:")
        print(f"{menu["coffee"]["count"]}xCoffee") if menu["coffee"]["count"]>0 else ""
        print(f"{menu["sandwich"]["count"]}xSandwich") if menu["sandwich"]["count"]>0 else ""
        print(f"{menu["salad"]["count"]}xSalad") if menu["salad"]["count"]>0 else ""
        print(f"{menu["juice"]["count"]}xJuice") if menu["juice"]["count"]>0 else ""
        print(f"Total Bill Amount : {total_bill}")
    elif(n==6):
        print("Thank you for visiting UST Cafeteria!")
        break
    else:
        print("Provide a number within range!!")
    ch=input("\nDo you wish to continue(Y/N)")
#Output
# ====== UST Cafeteria ======
# 1. Coffee (Rs.25)
# 2. Sandwich (Rs.50)
# 3. Salad (Rs.40)
# 4. Juice (Rs.30)
# 5. View Bill
# 6. Exit
# Choose choice:1
# Item added to bill!

# Do you wish to continue(Y/N)y
# ====== UST Cafeteria ======
# 1. Coffee (Rs.25)
# 2. Sandwich (Rs.50)
# 3. Salad (Rs.40)
# 4. Juice (Rs.30)
# 5. View Bill
# 6. Exit
# Choose choice:2
# Item added to bill!

# Do you wish to continue(Y/N)y
# ====== UST Cafeteria ======
# 1. Coffee (Rs.25)
# 2. Sandwich (Rs.50)
# 3. Salad (Rs.40)
# 4. Juice (Rs.30)
# 5. View Bill
# 6. Exit
# Choose choice:3
# Item added to bill!

# Do you wish to continue(Y/N)y
# ====== UST Cafeteria ======
# 1. Coffee (Rs.25)
# 2. Sandwich (Rs.50)
# 3. Salad (Rs.40)
# 4. Juice (Rs.30)
# 5. View Bill
# 6. Exit
# Choose choice:4
# Item added to bill!

# Do you wish to continue(Y/N)y
# ====== UST Cafeteria ======
# 1. Coffee (Rs.25)
# 2. Sandwich (Rs.50)
# 3. Salad (Rs.40)
# 4. Juice (Rs.30)
# 5. View Bill
# 6. Exit
# Choose choice:5
# You Ordered:
# 1xCoffee
# 1xSandwich
# 1xSalad
# 1xJuice
# Total Bill Amount : 145

# Do you wish to continue(Y/N)y
# ====== UST Cafeteria ======
# 1. Coffee (Rs.25)
# 2. Sandwich (Rs.50)
# 3. Salad (Rs.40)
# 4. Juice (Rs.30)
# 5. View Bill
# 6. Exit
# Choose choice:6
# Thank you for visiting UST Cafeteria!