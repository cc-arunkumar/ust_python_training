def ust_cafe():
    print("===== UST Cafeteria =====")
    print("1. Coffee ($25)")
    print("2. Sandwich ($50)")
    print("3. Salad ($40)")
    print("4. Juice ($30)")
    print("5. View Bill")
    print("6. Exit")
    total=0.00
    item=0
    while True:
        choice = int(input("Enter your choice: "))
        if(choice==1):
            item+=1
            total+=25
            print("Item added to bill!")
        elif(choice==2):
            item+=1
            total+=50
            print("Item added to bill!")
        elif(choice==3):
            item+=1
            total+=40
            print("Item added to bill!")
        elif(choice==4):
            item+=1
            total+=30
            print("Item added to bill!")
        elif(choice==5):
            print(f"You ordered {item} items")
            print("Total bill amount: ",total)
        elif(choice==6):
            print("Thank you for visiting UST Cafeteria!")
            break
        else:
            print("Invalid choice please enter valid choice.")
        print("")

ust_cafe()

# output

# ===== UST Cafeteria =====
# 1. Coffee ($25)
# 2. Sandwich ($50)
# 3. Salad ($40)
# 4. Juice ($30)
# 5. View Bill
# 6. Exit
# Enter your choice: 1
# Item added to bill!

# Enter your choice: 2
# Item added to bill!

# Enter your choice: 3
# Item added to bill!

# Enter your choice: 4
# Item added to bill!

# Enter your choice: 5
# You ordered 4 items
# Total bill amount:  145.0

# Enter your choice: 6
# Thank you for visiting UST Cafeteria!