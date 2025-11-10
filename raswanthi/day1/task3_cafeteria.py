#UST Cafeteria
print("UST Cafeteria\n")
print("1.Coffee - $25")
print("2.Sandwich - $50")
print("3.Salad - $40")
print("4.Juice - $30")
print("5.View Bill")
print("6.Exit")

item_count=0
total_price=0
while True:
    choice = input("Enter your choice: ")
    match choice:
        case "1":
            print("Item added to bill!")
            total_price+=25
            item_count+=1
        case "2":
            print("Item added to bill!")
            total_price+=50
            item_count+=1
        case "3":
            print("Item added to bill!")
            total_price+=40
            item_count+=1
        case "4":
            print("Item added to bill!")
            total_price+=30
            item_count+=1

        case "5":
            print(f"You ordered {item_count}")
            print(f"Total Bill Amount : ${total_price}")
        
        case "6":
            print("Thankyou for visiting UST Cafeteria!")
            break

'''output:
UST Cafeteria

1.Coffee - $25
2.Sandwich - $50
3.Salad - $40
4.Juice - $30
5.View Bill
6.Exit
Enter your choice: 1
Item added to bill!
Enter your choice: 1
Item added to bill!
Enter your choice: 2
Item added to bill!
Enter your choice: 3
Item added to bill!
Enter your choice: 3
Item added to bill!
Enter your choice: 4
Item added to bill!
Enter your choice: 5
You ordered 6
Total Bill Amount : $210
Enter your choice: 6
Thankyou for visiting UST Cafeteria!
'''

    