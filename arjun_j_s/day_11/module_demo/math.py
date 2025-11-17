# from math import sqrt,pi,pow
import math

# n= int(input("Enter : "))
# print(sqrt(n))
# print(f"Value of pi : {pi}")
# print(f"Power : {pow(5,2)}")
# num = 8
# print("Floor",math.floor(num))
# print("Ceil",math.ceil(num))
# print("Trunc",math.trunc(num))
# print("Fact",math.factorial(num))
# print("Fabs",math.fabs(-100))
# print(math.log(10))
# print(math.log10(10))
# print(math.log2(10))
# print(round(7.5))
import random as r

# print(r.randint(0,9))
# print(r.randint(100000,999999))
fruits = ["Apple","Orange","Pineapple","Kiwi","Grapes","Watermelon","DragonFruit"]
print("Original is",fruits)

r.shuffle(fruits)
fruit = r.choice(fruits)
print(fruit)
