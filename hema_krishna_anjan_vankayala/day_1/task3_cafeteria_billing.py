#Task 3: Cafeteria Billing System
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
# When a user selects an item,
# 	Display: "Item added to bill!"
# 	Add the item price to the running total.

# View Bill
# 	Show total bill amount so far and item count.

# Exit
# 	Display a thank-you message and stop the program.
	
	
# Sample Execution:
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

print("===== UST Cafeteria =====")
print("1. Coffee (Rs.25)")
print("2. Sandwitch (Rs.50)")
print("3. Salad (Rs.40)")
print("4. Juice (Rs.30)")
print("5. View Bill")
print("6. Exit")
total_amount = 0
no_of_items=0
while(True):

    value = int(input("Enter your choice: "))
    
    if value==1:
        total_amount += 25
        no_of_items += 1
        print(f"Item added to the bill")
    elif value==2:
        total_amount += 50
        no_of_items += 1
        print(f"Item added to the bill")
    elif value==3:
        total_amount += 40
        no_of_items += 1
        print(f"Item added to the bill")
    elif value==4:
        total_amount += 30
        no_of_items += 1
        print(f"Item added to the bill")
    elif value==5:
        print(f"You ordered {no_of_items} items.")
        print(f"Total Bill Amount: Rs. {float(total_amount)}")
    elif value==6:
        print("Thank you for visiting UST Cafe")
        break 
    else:
        print("Invalid Response!  Please Enter Correct Option")

#Sample Output
# ===== UST Cafeteria =====
# 1. Coffee (Rs.25)
# 2. Sandwitch (Rs.50)
# 3. Salad (Rs.40)
# 4. Juice (Rs.30)
# 5. View Bill
# 6. Exit
# Enter your choice: 1
# Item added to the bill
# Enter your choice: 2
# Item added to the bill
# Enter your choice: 3
# Item added to the bill
# Enter your choice: 5
# You ordered 3 items.
# Total Bill Amount: Rs. 115.0
# Enter your choice: 6
# Thank you for visiting UST Cafe