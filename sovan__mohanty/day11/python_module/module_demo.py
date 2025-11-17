import math
print("Square root of 49",math.sqrt(49))
print("Value of pi ",math.pi)
print("square of 2 with 5 ",math.pow(2,5))
n=5
print(math.ceil(n))
print(math.floor(n))
print(math.trunc(n))
print(math.factorial(n))
n1=-8
print(math.fabs(n1))
n3=10
print(math.log(n3))
print(math.log10(n3))
print(math.log2(n3))
print(round(7.2))
print(round(7.4))
print(round(7.8))
print(abs(-8))
import random
otp=random.randint(100000,999999)
print(otp)

fruits=["apple","bananana","mango","orange","pineapple","coconut","avocado"]
print("Original fruit list ",fruits)
random.shuffle(fruits)
print(fruits)
fruits=random.choice(fruits)
print(fruits)

#Sample Execution
# Square root of 49 7.0
# Value of pi  3.141592653589793
# square of 2 with 5  32.0
# 5
# 5
# 5
# 120
# 8.0
# 2.302585092994046
# 1.0
# 3.321928094887362
# 7
# 7
# 8
# 8
# 212159
# Original fruit list  ['apple', 'bananana', 'mango', 'orange', 'pineapple', 'coconut', 'avocado']
# ['orange', 'avocado', 'apple', 'coconut', 'bananana', 'pineapple', 'mango']