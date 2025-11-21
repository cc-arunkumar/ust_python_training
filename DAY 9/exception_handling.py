import sys

# Welcome message for the calculator
print("Welcome to UST Calculator")

# Taking user input for numbers
a = int(input("Enter Numerator : "))
b = int(input("Enter Denominator : "))

# Basic Arithmetic Operations
print("Add :", a + b)
print("Subtract :", a - b)
print("Multiply :", a * b)

# Handling division with exception block
try:
    print("Division :", a / b)

except ZeroDivisionError:
    # Executes when denominator is zero
    print("Division Error : Enter Denominator > 0")

#Generic exception (commented by user)
# except Exception as e:
#     print("Please check :", e)

# End message
print("Thank you For Using UST Calculator")




"""
SAMPLE OUTPUT

Welcome to UST Calculator
Enter Numberator :10
Enter Denominator :0
Add : 10
Subtract : 10
Multiply : 0
Division Error :Enter Denominator > 0
Thanks For using UST Calculator

"""