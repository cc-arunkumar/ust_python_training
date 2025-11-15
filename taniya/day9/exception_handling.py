# Task
# Exception Handling
# Take first number as input from user and convert to integer
a = int(input("Enter first number: "))

# Take second number as input from user and convert to integer
b = int(input("Enter second number: "))

# Welcome message
print("Welcome to UST Calculator")

# Display the sum of a and b
print(f"Sum of {a} and {b} is {a+b}")

# Display the subtraction of a and b
print(f"Division of {a} and {b} is {a-b}") 

# Display the multiplication of a and b
print(f"Multiplication of {a} and {b} is {a*b}")

# Try block to handle division and catch divide-by-zero error
try:
    # Attempt to divide a by b
    print(f"Division of {a} and {b} is {a/b}")
except ZeroDivisionError:
    # Handle case where b is zero
    print("Error: Zero division is not allowed")

# Final message after all operations
print("Thank you")

# Output
# Enter first number: 10
# Enter second number: 0
# Welcome to UST Calculator
# Sum of 10 and 0 is 10
# Division of 10 and 0 is 10
# Multiplication of 10 and 0 is 0
# Error: Zero division is not allowed
# Thank you