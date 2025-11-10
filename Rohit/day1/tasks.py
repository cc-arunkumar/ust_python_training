a = int(input("Enter the first number: "))
b = int(input("Enter the first number: "))
c = int(input("Enter the first number: "))
d = int(input("Enter the first number: "))
e = int(input("Enter the first number: "))
sum = a+b+c+d+e
percentage = (sum/500)*100
if(percentage>=90):
    print("A")
elif(percentage>=80 and percentage<=89):
    print("B")
elif(percentage>=70 and percentage<=79):
    print("C")
elif(percentage>=60 and percentage<=69):
    print("D")
elif(percentage<60):
    print("FAIL")

print(percentage)
