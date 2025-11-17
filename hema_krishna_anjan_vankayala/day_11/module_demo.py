import math

# print("Pi in Math Module:", math.pi)
# print("Square root of 16:", math.sqrt(16))
# print("Power 2^5:", math.pow(2, 5))
num = 7.000
# print(f"Ceiling of {num} :", math.ceil(num))
# print(f"Floor of {num}:", math.floor(num))
# print(f"Truncate of {num}:", math.trunc(num))
# print(f"Factorial of 5:", math.factorial(5))
# print("Fabs of -9.81:", math.fabs(-9.81))
# print("log base 10 of 1000:", math.log10(1000))
# print("log base e of 1000:", math.log(1000))
# print("log base 2 of 1024:", math.log2(1000))
# print("Round of 9.5678:", round(9.5))

import random
# for i in range(random.randint(0,100)): 
#     print("Randam Int:",random.randint(1000,9999))

fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape','orange','kiwi','mango']
print("Original list:", fruits)
print("Random choice:", random.choice(fruits))
print("Random sample of 3 fruits:", random.sample(fruits, 3))
print("Shuffled fruits:", random.shuffle(fruits), fruits)