print("UST Calculator")
try:
    a=int(input("Enter the number :"))
    b=int(input("Enter the number :"))
    print(f"Sum = {a+b}")
    print(f"Diff = {a-b}")
    print(f"Product = {a*b}")
    print(f"Division = {a/b}")
    s="1"+1
    file = open("f1.txt","r")

except ZeroDivisionError:
    print("Division by zero is not allowed!!")

except Exception as e:
    print(str(e))
