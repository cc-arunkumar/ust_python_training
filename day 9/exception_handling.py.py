# Exceptional Handling


a=int(input("Enter a: "))
b=int(input("Enter b: "))

print("Welcome to UST Calculator")

print(f"add= {a+b}")
print(f"sub= {a-b}")
print(f"mul= {a*b}")
try:
    print(f"div= {a//b}")
except ZeroDivisionError:
    print("Denominator should not be Zero")

except FileNotFoundError:
    print("File not found")

except Exception:
    print("Exception Found")


#sample Output
# Enter a: 10
# Enter b: 0
# Welcome to UST Calculator
# add= 10
# sub= 10
# mul= 0
# Denominator should not be Zero