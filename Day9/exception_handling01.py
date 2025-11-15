a = int(input("Enter the numerator:"))
b = int(input("Enter the denominator:"))

#Try some arithmetic operations
try:
    print(f"Sum : {a+b}")
    print(f"Difference : {a-b}")
    print(f"Product : {a*b}")
    print(f"Result : {a/b}")

#handling error
except ZeroDivisionError as e:
    print(f"Error :{e}")

# sample output:
# Enter the numerator:10
# Enter the denominator:0
# Sum : 10
# Difference : 10
# Product : 0
# Error :division by zero


