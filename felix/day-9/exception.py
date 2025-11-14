
# Input numbers for doing operation
a = int(input("Enter First number: "))
b = int(input("Enter Second number: "))

# Exception handling for ZeroDivisionError
try:
    print(f"Sum : {a+b}")
    print(f"Difference : {a-b}")
    print(f"Product : {a*b}")
    print(f"Result : {a/b}")
except ZeroDivisionError as err:
    print(f"Error :{err}")
except Exception:
    print("Error occured")
    
# output

# Enter First number: 8 
# Enter Second number: 0
# Sum : 8
# Difference : 8
# Product : 0
# Error :division by zero