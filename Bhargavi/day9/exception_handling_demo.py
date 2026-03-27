# Write a Python program that takes two numbers as input.

# Perform addition, subtraction, multiplication, and division on them.

# Use a try/except block to handle division by zero gracefully.

# Taking input of two numbers
a = int(input("Enter the number: "))  
b = int(input("Enter the number: ")) 

# Display welcome message
print("Welcome to UST Calculator App")  

# Addition
add = a + b 
print("Addition:", add)  # Display the result

 # Subtract the second number from the first
sub = a - b  
print("Subtraction:", sub)  

# Multiply the two numbers
mul = a * b 
print("Multiplication:", mul)  

# Division with error handling (to avoid division by zero)
 # Handle division by zero error
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