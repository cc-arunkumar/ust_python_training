# Task 3: Cafeteria Billing System

total_bill = 0.0
item_count = 0


print("\n====== UST Cafeteria ======")
print("1. Coffee (₹25)")
print("2. Sandwich (₹50)")
print("3. Salad (₹40)")
print("4. Juice (₹30)")
print("5. View Bill")
print("6. Exit")
while True:
    
    choice = int(input("Enter your choice: "))
    
    match choice:
        case 1:
            total_bill += 25
            item_count += 1
            print("Item added to bill!")
            
        case 2:
            total_bill += 50
            item_count += 1
            print("Item added to bill!")
            
        case 3:
            total_bill += 40
            item_count += 1
            print("Item added to bill!")
            
        case 4:
            total_bill += 30
            item_count += 1
            print("Item added to bill!")
            
        case 5:
            print(f"You ordered {item_count} items.")
            print(f"Total Bill Amount: ₹{total_bill:.2f}")
            
        case 6:
            print("Thank you for visiting UST Cafeteria!")
            break
            
# sample output      
# ====== UST Cafeteria ======
# 1. Coffee (₹25)
# 2. Sandwich (₹50)
# 3. Salad (₹40)
# 4. Juice (₹30)
# 5. View Bill
# 6. Exit
# Enter your choice: 1
# Item added to bill!
# Enter your choice: 2
# Item added to bill!
# Enter your choice: 5
# You ordered 2 items.
# Total Bill Amount: ₹75.00
# Enter your choice: 6
# Thank you for visiting UST Cafeteria!