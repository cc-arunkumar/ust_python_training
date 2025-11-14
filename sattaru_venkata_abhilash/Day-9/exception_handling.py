# Exception Handlingzero

# Taking two numbers from the user
a = int(input("Enter a Value of A: "))
b = int(input("Enter a Value of B: "))

print("Welcome to UST Calculator Application")

# Performing normal arithmetic operations
print(f"add = {a + b}")
print(f"sub = {a - b}")
print(f"product = {a * b}")

# Exception handling for division
try:
    print(f"div = {a / b}")   # Risky code: b might be zero

# Handles division by zero error
except ZeroDivisionError:
    print("Error: Cannot divide by zero")

# Example of catching file-related issues (not used here, but included)
except FileNotFoundError:
    print("Error: File does not exist")

# Generic exception for any other unexpected error
except Exception:
    print("Error: Something went wrong (possibly invalid input)")

# This will print always whether error happens or not
print("Thank you")
print("------Visit Again------")




# Sample Output:
# Enter a Value of A: 12
# Enter a Value of B: 0
# Welcome to UST Calculator Application
# add = 12
# sub = 12
# product = 0
# Error: Cannot divide by zero
# Thank you
# ------Visit Again------