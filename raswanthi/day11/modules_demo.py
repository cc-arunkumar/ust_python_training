#Modules Implementation
import math 

from math import sqrt
print("Square root of 4: ",math.sqrt(4))
print("Pi value: ",math.pi)
print("Power: ",math.pow(2,5))
print("Floor: ",math.floor(8.2))
print("Ceil: ",math.ceil(8.2))
print("Trunc: ",math.trunc(8.2)) #removes decimal and shows integer
print("Factorial: ",math.factorial(8))
print("Absolute value:",math.fabs(-12)) #absolute val
x=2
print(math.log(x))
print(math.log10(x))
print(math.log2(x))
print(round(7.2))
print(round(7.8))
print(round(7.4))


# import random
# otp=random.randint(0,9)
# print(otp)

import random
otp=random.randint(1000,9999)
print("Your OTP is:",otp)

fruits=["apple","banana","kiwi","pomegranate","papaya","mango","guava","pineapple"]
random.shuffle(fruits)

fruit=random.choice(fruits) #print random fruit
print(fruit)