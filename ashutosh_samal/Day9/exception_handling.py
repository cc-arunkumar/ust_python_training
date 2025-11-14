#Exception handling

#user input of two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

#try except for error handling
try:
    print(a/b)
except ZeroDivisionError:
    print("Not divisible by zero")
except Exception:
    print("Error")

#Sample Execution
# Enter first number: 10
# Enter second number: 0
# Not divisible by zero