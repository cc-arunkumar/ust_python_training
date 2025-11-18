# import math

# # Input
# a = float(input("Enter the value of a: "))
# b = 1.78

# # Square root
# print(f"Square root of a: {math.sqrt(a)}")

# # Value of pi
# print(f"Value of pi: {math.pi}")

# # Power (a^2)
# print(f"a raised to power 2: {math.pow(a, 2)}")

# # Absolute value using fabs
# print(f"Absolute value of a: {math.fabs(a)}")

# # Factorial (only works for integers)
# if a.is_integer() and a >= 0:
#     print(f"Factorial of a: {math.factorial(int(a))}")
# else:
#     print("Factorial is only defined for non-negative integers.")

# # Ceiling and Floor
# print(f"Ceiling of a: {math.ceil(a)}")
# print(f"Floor of a: {math.floor(a)}")

# #logging of number

# print(f"log of a: {math.log(a)}")
# print(f"log10 of a: {math.log10(a)}")
# print(f"log2x of a: {math.log2(a)}")

# print(f"round of a: {round(b)}")

import random

otp = random.randint(100000,999999)  #Four digit OTP
print(f"Your OTP is: {otp}")

list1 = ["apple","mango","grape","orange"]
print(f"Original fruit list:{list1}")
random.shuffle(list1)
print(f"Shuffled fruit list:{list1}")
choice = random.choice(list1)
print(f"Fruits choice is: {choice}")