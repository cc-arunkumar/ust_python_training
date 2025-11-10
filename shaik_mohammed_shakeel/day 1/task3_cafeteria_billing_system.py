

# Task 3: Cafeteria Billing System
# Objective
# 	Simulate a Cafeteria Menu Ordering System for employees inside the office campus. Employees can order multiple items and get a running total of their bill.
	

print("Hi Welcome To Cafeteria")
print("Coffee ($25)")
print("Sandwich ($50)")
print("Salad($40)")
print("Juice($30)")
print("View Bill")
print("Exit")
co=sa=sl=ju=0
total=0
while True:
    
    a=int(input("Enter Your Choice: "))
    if(a==1):
        print("Item added to bill")
        co+=1
        total+=25
    elif(a==2):
        print("Item added to bill")
        sa+=1
        total+=50
    elif(a==3):
        print("Item added to bill")
        sl+=1
        total+=40
    elif(a==4):
        print("Item added to bill")
        ju+=1
        total+=30
    elif(a==5):
        count=co+sa+sl+ju

        print("You ordered", count,"items.")
        print("Total bill amount:", total)
    elif(a==6):
        print("Thank you for visiting Cafeteria")
        break
    else:
        print("Invalid Number")


# Sample Output
# Hi Welcome To Cafeteria
# Coffee ($25)
# Sandwich ($50)
# Salad($40)
# Juice($30)
# View Bill
# Exit
# Enter Your Choice: 1
# Item added to bill
# Enter Your Choice: 3
# Item added to bill
# Enter Your Choice: 5
# You ordered 2 items.
# Total bill amount: 65
# Enter Your Choice: 6
# Thank you for visiting Cafeteria
