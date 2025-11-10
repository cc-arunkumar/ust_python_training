print("============ UST Cafeteria ==============")
print("1. Coffee Rs25")
print("2. Sandwich Rs50")
print("3. Salad Rs40")
print("4. Juice Rs30")
print("5. View Bill")
print("5. Exit")

total=0
count=0
while(True):
    choice=int(input("enter the choice: "))
    if(choice<1 or choice >5):
        print("Enter the number between 1 to 5")
    if (choice==1):
        total+=25
        count+=1
        print("Item added to bill! ")
    if(choice==2):
        total+=50
        count+=1
        print("Item added to bill! ")
    if(choice==3):
        total+=40
        count+=1
        print("Item added to bill! ")
    if(choice==4):
        total+=30
        count+=1
        print("Item added to bill! ")
    if(choice==5):
        print(f"You ordered {count} items.")
        print(f"Total Bill Amount: {total}")
    if(choice==6):
        print("Thank you for visiting UST Cafeteria!")
        print("***********************************************************")
        break



#     ============ UST Cafeteria ==============
# 1. Coffee Rs25
# 2. Sandwich Rs50
# 3. Salad Rs40
# 4. Juice Rs30
# 5. View Bill
# 5. Exit
# enter the choice: 1
# Item added to bill! 
# enter the choice: 2
# Item added to bill! 
# enter the choice: 3
# Item added to bill! 
# enter the choice: 4
# Item added to bill! 
# enter the choice: 5
# You ordered 4 items.
# Total Bill Amount: 145
# enter the choice: 6
# Enter the number between 1 to 5
# Thank you for visiting UST Cafeteria!
# ***********************************************************