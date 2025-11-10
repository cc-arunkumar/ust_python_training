
def cafeteria_system():
    print('''Cafeteria Menu
          1.Coffee - $3
          2.Sandwich - $5
          3.Salad - $4
          4.Juice - $2
          5.View Bill
          6.Exit''')
    choice = int(input("Enter your choice: "))
    total_bill,items=0,0
    if (choice<1 and choice>6):
        print("Invalid Choice")
    while(True):
        if choice == 1:
            total_bill+=3
            items+=1
        elif choice == 2:
            total_bill+=5
            items+=1
        elif choice == 3:
            total_bill+=4
            items+=1
        elif choice == 4:
            total_bill+=2
            items+=1
        elif choice == 5:
         print(f'''Total items ordered: {items}
        Total bill amount: ${total_bill}''')
        elif choice == 6:
            print("Exiting the Cafeteria System.Thank you!")
            break
        choice = int(input("Enter your choice: "))
    return
cafeteria_system()
# Cafeteria Menu
#           1.Coffee - $3
#           2.Sandwich - $5
#           3.Salad - $4
#           4.Juice - $2
#           5.View Bill
#           6.Exit
# Enter your choice: 1
# Enter your choice: 2
# Enter your choice: 3
# Enter your choice: 4
# Enter your choice: 5
# Total items ordered: 4
#         Total bill amount: $14
# Enter your choice: 6
# Exiting the Cafeteria System.Thank you!