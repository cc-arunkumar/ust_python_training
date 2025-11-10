# Cafeteria Billing System

total_amount = 0
item_count = 0

while True:
    print("\n====== UST Cafeteria ======")
    print("1. Coffee (₹25)")
    print("2. Sandwich (₹50)")
    print("3. Salad (₹40)")
    print("4. Juice (₹30)")
    print("5. View Bill")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        total_amount += 25
        item_count += 1
        print("Item added to bill!")
    elif choice == '2':
        total_amount += 50
        item_count += 1
        print("Item added to bill!")
    elif choice == '3':
        total_amount += 40
        item_count += 1
        print("Item added to bill!")
    elif choice == '4':
        total_amount += 30
        item_count += 1
        print("Item added to bill!")
    elif choice == '5':
        print(f"You ordered {item_count} items.")
        print(f"Total Bill Amount: ₹{total_amount:.2f}")
    elif choice == '6':
        print("Thank you for visiting UST Cafeteria!")
        break
    else:
        print("Invalid choice. Please try again.")

# ====== UST Cafeteria ======
# 1. Coffee (₹25)
# 2. Sandwich (₹50)
# 3. Salad (₹40)
# 4. Juice (₹30)
# 5. View Bill
# 6. Exit
# Enter your choice: 4
# Item added to bill!

# ====== UST Cafeteria ======
# 1. Coffee (₹25)
# 2. Sandwich (₹50)
# 3. Salad (₹40)
# 4. Juice (₹30)
# 5. View Bill
# 6. Exit
# Enter your choice: 4
# Item added to bill!

# ====== UST Cafeteria ======
# 1. Coffee (₹25)
# 2. Sandwich (₹50)
# 3. Salad (₹40)
# 4. Juice (₹30)
# 5. View Bill
# 6. Exit
# Enter your choice: 5
# You ordered 2 items.
# Total Bill Amount: ₹60.00

# ====== UST Cafeteria ======
# 1. Coffee (₹25)
# 2. Sandwich (₹50)
# 3. Salad (₹40)
# 4. Juice (₹30)
# 5. View Bill
# 6. Exit
# Enter your choice: 6
# Thank you for visiting UST Cafeteria!