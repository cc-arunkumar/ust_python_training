marks = eval(input("Enter your Mark of 5 Subjects : "))
total =0
percentage =0
for mark in marks:  
    total = total+mark
    #print("Total mark", total)
percentage= (total//100)*100
if(percentage>90):
    print("A")
elif(percentage>=80 and percentage<=89):
    print("B")
elif(percentage>=70 and percentage<=79):
    print("C")
elif(percentage>=60 and percentage<=69):
    print("D")
else:
    print("F")
    





