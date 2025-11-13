#Task3 Cafeteria Billing System
print("====== UST Cafeteria ======")
print("1. Coffee (Rs. 25)")
print("2. Sandwich (Rs. 50)")
print("3. Salad (Rs. 40)")
print("4. Juice (Rs. 30)")
print("5. View Bill ")
print("6. Exit")
choice=int(input("Enter your choice: "))
count_items=0
total_bill=0
while(True):
    if(choice==1):
        total_bill=total_bill+25.00
        count_items+=1
        print("Item added to bill!")
    elif(choice==2):
        total_bill=total_bill+50.00
        count_items+=1
        print("Item added to bill!")
    elif(choice==3):
        total_bill=total_bill+40.00
        count_items+=1
        print("Item added to bill!")
    elif(choice==4):
        total_bill=total_bill+30.00
        count_items+=1
        print("Item added to bill!")
    elif(choice==5):
        print("You have ordered ",count_items," items.")
        print("Total Bill Amount: Rs",total_bill)
    else:
        break
    choice=int(input("Enter your choice: "))
print("Thank you for visiting UST Cafeteria")

#Sample Execution
#====== UST Cafeteria ======
#1. Coffee (Rs. 25)
#2. Sandwich (Rs. 50)
#3. Salad (Rs. 40)
#4. Juice (Rs. 30)
#5. View Bill
#6. Exit
#Enter your choice: 1
#Item added to bill!
#Enter your choice: 2
#Item added to bill!
#Enter your choice: 3
#Item added to bill!
#Enter your choice: 5
#You have ordered  3  items.
#Total Bill Amount: Rs 115.0
#Enter your choice: 6
#Thank you for visiting UST Cafeteria
