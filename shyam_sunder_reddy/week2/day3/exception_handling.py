#Exception Handling
a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
print(a+b)
print(a-b)
print(a*b)
#try block
try:
    print(a/b)

#specific except block
except ZeroDivisionError:
    print("Division by zero")

#generic except block
except Exception:
    print("Generic Error")
    
#sample output
# Enter a number: 10
# Enter another number: 0
# 10
# 10
# 0
# Division by zero