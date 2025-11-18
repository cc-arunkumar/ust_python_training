
# import math
# from math import sqrt
# print("square of a number",math.sqrt(4))
# # print("pi value of a number",math.pi(45))
# print("power of a number",math.pow(2,5))
# print("floor of a number",math.floor(7.3))
# print("ceil of a number",math.ceil(8.2))
# print("trunc of a number",math.trunc(7.3))
# print("factorial of a number",math.factorial(8))
# print("abs of a number",math.fabs(-5))
# print("log of a number",math.log(3))
# print("log of a number",math.log10(3))
# print("log of a number",math.log2(3))


import random
otp=random.randint(0,999)
print("yor otp is:",otp)


fruits=["apple","orange","banana","kiwi","fig","pears","cherry"]
print(fruits)
random.shuffle(fruits)
print(fruits)

fruit=random.choice(fruits)
print(fruit)