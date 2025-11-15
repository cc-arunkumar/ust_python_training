# Cafeteria Billing System
# Task 3: Cafeteria Billing System
# Objective
# 	Simulate a Cafeteria Menu Ordering System for employees inside the office campus. Employees can order multiple items and get a running total of their bill.
	
# ====== UST Cafeteria ======
# 1. Coffee (₹25)
# 2. Sandwich (₹50)
# 3. Salad (₹40)
# 4. Juice (₹30)
# 5. View Bill
# 6. Exit
# Enter your choice:

# Functional Rules
# =================
# When a user selects an item,
# 	Display: "Item added to bill!"
# 	Add the item price to the running total.
# View Bill
# 	Show total bill amount so far and item count.
# Exit
# 	Display a thank-you message and stop the program.	
# total_amount = 0
# item_count = 0

# UST Cafeteria Menu Program

# Initialize variables to track bill
total_amount = 0
item_count = 0

# Infinite loop to keep showing menu until user exits
while True:
    # Display menu options
    print("\n====== UST Cafeteria ======")
    print("1. Coffee (₹25)")
    print("2. Sandwich (₹50)")
    print("3. Salad (₹40)")
    print("4. Juice (₹30)")
    print("5. View Bill")
    print("6. Exit")
    
    # Take user choice
    choice = input("Enter your choice: ")

    # Add Coffee
    if choice == '1':
        total_amount += 25
        item_count += 1
        print("Item added to bill!")

    # Add Sandwich
    elif choice == '2':
        total_amount += 50
        item_count += 1
        print("Item added to bill!")

    # Add Salad
    elif choice == '3':
        total_amount += 40
        item_count += 1
        print("Item added to bill!")

    # Add Juice
    elif choice == '4':
        total_amount += 30
        item_count += 1
        print("Item added to bill!")

    # View total bill
    elif choice == '5':
        print(f"You ordered {item_count} items.")
        print(f"Total Bill Amount: ₹{total_amount:.2f}")

    # Exit program
    elif choice == '6':
        print("Thank you for visiting UST Cafeteria!")
        break

    # Handle invalid input
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