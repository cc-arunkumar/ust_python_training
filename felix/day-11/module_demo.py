# import math

# num1= 23
# # print(f"Suare root of {num1} = {math.sqrt(num1)}")
# print(f"Ceil of {num1} = {math.ceil(num1)}")
# print(f"Floor of {num1} ={math.floor(num1)}")
# print(f"Trunc of {num1} ={math.trunc(num1)}")

# print(f"{math.fabs(num1)}")

# print(math.log(num1))
# print(math.log10(num1))
# print(math.log2(num1))

# print(round(7.5))
# print(round(7.4))

import random

print(random.randint(100000,999999))

fruits = ["Apple","Orange","Grapes","Banana","Guva","Pineapple"]
print("Original fruit list: ",fruits)
random.shuffle(fruits)
print(fruits)
print(random.choice(fruits))