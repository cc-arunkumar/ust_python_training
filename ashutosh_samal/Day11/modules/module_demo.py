import math  # Import the math module
from math import sqrt  # Import the square root function

# Prompt the user to input a number
num = int(input("Enter a number: "))  
# Calculate and print the square root of the entered number
print(f"Square root of {num} is {sqrt(num)}")


# Assign values to variables a, b, and c
a = 2
b = 7.456
c = 5

# Print the value of pi using math.pi
print("Value of pi is:", (math.pi))

# Calculate the power of 'a' raised to 2 using math.pow()
print("pow", math.pow(a, 2)) 

# Round up the value of 'b' to the nearest integer using math.ceil()
print(math.ceil(b))  

# Round down the value of 'b' to the nearest integer using math.floor()
print(math.floor(b)) 

# Truncate the decimal part of 'b' using math.trunc()
print(math.trunc(b))  

# Calculate the factorial of 'c' using math.factorial()
print(math.factorial(c))  

# Calculate the absolute value of 'b' using math.fabs()
print(math.fabs(b)) 


#Sample Output
# Enter a number: 4
# Square root of 4 is 2.0
# Value of pi is: 3.141592653589793
# pow 4.0
# 8
# 7
# 7
# 120
# 7.456
