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
	
	
# Sample Execution
# -----------------

# ====== UST Cafeteria ======
# 1. Coffee (₹25)
# 2. Sandwich (₹50)
# 3. Salad (₹40)
# 4. Juice (₹30)
# 5. View Bill
# 6. Exit
# Enter your choice: 1
# Item added to bill!

# Enter your choice: 3
# Item added to bill!

# Enter your choice: 5
# You ordered 2 items.
# Total Bill Amount: ₹65.00

# Enter your choice: 6
# Thank you for visiting UST Cafeteria!

# Code

# Initialize total bill amount and item counter
total_amount = 0
item_count = 0

# Run the program until user chooses to exit
while True:
    # Display menu options
    print("1. Coffee = $25")
    print("2. Sandwich = $50")
    print("3. Salad = $40")
    print("4. Juice = $30")
    print("5. View bill")
    print("6. Exit")   # <-- corrected to show '6' for exit

    # Take user input
    choice = input("Enter your choice: ")

    # Check which option user selected
    if choice == '1':  # Coffee
        total_amount += 25
        item_count += 1
        print("Item added to bill")
    elif choice == '2':  # Sandwich
        total_amount += 50
        item_count += 1
        print("Item added to bill")
    elif choice == '3':  # Salad
        total_amount += 40
        item_count += 1
        print("Item added to bill")
    elif choice == '4':  # Juice
        total_amount += 30
        item_count += 1
        print("Item added to bill")
    elif choice == '5':  # Show bill summary
        print(f"You ordered {item_count} items")
        # Use f-string correctly to display total amount
        print(f"Total bill amount: {total_amount:.2f}")
    elif choice == '6':  # Exit program
        print("Thank you for visiting\nUST cafeteria")
        break
    else:  # Invalid input
        print("Invalid choice. Please try again.")

#output
# PS C:\Users\303379\day1_training> & C:/Users/303379/AppData/Local/Microsoft/WindowsApps/python3.13.exe c:/Users/303379/day1_training/task3.py
# 1.coffee=$25
# 2.sandwich=$50
# 3.salad=$40
# 4.juice=$30
# 5.view bill
# exit
# enter your choice:1
# Item added to bill
# 1.coffee=$25
# 2.sandwich=$50
# 3.salad=$40
# 4.juice=$30
# 5.view bill
# exit
# enter your choice:2
# Item added to bill
# 1.coffee=$25
# 2.sandwich=$50
# 3.salad=$40
# 4.juice=$30
# 5.view bill
# exit
# enter your choice:3
# Item added to bill
# 1.coffee=$25
# 2.sandwich=$50
# 3.salad=$40
# 4.juice=$30
# 5.view bill
# exit
# enter your choice:4
# Item added to bill
# 1.coffee=$25
# 2.sandwich=$50
# 3.salad=$40
# 4.juice=$30
# 5.view bill
# exit
# enter your choice:5
# you odered 4 items
# total bill amount:{total_amount:.2f}
# 1.coffee=$25
# 2.sandwich=$50
# 3.salad=$40
# 4.juice=$30
# 5.view bill
# exit
# enter your choice:6
# thank you for visiting
# UST cafeteria
# PS C:\Users\303379\day1_training> 