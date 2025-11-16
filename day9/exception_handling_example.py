# Program that demonstrates Exception handling


a=int(input("Enter the value for numerator: "))
b=int(input("Enter the value for denominator: "))

print("    WELCOME TO UST CALCULATOR   ")
print(f" add={a + b}")
print(f" sub={a - b}")
print(f" mul={a * b}")

try:
    print(f"div = {a / b}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
    

# OUTPUT 1:
  
# Enter the value for numerator: 67
# Enter the value for denominator: 7
#     WELCOME TO UST CALCULATOR   
#  add=74
#  sub=60
#  mul=469
# div = 9.571428571428571

# OUTPUT 2:

# Enter the value for numerator: 35
# Enter the value for denominator: 0
#     WELCOME TO UST CALCULATOR   
#  add=35
#  sub=35
#  mul=0
# Error: Division by zero is not allowed.


