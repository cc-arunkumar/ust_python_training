## Task 3: Cafeteria Billing System
# Simulate a Cafeteria Menu Ordering System for employees inside the office campus.
# Employees can order multiple items and get a running total of their bill.

# Initialize prices and counters
coff, sand, salad, juice, tot, count = 25, 50, 40, 25, 0, 0

# Start a continuous loop for the cafeteria menu system
while(True):
    print("\n===UST Cafeteria===")
    print("1. Coffee ($25)")
    print("2. Sandwich ($50)")
    print("3. Salad ($40)")
    print("4. Juice ($25)")
    print("5. View Bill")
    print("6. Exit")
    
    # Get user's choice
    chc = input("Enter your choice: ")
    
    # Add coffee to the bill
    if chc == '1':
        tot += coff  # Add coffee price to total
        count += 1   # Increment item count
        print("Item added to the bill")
        
    # Add sandwich to the bill
    elif chc == '2':
        tot += sand  # Add sandwich price to total
        count += 1   # Increment item count
        print("Item added to the bill")
        
    # Add salad to the bill
    elif chc == '3':
        tot += salad  # Add salad price to total
        count += 1    # Increment item count
        print("Item added to the bill")
        
    # Add juice to the bill
    elif chc == '4':
        tot += juice  # Add juice price to total
        count += 1    # Increment item count
        print("Item added to the bill")
        
    # Display total bill and items ordered
    elif chc == '5':
        print(f"You ordered {count} items")
        print(f"Total bill amount: {tot}")
        
    # Exit the program
    elif chc == '6':
        print("Thank You for visiting UST Cafeteria")
        break
        
    # Invalid choice
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