# Exception_handling

# class ExceptionHandling:
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("Welcome to the UST")
print(f"Addition = {a + b}")
print(f"Subtraction = {a - b}")
print(f"Multiplication = {a * b}")

# Using try except to handle exception

try:
     print(f"Division = {a / b}")  

except ZeroDivisionError:
    print("Zero Division Error: Division by zero is not allowed")

except ValueError:
    print("Value Error: Please enter only numbers")

except Exception:
    print("Exception Found")

# -----------------------------------------------------------------------------------------

# Sample Output

# Enter the first number: 100
# Enter the second number: 0
# Welcome to the UST
# Addition = 100
# Subtraction = 100
# Multiplication = 0
# Zero Division Error: Division by zero is not allowed


