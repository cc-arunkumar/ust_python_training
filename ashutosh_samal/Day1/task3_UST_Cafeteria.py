#Task3: UST Cafeteria

# Display the UST Cafeteria menu with available items and their prices
print("====== UST Cafeteria ======")
print("1. Coffee (RS25)")
print("2. Sandwich (RS50)")
print("3. Salad (RS40)")
print("4. Juice (RS30)")
print("5. View Bill")
print("6. Exit")

# Initialize variables to track the total items ordered and the total cost
total_item_count = 0
total_cost = 0

# Start an infinite loop to process the user's choices
while True:
    # Prompt the user to enter a choice from the menu
    choice = int(input("Enter your choice: "))

    # Check if the user selected coffee (RS25)
    if choice == 1:
        total_item_count += 1  # Increment the total item count
        total_cost += 25       # Add the price of coffee to the total cost
        print("Item added to bill!")
    
    # Check if the user selected sandwich (RS50)
    elif choice == 2:
        total_item_count += 1  # Increment the total item count
        total_cost += 50       # Add the price of sandwich to the total cost
        print("Item added to bill!")
    
    # Check if the user selected salad (RS40)
    elif choice == 3:
        total_item_count += 1  # Increment the total item count
        total_cost += 40       # Add the price of salad to the total cost
        print("Item added to bill!")
    
    # Check if the user selected juice (RS30)
    elif choice == 4:
        total_item_count += 1  # Increment the total item count
        total_cost += 30       # Add the price of juice to the total cost
        print("Item added to bill!")
    
    # If the user wants to view their bill
    elif choice == 5:
        print("You ordered ", total_item_count, " items")  # Display total items ordered
        print("Total Bill: ", total_cost)  # Display the total cost of the bill
    
    # If the user selects the exit option
    elif choice == 6:
        print("Thank you for visiting UST Cafeteria")  # Farewell message
        break  # Exit the loop and terminate the program
    
    # If the user enters an invalid choice (anything other than 1-6)
    else:
        print("Invalid Choice, please select a valid option.")




#Sample Execution
# ====== UST Cafeteria ======
# 1. Coffee (RS25)
# 2. Sandwich (RS50)
# 3. Salad (RS40)
# 4. Juice (RS30)
# 5. View Bill
# 6. Exit
# Enter your choice: 1
# Item added to bill!
# Enter your choice: 2
# Item added to bill!
# Enter your choice: 3
# Item added to bill!
# Enter your choice: 4
# Item added to bill!
# Enter your choice: 5
# You ordered  4  items
# Total Bill:  145
# Enter your choice: 6
# Thankyou for visiting UST Cafeteria