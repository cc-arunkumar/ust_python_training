# Exception_handling

# Take input from the user and convert to integer
a = int(input("Enter a number"))
b = int(input("Enter a number"))

# Display welcome message
print("Welcome to the calculator app")

# Perform basic arithmetic operations
print("Addition :", a + b)          # Add two numbers
print("Subtraction :", a - b)      # Subtract second number from first
print("Multiplication:", a * b)    # Multiply two numbers

# Division wrapped in try-except to handle errors
try:
    div = a / b                    # Try dividing a by b
    print("Division:", div)        # Print result if no error occurs

# trying all expects 
except FileNotFoundError:
    print("file not found")

# Handle division by zero error
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

