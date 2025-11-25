from datetime import date   # Import date class to work with calendar dates
from math import sqrt, pi, pow, floor, trunc, ceil, factorial, fabs
# Import common math functions/constants

# print("the value of 9 is " ,sqrt(9))  
# sqrt(9) → square root of 9 = 3.0

# print("the value of 9 is " ,pi)  
# pi → mathematical constant ≈ 3.14159

# print("the value of math.pow()", pow(3,5))  
# pow(3,5) → 3 raised to power 5 = 243.0

# val = 7.2
# print("the value of math.floor()", floor(val))  
# floor(7.2) → largest integer ≤ 7.2 → 7

# print("the value of math.ceil()", ceil(val))  
# ceil(7.2) → smallest integer ≥ 7.2 → 8

# print("the value of math.trunc()", trunc(val))  
# trunc(7.2) → truncate decimal part → 7

# print("the value of math.trunc()", factorial(val))  
# factorial() only works with integers, factorial(7) = 5040

# print("the value of math.abs()", abs(val))  
# abs(7.2) → absolute value → 7.2

# print("the value of math.round()",(val))  
# round(val) → rounds to nearest integer → 7

# Print today’s date in DD-MM-YYYY format
print(date.today().strftime("%d-%m-%Y"))
