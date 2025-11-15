# Write a Python program that takes two numbers as input.

# Perform addition, subtraction, multiplication, and division on them.

# Use a try/except block to handle division by zero gracefully.

#taking input of two numbers
a = int(input("Enter the number : "))
b = int(input("Enter the number : "))

print("Welcome to UST Calculator App")

add = a + b
print("Addition:", add)

sub = a - b
print("Subtraction:", sub)

mul = a * b
print("Multiplication:", mul)

# Division with error handling
try:
    div = a / b
    print("Division:", div)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed")

#output
# Enter the number : 10
# Enter the number : 0
# Welcome to UST Calculator App
# Addition: 10
# Subtraction: 10
# Multiplication: 0
# Error: Division by zero is not allowed

#output2
# Enter the number : 10
# Enter the number : 20
# Welcome to UST Calculator App
# Addition: 30
# Subtraction: -10
# Multiplication: 200
# Division: 0.5