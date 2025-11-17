# from math import sqrt,pi
# import math

# x=int(input("Enter a number: "))
# print(sqrt(x))
# print(pi)
# print(math.pow(x,2))

# x=7.3333
# print(math.ceil(x))
# print(math.floor(x))
# print(math.trunc(x))
# print(math.factorial(8))
# print(math.fabs(-10))
# print(math.log(x))
# print(math.log10(x))
# print(math.log2(x))
# print(round(5.2))
# print(round(5.8))

import random

# x=random.randint(0,9)
# print(x)

# x=random.randint(100000,999999)
# print(x)

fruits=["apple","bannana","kiwi","strawberry","mango"]
print("original fruits :",fruits)
random.shuffle(fruits)
print("after shuffling: ",fruits)
print("random: ",random.choice(fruits))
print(random.sample(fruits,2))