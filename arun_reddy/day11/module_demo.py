import math
num=int(input("ENter a number"))
print(f"square root of a number {math.sqrt(num)}")
print(f"PI value is {math.pi}")
# power and exponent 
number=int(input("Enter the power"))
print(f"Th power iof the number {math.pow(2,number)}")
# seal,trunk and floor
value=7.9087
print(f"the math ceil value us {math.ceil(value)}")
print(f"Th floor value is {math.floor(value)}")
print(f"teh trunk value is {math.trunc(value)}")
# Fcatorial of a number
val=4
print(f"The factorial of number{math.factorial(val)}")
nums=-90
print(f"Th efabs value is {math.fabs(nums)}")
print(math.log(90))
print(round(7.2))
print(round(7.8))
print(round(7.5))

import random
value=random.randint(100000,999999)
print(value)

fruits=["Apple","Banana","Grapes","PineApple","Oranges"]
print(f"Original fruits list ={fruits}")
item=random.shuffle(fruits)
print(f"Shuffled fruits:{fruits}")
fruit=random.choice(fruits)
print(fruit)

