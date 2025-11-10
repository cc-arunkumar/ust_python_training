#Simulate a Cafeteria Menu Ordering System for employees inside the office campus. 
# #Employees can order multiple items and get a running total of their bill.


menu = {
    '1': ('Coffee', 25),
    '2': ('Sandwich', 50),
    '3': ('Salad', 40),
    '4': ('Juice', 30)
}
total_bill = 0
item_count = 0
while True:
    print("UST Cafeteria")
    print("1. Coffee (₹25)")
    print("2. Sandwich (₹50)")
    print("3. Salad (₹40)")
    print("4. Juice (₹30)")
    print("5. View Bill")
    print("6. Exit")
    choice = input("Enter your choice: ")
    if choice in menu:
        item_name, item_price = menu[choice]
        total_bill += item_price
        item_count += 1
        print("Item added to bill!")
    elif choice == '5':
        print(f"You ordered {item_count} items.")
        print(f"Total Bill Amount: ₹{total_bill:.2f}")
    elif choice == '6':
        print("Thank you for visiting UST Cafeteria!")
        break
    else:
        print("Invalid choice. Please try again.")

#sample execution
# UST Cafeteria
# 1. Coffee (₹25)
# 2. Sandwich (₹50)
# 3. Salad (₹40)
# 4. Juice (₹30)
# 5. View Bill
# 6. Exit
# Enter your choice: 5
# You ordered 0 items.
# Total Bill Amount: ₹0.00
# UST Cafeteria
# 1. Coffee (₹25)
# 2. Sandwich (₹50)
# 3. Salad (₹40)
# 4. Juice (₹30)
# 5. View Bill
# 6. Exit
# Enter your choice: 2
# Item added to bill!
# UST Cafeteria
# 1. Coffee (₹25)
# 2. Sandwich (₹50)
# 3. Salad (₹40)
# 4. Juice (₹30)
# 5. View Bill
# 6. Exit
# Enter your choice: 5
# You ordered 1 items.
# Total Bill Amount: ₹50.00
# UST Cafeteria
# 1. Coffee (₹25)
# 2. Sandwich (₹50)
# 3. Salad (₹40)
# 4. Juice (₹30)
# 5. View Bill
# 6. Exit
# Enter your choice: