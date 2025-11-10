#Task 3: Cafeteria Billing System

#Code
print("=======UST Cafeteria=======")
print("1.Coffee(Rs.25)")
print("2.Sandwich(Rs.50)")
print("3.Salad(Rs.40)")
print("4.Juice(Rs.30)")
print("5.View Bill")
print("6.Exit")

choice = int(input("Enter Your Choice : "))
total_item=0
total_amt=0

coffee_price=25
sandwich_price=50
salad_price=40
juice_price=30

Coffee=0
Sandwich=0
Salad=0
Juice=0
while(True):
    if(choice==1):
        Coffee+=1
        print("Item added to Bill!!")
    elif(choice==2):
        Sandwich+=1
        print("Item added to bill!!")
    elif(choice==3):
        Salad+=1
        print("Item added to bill!!")
    elif(choice==4):
        Juice+=1
        print("Item added to bill!!")
    elif(choice==5):
        total_item=Coffee+Sandwich+Salad+Juice
        total_amt=coffee_price+sandwich_price+salad_price+juice_price
        print("You ordered",total_item,"item")
        print("Total Amount : ",total_amt)
    else:
        break
    choice=int(input("Enter your choice : "))
print("Thank Youu for visiting UST Cafeteria!!")


#Sample Output:
# =======UST Cafeteria=======
# 1.Coffee(Rs.25)
# 2.Sandwich(Rs.50)
# 3.Salad(Rs.40)
# 4.Juice(Rs.30)
# 5.View Bill
# 6.Exit

# Enter Your Choice : 1
# Item added to Bill!!
# Enter your choice : 3
# Item added to bill!!
# Enter your choice : 2
# Item added to bill!!
# Enter your choice : 1
# Item added to Bill!!
# Enter your choice : 5
# You ordered 4 item
# Total Amount :  145
# Enter your choice : 6
# Thank Youu for visiting UST Cafeteria!!


