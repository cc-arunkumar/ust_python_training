import math
import random as rand
from math import sqrt
a=10
num=7.5
ne=-1.989
print(math.sqrt(a))
print(math.pi)
print(math.pow(a,3))
print(math.ceil(num))
print(math.floor(num))
print(math.trunc(num)) #removes decimal
print(math.factorial(a))
print(math.fabs(ne))  #return postive
print(math.fabs(num))
print(math.log(a))
print(math.log10(a))
print(round(num)) #if 7.5 then 8 else 7.4 
print(rand.randint(0,9)) #random numbers
print(rand.randint(1000,9999))
print(rand.randint(100000,999999)) 

fruits=["Pineapple","dragon",'apple','banana','toamato','orange','melon']
print("Original fruit list",fruits)
rand.shuffle(fruits)
print(fruits)
print(rand.choice(fruits))