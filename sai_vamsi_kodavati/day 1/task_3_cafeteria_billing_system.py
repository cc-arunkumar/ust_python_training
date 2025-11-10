# TASK 3 - Cafeteria Billing System
print("Hello")
total = 0

print("UST Cafeteria")
print("1.Coffee (Rs 25)")
print("2.Sandwich (Rs 50)")
print("3.Salad (Rs 40)")
print("4.Juice (Rs 30)")
print("5.View Bill")
print("6.Exit")

while True:
    choice = int(input("Enter your choice: "))

    if(choice == 1):
        print("Item added to bill")
        price = 25
        total += price

    elif(choice == 2):
        print("Item added to bill")
        price = 50
        total += price

    elif(choice == 3):
        print("Item added to bill")
        price = 40
        total += price

    elif(choice == 4):
        print("Item added to bill")
        price = 30
        total += price

    elif(choice == 5):
        print(total)
        print("Thank you for visiting UST Cafeteria")
        
    
    elif(choice == 6):
        print("Exit")
        

    else:
        print("Invalid choice")
        break

# Sample Output
# Hello
# UST Cafeteria
# 1.Coffee (Rs 25)
# 2.Sandwich (Rs 50)
# 3.Salad (Rs 40)
# 4.Juice (Rs 30)
# 5.View Bill
# 6.Exit
# Enter your choice: 1
# Item added to bill
# Enter your choice: 2
# Item added to bill
# Enter your choice: 3
# Item added to bill
# Enter your choice: 4
# Item added to bill
# Enter your choice: 5
# 145
# Thank you for visiting UST Cafeteria
# Enter your choice: 6
# Exit
# Enter your choice: 7
# Invalid choice

