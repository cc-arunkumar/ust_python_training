print("==========Ust IT Help Desk===========")
print("coffee price 25 and choose 1")
print("Sandwhich price 50 and choose 2")
print("salad price 40 and choose 3")
print("juice price 30 and choose 4")
print("view bill 5")
print("Exit 6")
print("Please choose between 1 to 5")


total_bill =0
count=0
while True:
    n = int(input("Enter the number"))
    if n==1:
        
        total_bill+=25
        count+=1
        print("item added")
    if n==2:
        total_bill+=50
        count+=1
        print("item added")
    if n==3:
        total_bill+=40
        count+=1
        print("item added")
    if n==4:
        total_bill+=30
        count+=1
        print("item added")
    if n==5:
        print(f"Items added {count} and total price {total_bill}")
    if n==6:
        print("Thank you for visiting UST Cafeteria")
    if n>5 or n<1:
         print("please choose between 1 to 5")

# ==========Ust IT Help Desk===========
# coffee price 25 and choose 1
# Sandwhich price 50 and choose 2
# salad price 40 and choose 3
# juice price 30 and choose 4
# view bill 5
# Exit 6
# Please choose between 1 to 5
# Enter the number3
# item added
# Enter the number2
# item added
# Enter the number3
# item added
# Enter the number1
# item added
# Enter the number5
# Items added 4 and total price 155
    