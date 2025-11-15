# Exception_handling

a=int(input("Enter a number"))
b=int(input("Enter a number"))
print("Welcome to the calculator app")
print("Addition :",a+b)
print("Subtraction :",a-b)
print("Multiplication:",a*b)
try:
    div=a/b
    print("Division:",div)
except FileNotFoundError:
    print("file not found")
    
except ZeroDivisionError:
    print("Zero Division Error")

#output
# Enter a number2
# Enter a number4
# Welcome to the calculator app
# Addition : 6
# Subtraction : -2
# Multiplication: 8
# Division: 0.5


# Enter a number2
# Enter a number0
# Welcome to the calculator app
# Addition : 2
# Subtraction : 2
# Multiplication: 0
# Zero Division Error

