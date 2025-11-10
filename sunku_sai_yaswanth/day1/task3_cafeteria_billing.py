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


print("=======UST Cafeteria=======")
coffee=0
sandwich=0
salad=0
juice=0
while True:
    print("1.coffee ₹25")
    print("2.sandwich ₹50")
    print("3.salad ₹40")
    print("4.juice ₹30")
    print("5.view bill")
    print("6.Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        coffee+=25
        print("item added to bill")
        
    elif choice==2:
        sandwich+=50
        print("item is added")
        
    elif choice==3:
        salad+=40
        print("item is added")
       
    elif choice==4:
        juice+=30
        print("item is added")
        
    elif choice==5:
        total=coffee+sandwich+salad+juice
        print(f"The total amount is ₹{total}")
    elif choice==6:
        print("Exit")
        break
    



# =======UST Cafeteria=======
# 1.coffee ₹25
# 2.sandwich ₹50
# 3.salad ₹40
# 4.juice ₹30
# 5.view bill
# 6.Exit
# Enter your choice:1
# item added to bill
# 1.coffee ₹25
# 2.sandwich ₹50
# 3.salad ₹40
# 4.juice ₹30
# 5.view bill
# 6.Exit
# Enter your choice:2
# item is added
# 1.coffee ₹25
# 2.sandwich ₹50
# 3.salad ₹40
# 4.juice ₹30
# 5.view bill
# 6.Exit
# Enter your choice:3
# item is added
# 1.coffee ₹25
# 2.sandwich ₹50
# 3.salad ₹40
# 4.juice ₹30
# 5.view bill
# 6.Exit
# Enter your choice:4
# item is added
# 1.coffee ₹25
# 2.sandwich ₹50
# 3.salad ₹40
# 4.juice ₹30
# 5.view bill
# 6.Exit
# Enter your choice:5
# The total amount is ₹145
# 1.coffee ₹25
# 2.sandwich ₹50
# 3.salad ₹40
# 4.juice ₹30
# 5.view bill
# 6.Exit
# Enter your choice:6
# Exit