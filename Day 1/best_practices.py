a = int(input("Enter sub1 mark:"))
b = int(input("Enter sub2 mark:"))
c = int(input("Enter sub3 mark:"))
d = int(input("Enter sub4 mark:"))
e = int(input("Enter sub5 mark:"))


tot = a+b+c+d+e
print(tot)
percentage = tot/5
print(percentage)

if(percentage>=90):
    print("A Grade")
elif(percentage>=80 and percentage<90):
    print("B Grade")
elif(percentage>=70 and percentage<80):
    print("C Grade")
elif(percentage>=60 and percentage<70):
    print("D Grade")
else:
    print("E Grade")