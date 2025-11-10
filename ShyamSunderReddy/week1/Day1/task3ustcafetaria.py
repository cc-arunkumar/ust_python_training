#Task 3: Cafeteria Billing System
total=0
while(True):
    print("====== UST Csfetaria ======")
    print("1. Coffee (₹25)")
    print("2. Sandwich (₹50)")
    print("3. Salad(₹40)")
    print("4. Juice(₹30)")
    print("5. View Bill")
    print("6. Exit")
    n=int(input("Enter your choice: "))
    
    if(n==1):
        total=total+25
    elif(n==2):
        total=total+50
    elif(n==3):
        total=total+40
    elif(n==4):
        total=total+30
    elif(n==5):
        print(f"Total bill amount: {total}")
    elif(n==6):
        print("Thank you for visiting UST Cafeteria!")
        break
    else:
        print("Enter proper choice")

#Sample output
# ====== UST Csfetaria ======
# 1. Coffee (₹25)
# 2. Sandwich (₹50)
# 3. Salad(₹40)
# 4. Juice(₹30)
# 5. View Bill
# 6. Exit
# Enter your choice: 1
# ====== UST Csfetaria ======
# 1. Coffee (₹25)
# 2. Sandwich (₹50)
# 3. Salad(₹40)
# 4. Juice(₹30)
# 5. View Bill
# 6. Exit
# Enter your choice: 3
# ====== UST Csfetaria ======
# 1. Coffee (₹25)
# 2. Sandwich (₹50)
# 3. Salad(₹40)
# 4. Juice(₹30)
# 5. View Bill
# 6. Exit
# Enter your choice: 5
# Total bill amount: 65
# ====== UST Csfetaria ======
# 1. Coffee (₹25)
# 2. Sandwich (₹50)
# 3. Salad(₹40)
# 4. Juice(₹30)
# 5. View Bill
# 6. Exit
# Enter your choice: 6
# Thank you for visiting UST Cafeteria!