import math
import random

# Importing sqrt directly from math for convenience
from math import sqrt

# -------------------------------
# MATH MODULE FUNCTIONS
# -------------------------------

# Square root of a number
print("Square root of 5 =", sqrt(5))

# Print value of PI
print("PI value =", math.pi)

# Power function: 2⁵
print("2 power 5 =", math.pow(2, 5))

# Floor: largest integer ≤ value
print("Floor of 2.455 =", math.floor(2.455))

# Ceil: smallest integer ≥ value
print("Ceiling of 8.2 =", math.ceil(8.2))

# Truncate: remove decimal part
print("Truncate 7.5 =", math.trunc(7.5))

# Factorial of 5
print("Factorial(5) =", math.factorial(5))

# fabs: absolute value (always positive)
print("fabs(-5) =", math.fabs(-5))
print("fabs(5) =", math.fabs(5))
print("fabs(5.3) =", math.fabs(5.3))

# Logarithms
x = 10
print("Natural log of 10 =", math.log(x))       # ln(10)
print("Log base 10 of 10 =", math.log10(x))    # log₁₀(10)
print("Log base 2 of 10 =", math.log2(x))      # log₂(10)

# Rounding numbers
print("round(7.2) =", round(7.2))
print("round(7.8) =", round(7.8))
print("round(7.4) =", round(7.4))

# -------------------------------
# RANDOM MODULE FUNCTIONS
# -------------------------------

# Generate random OTP between 0–9
otp = random.randint(0, 9)
print("Random OTP (0-9) =", otp)

# Generate random integer between given range
otp = random.randint(12, 604554)
print("Random number (12 to 604554) =", otp)

# Working with lists and random operations
fruits = ["Apple", "Banana", "Graps", "Mango", "Orange"]
print("Original fruit list =", fruits)

# Shuffle list items (changes original list)
random.shuffle(fruits)
print("Shuffled fruit list =", fruits)

# Pick one random fruit from list
fruits_choice = random.choice(fruits)
print("Randomly chosen fruit =", fruits_choice)




# sample output:
# Square root of 5 = 2.23606797749979
# PI value = 3.141592653589793
# 2 power 5 = 32.0
# Floor of 2.455 = 2
# Ceiling of 8.2 = 9
# Truncate 7.5 = 7
# Factorial(5) = 120
# fabs(-5) = 5.0
# fabs(5) = 5.0
# fabs(5.3) = 5.3
# Natural log of 10 = 2.302585092994046
# Log base 10 of 10 = 1.0
# Log base 2 of 10 = 3.321928094887362
# round(7.2) = 7
# round(7.8) = 8
# round(7.4) = 7

# Random OTP (0-9) = 4
# Random number (12 to 604554) = 98746

# Original fruit list = ['Apple', 'Banana', 'Graps', 'Mango', 'Orange']
# Shuffled fruit list = ['Mango', 'Apple', 'Orange', 'Graps', 'Banana']
# Randomly chosen fruit = Orange
