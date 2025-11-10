# Task_3_Cafeteria_Billing_System


print("WECOME TO UST CAFETERIA")
to_bill=True
total_bill=0
no_of_items=0


while to_bill:
    print("1. Coffee (₹25)")
    print("2. Sandwich (₹50)")
    print("3. Salad (₹40)")
    print("4. Juice (₹30)")
    print("5. View Bill")
    print("6. Exit")

    option =int(input("Enter the option"))

    match option:
        case 1:
            print("Item added to bill!")
            total_bill+=25
            no_of_items+=1
        case 2:
            print("Item added to bill!")
            total_bill+=50
            no_of_items+=1
        case 3:
            print("Item added to bill!")
            total_bill+=40
            no_of_items+=1
        case 4:
            print("Item added to bill!")
            total_bill+=30
            no_of_items+=1
        case 5:
            print(f"Total bill amount!:{total_bill}")
            print(f"Total No Of Items:{no_of_items}")
        case 6:
            total_bill=0
            no_of_items=0
            to_bill=False


# Cafeteria_Billing_System.py"
# WECOME TO UST CAFETERIA
# 1. Coffee (₹25)
# 2. Sandwich (₹50)
# 3. Salad (₹40)
# 4. Juice (₹30)
# 5. View Bill
# 6. Exit
# Enter the option1
# Item added to bill!
# 1. Coffee (₹25)
# 2. Sandwich (₹50)
# 3. Salad (₹40)
# 4. Juice (₹30)
# 5. View Bill
# 6. Exit
# Enter the option2
# Item added to bill!
# 1. Coffee (₹25)
# 2. Sandwich (₹50)
# 3. Salad (₹40)
# 4. Juice (₹30)
# 5. View Bill
# 6. Exit
# Enter the option3
# Item added to bill!
# 1. Coffee (₹25)
# 2. Sandwich (₹50)
# 3. Salad (₹40)
# 4. Juice (₹30)
# 5. View Bill
# 6. Exit
# Enter the option4
# Item added to bill!
# 1. Coffee (₹25)
# 2. Sandwich (₹50)
# 3. Salad (₹40)
# 4. Juice (₹30)
# 5. View Bill
# 6. Exit
# Enter the option5
# Total bill amount!:145
# Total No Of Items:4
# 1. Coffee (₹25)
# 2. Sandwich (₹50)
# 3. Salad (₹40)
# 4. Juice (₹30)
# 5. View Bill
# 6. Exit
# Enter the option6           