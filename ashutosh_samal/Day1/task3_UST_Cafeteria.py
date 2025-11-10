#Task3: UST Cafeteria

#Code
print("====== UST Cafeteria ======")
print("1. Coffee (RS25)")
print("2. Sandwich (RS50)")
print("3. Salad (RS40)")
print("4. Juice (RS30)")
print("5. View Bill")
print("6. Exit")

total_item_count=0
total_cost=0
while True:
    choice = int(input("Enter your choice: "))

    if(choice == 1):
        total_item_count += 1
        total_cost += 25
        print("Item added to bill!")
    elif(choice == 2):
        total_item_count += 1
        total_cost += 50
        print("Item added to bill!")
    elif(choice == 3):
        total_item_count += 1
        total_cost += 40
        print("Item added to bill!")
    elif(choice == 4):
        total_item_count += 1
        total_cost += 30
        print("Item added to bill!")
    elif(choice == 5):
        print("You ordered ", total_item_count," items")
        print("Total Bill: ",total_cost)
    elif(choice == 6):
        print("Thankyou for visiting UST Cafeteria")
        break


#Sample Execution
# ====== UST Cafeteria ======
# 1. Coffee (RS25)
# 2. Sandwich (RS50)
# 3. Salad (RS40)
# 4. Juice (RS30)
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
# You ordered  4  items
# Total Bill:  145
# Enter your choice: 6
# Thankyou for visiting UST Cafeteria