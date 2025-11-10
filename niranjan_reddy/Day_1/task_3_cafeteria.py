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


print("1. Coffee (₹25)")
print("2. Sandwich (₹50)")
print("3. Salad (₹40)")
print("4. Juice (₹30)")
print("5. View Bill")
print("6. Exit")

item=0
total=0

choice =int(input("Enter your choice: "))

while choice<=6:
    if choice==1:
        print("Item added to bill!")
        item+=1
        total+=25
    elif choice==2:
        print("Item added to bill!")
        item+=1
        total+=50
    elif choice==3:
        print("Item added to bill!")
        item+=1
        total+=40
    elif choice==4:
        print("Item added to bill!")
        item+=1
        total+=30
    elif choice==5:
        print(f"Your ordered {item} items")
        print(f"Total Bill Amount: ₹{total:.2f}")
    else:
        print("Thank you for visiting UST Cafeteria!")
        break
    choice =int(input("Enter your choice: "))
    
# Sample output

# 1. Coffee (₹25)
# 2. Sandwich (₹50)
# 3. Salad (₹40)
# 4. Juice (₹30)
# 5. View Bill
# 6. Exit

# Enter your choice: 2
# Item added to bill!

# Enter your choice: 1
# Item added to bill!

# Enter your choice: 4
# Item added to bill!

# Enter your choice: 5
# Your ordered 3 items
# Total Bill Amount: ₹105.00

# Enter your choice: 6
# Thank you for visiting UST Cafeteria!