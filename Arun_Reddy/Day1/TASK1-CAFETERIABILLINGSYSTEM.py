print("======UST CAFETERIA=====")
print("1. Coffee (a,25)")
print("2. Sandwich (a,50)")
print("3. Salad (a,40)")
print("4. Juice (a,30)")
print("5. View Bill")
print("6. Exit")
TotalAmount=0
count=0
while True:
    ch=int(input("Enter ur choice: "))
    match ch:
        case 1:
            print("Item added to bill")
            TotalAmount+=25
            count=count+1
        case 2: 
            print("Item added to bill")
            TotalAmount+=50
            count=count+1
        case 3:
            print("Item added to bill")
            TotalAmount+=40
            count=count+1
        case 4:
            print("Item added to bill")
            TotalAmount+=30
            count=count+1
        case 5:
            print(f"You Ordered {count} Items")
            print("Total Bill Amount:",TotalAmount)
        case 6:
            print("Thank you for visiting UST Cafeteria!")
            break

