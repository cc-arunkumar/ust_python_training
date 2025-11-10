print("===== UST Cafeteria =====")
total_amount = 0.0
item_count = 0
while(True):
    print("1. Coffee($25)\n2. Sandwich($50\n3. ASalad($40)\n4. Juice($30)\n5. View bill\n6. Exit")
    choice = int(input("Enter choice: "))
    if(choice == 1):
        total_amount += 25
        item_count += 1
        print("Item added to bill.")
    elif(choice == 2):
        total_amount += 50
        item_count += 1
        print("Item added to bill.")
    elif(choice == 3):
        total_amount += 40
        item_count += 1
        print("Item added to bill.")
    elif(choice == 4):
        total_amount += 30
        item_count += 1
        print("Item added to bill.")
    elif(choice == 5):
        print("You orded ",item_count," items.")
    elif(choice == 6):
        break
    else:
        print("Invalid choice")
    print("\n")
print("Thank you for visiting UST cafeteria.")


# output

# ===== UST Cafeteria =====
# 1. Coffee($25)
# 2. Sandwich($50
# 3. ASalad($40)
# 4. Juice($30)
# 5. View bill
# 6. Exit
# Enter choice: 1
# Item added to bill.


# 1. Coffee($25)
# 2. Sandwich($50
# 3. ASalad($40)
# 4. Juice($30)
# 5. View bill
# 6. Exit
# Enter choice: 2
# Item added to bill.


# 1. Coffee($25)
# 2. Sandwich($50
# 3. ASalad($40)
# 4. Juice($30)
# 5. View bill
# 6. Exit
# Enter choice: 4
# Item added to bill.


# 1. Coffee($25)
# 2. Sandwich($50
# 3. ASalad($40)
# 4. Juice($30)
# 5. View bill
# 6. Exit
# Enter choice: 5
# You orded  3  items.


# 1. Coffee($25)
# 2. Sandwich($50
# 3. ASalad($40)
# 4. Juice($30)
# 5. View bill
# 6. Exit
# Enter choice: 6
# Thank you for visiting UST cafeteria.