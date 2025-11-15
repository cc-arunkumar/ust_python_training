a=int(input("Enter number 1:"))
b=int(input("Enter number 2:"))

try:
    c=a//b
    print(c)

except ZeroDivisionError:
    print("Dont give zero denominator da dei")

