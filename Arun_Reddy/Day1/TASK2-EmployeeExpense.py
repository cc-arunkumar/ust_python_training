print("======Employee Expense System=========")
print("1. Add Travel Expense")
print("2. Add Meal Expense")
print("3. Add Miscellaneous Expense")
print("4. View Total Reimbursement")
print("5. Exit")
totalCost=0.0
while True:
    ch=int(input("Enter your choice"))
    match ch:
        case 1:
             ans=int(input("Enter ur travel expense"))
             totalCost+=ans
             print("Expense added Succesfully")
        case 2:
            res=float(input("Enter ur Meal Expense"))
            totalCost+=res
            print("Expense added Succesfully")
        case 3:
            misc=float(input("Enter ur Miscallaneous expense"))
            totalCost+=misc
            print("Expense added Succesfully")
        case 4:
            print("TotalCost EXpenses",totalCost)
        case 5:
            print("Thank you! Hava a great day")
            break

                
                