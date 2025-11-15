# Exception Handling Demo

a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))

print("Welcome to ust calculator")

print(f"add= {a+b}")
print(f"sub= {a-b}")
print(f"mul= {a*b}")

# using try except block for encountering Exception

try:
    print(f"div={a/b}")
except ZeroDivisionError:
    print("Denominator cannot be zero")
except FileNotFoundError:
    print("File doen't exists")

except Exception:
    print("The value of b must not be zero")

print("Thank you")

    
# Sample output
# Enter the value of a:12
# Enter the value of b:0
# Welcome to ust calculator
# add= 12
# sub= 12
# mul= 0
# Denominator cannot be zero
# Thank you