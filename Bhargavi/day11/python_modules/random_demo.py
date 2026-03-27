# the demostration of various random functions
from math import sqrt, pi
import math
import random

# Getting user input for a number to demonstrate math functions
x = int(input("Enter a number: "))
print("Square root of", x, "is:", sqrt(x))
print("Value of pi is:", pi)
print(f"Square of {x} is:", math.pow(x, 2))

# Demonstrating math functions with a float
x = 7.3333
print("Ceiling value of", x, "is:", math.ceil(x))
print("Floor value of", x, "is:", math.floor(x))
print("Truncated value of", x, "is:", math.trunc(x))
print("Factorial of 8 is:", math.factorial(8))
print("Absolute value of -10 is:", math.fabs(-10))
print("Natural logarithm of", x, "is:", math.log(x))
print("Base-10 logarithm of", x, "is:", math.log10(x))
print("Base-2 logarithm of", x, "is:", math.log2(x))

# Demonstrating rounding
print("Round of 5.2 is:", round(5.2))
print("Round of 5.8 is:", round(5.8))

# Random module examples

# Generating a random integer between 0 and 9
x = random.randint(0, 9)
print("Random integer between 0 and 9:", x)

# Generating a random 6-digit number
x = random.randint(100000, 999999)
print("Random 6-digit number:", x)

# List of fruits to demonstrate random operations
fruits = ["apple", "banana", "kiwi", "strawberry", "mango"]
print("Original fruits:", fruits)

# Shuffling the list of fruits
random.shuffle(fruits)
print("After shuffling:", fruits)

# Picking a random fruit from the list
print("Randomly chosen fruit:", random.choice(fruits))

# Getting a random sample of 2 fruits from the list
print("Random sample of 2 fruits:", random.sample(fruits, 2))

# Additional demonstration: generating a random float
random_float = random.uniform(1.0, 10.0)
print("Random float between 1.0 and 10.0:", random_float)

#output
# Enter a number: 20
# Square root of 20 is: 4.47213595499958
# Value of pi is: 3.141592653589793
# Square of 20 is: 400.0
# Ceiling value of 7.3333 is: 8
# Floor value of 7.3333 is: 7
# Truncated value of 7.3333 is: 7
# Factorial of 8 is: 40320
# Absolute value of -10 is: 10.0
# Natural logarithm of 7.3333 is: 1.9924256192253302
# Base-10 logarithm of 7.3333 is: 0.8652994520322305
# Base-2 logarithm of 7.3333 is: 2.874462560196506  
# Round of 5.2 is: 5
# Round of 5.8 is: 6
# Random integer between 0 and 9: 7
# Random 6-digit number: 116044
# Original fruits: ['apple', 'banana', 'kiwi', 'strawberry', 'mango']
# After shuffling: ['kiwi', 'mango', 'strawberry', 'apple', 'banana']
# Randomly chosen fruit: strawberry
# Random sample of 2 fruits: ['apple', 'mango']
# Random float between 1.0 and 10.0: 3.073334750696448