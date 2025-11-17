import math
import random


print("Square root of 4 is:",math.sqrt(4))
print("usage of pi in math",math.pi)
print("pow in math",math.pow(2,5))
print("floor in math:",math.floor(8.2))
print("ceil in math: ",math.ceil(8.2))
print("truncate in math:",math.trunc(8.2))
print("factorial in math:",math.factorial(6))
print("fabs in math gives positive:",math.fabs(-82))
print("log in math:",math.log(8))
print("log in math for base 10:", math.log10(8))
print("round in math:", round(7.8))
otp=random.randint(100000,999999)
print("randint in random: ", otp)

fruits=["Apple","orange","Banana","Mango","pineapple","grapes",]
print("original fruits list",fruits)
random.shuffle(fruits)
print("shuffle in random:",fruits)
fruit=random.choice(fruits)
print("choice in random:",fruit)


