## Task 3: Cafeteria Billing System
# Simulate a Cafeteria Menu Ordering System for employees inside the office campus.
# Employees can order multiple items and get a running total of their bill.

coff,sand,salad,juice,tot,count=25,50,40,25,0,0
while(True):
    print("\n===UST Cafetaria===")
    print("1.Coffee($25)")
    print("2.Sandwich($50)")
    print("3.Salad($40)")
    print("4.Juice($25)")
    print("5.View Bill")
    print("6.Exit")
    chc=input("Enter your choice: ")
    if chc== '1':
        tot+=coff
        count+=1
        print("Item added to the bill")
    elif chc=='2':
        tot+=sand
        count+=1
        print("Item added to the bill")
    elif chc=='3':
        tot+=salad
        count+=1
        print("Item added to the bill")

    elif chc=='4':
        tot+=juice
        count+=1
        print("Item added to the bill")
    elif chc=='5':
        print(f"You ordered {count} items")
        print(f"Total bill amount: {tot}")
    elif chc=='6':
        print("Thank You for visiting UST Cafeteria")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6")

## Sample output

# ===UST Cafetaria===
# 1.Coffee($25)
# 2.Sandwich($50)
# 3.Salad($40)
# 4.Juice($25)
# 5.View Bill
# 6.Exit
# Enter your choice: 1
# Item added to the bill

# ===UST Cafetaria===
# 1.Coffee($25)
# 2.Sandwich($50)
# 3.Salad($40)
# 4.Juice($25)
# 5.View Bill
# 6.Exit
# Enter your choice: 2
# Item added to the bill

# ===UST Cafetaria===
# 1.Coffee($25)
# 2.Sandwich($50)
# 3.Salad($40)
# 4.Juice($25)
# 5.View Bill
# 6.Exit
# Enter your choice: 3
# Item added to the bill

# ===UST Cafetaria===
# 1.Coffee($25)
# 2.Sandwich($50)
# 3.Salad($40)
# 4.Juice($25)
# 5.View Bill
# 6.Exit
# Enter your choice: 4
# Item added to the bill

# ===UST Cafetaria===
# 1.Coffee($25)
# 2.Sandwich($50)
# 3.Salad($40)
# 4.Juice($25)
# 5.View Bill
# 6.Exit
# Enter your choice: 5
# You ordered 4 items
# Total bill amount: 140

# ===UST Cafetaria===
# 1.Coffee($25)
# 2.Sandwich($50)
# 3.Salad($40)
# 4.Juice($25)
# 5.View Bill
# 6.Exit
# Enter your choice: 6
# Thank You for visiting UST Cafeteria