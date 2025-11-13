marks=eval(input("Marks of 5 subjects"))
total=0
percentage=0
for mark in marks:
    total=total+mark
print("Total mark ",total)
percentage=int(input("Enter percentage"))
if(percentage>=90):
    print("Grade A")
elif(percentage>=80 and percentage<=89):
    print("Grade B")
elif(percentage>=70 and percentage<=79):
    print("Grade C")
elif(percentage>=60 and percentage<=69):
    print("Grade D")
elif(percentage<60):
    print("Grade F")
    


