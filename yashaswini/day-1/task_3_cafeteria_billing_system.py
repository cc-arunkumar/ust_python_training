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

menu = {'1': ('Coffee', 25),'2': ('Sandwich', 50),'3': ('Salad', 40),'4': ('Juice', 30)}
total_amount=0
item_count=0
while True:
    print("UST Cafeteria")
    print("1.coffee (₹25)")
    print("2.sandwich (₹50)")
    print("3.salad (₹40)")
    print("4.juice (₹30)")
    print("5.view bill")
    print("6.exit")
    choice=input("enter your choice:")
    if choice in menu:
        item_name, item_price = menu[choice]
        total_amount+=item_price
        item_count+=1
        print("Item added to bill!")
    elif choice == '5':
        print(f"You ordered {item_count} items.")
        print(f"Total Bill Amount: ₹{total_amount:.2f}")
    elif choice == '6':
        print("Thank you for visiting UST Cafeteria!")
        break
    else:
        print("Invalid choice. Please try again.")


#o/p:
#UST Cafeteria
# 1.coffee (₹25)
# 2.sandwich (₹50)
# 3.salad (₹40)
# 4.juice (₹30)
# 5.view bill
# 6.exit
# enter your choice:5
# You ordered 0 items.
# Total Bill Amount: ₹0.00
# UST Cafeteria
# 1.coffee (₹25)
# 2.sandwich (₹50)
# 3.salad (₹40)
# 4.juice (₹30)
# 5.view bill
# 6.exit
# enter your choice:3
# Item added to bill!
# UST Cafeteria
# 1.coffee (₹25)
# 2.sandwich (₹50)
# 3.salad (₹40)
# 4.juice (₹30)
# 5.view bill
# 6.exit
# enter your choice:1
# Item added to bill!
# UST Cafeteria
# 1.coffee (₹25)
# 2.sandwich (₹50)
# 3.salad (₹40)
# 4.juice (₹30)
# 5.view bill
# 6.exit
# enter your choice:5
# You ordered 2 items.
# Total Bill Amount: ₹65.00
# UST Cafeteria
# 1.coffee (₹25)
# 2.sandwich (₹50)
# 3.salad (₹40)
# 4.juice (₹30)
# 5.view bill
# 6.exit
# enter your choice:6
# Thank you for visiting UST Cafeteria!