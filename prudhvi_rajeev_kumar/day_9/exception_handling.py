#exception handling:
a = int(input("Enter  number a : "))
b = int(input("Enter  number b : "))
sum = a + b
print("The sum is :",sum)
sub = a - b
print("The subtraction is :",sub)
mul = a * b
print("The multiplication is :",mul)
try:
    result = a / b
    print("The Division is:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
finally:
    b = int(input("Enter  number b : "))
    result = a / b
    print("The Division is:", result)

#Sample Output:
# Enter  number a : 10
# Enter  number b : 0
# The sum is : 10
# The subtraction is : 10
# The multiplication is : 0
# Error: Division by zero is not allowed.

# Enter  number b : 20
# The sum is : 30
# The subtraction is : -10
# The multiplication is : 200
# The Division is: 0.5

