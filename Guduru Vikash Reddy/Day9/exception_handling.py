#Exception Handling using try except
a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
print("Welcome to ust")
print (f"add={a+b}")
print(f"sub={a-b}")

try:
    print(f"mod={a/b}")
except ZeroDivisionError:
    print("Denominator not be zero")
print("Thank you")

# sample output
# Enter a number:10
# Enter a number:0
# Welcome to ust
# add=10
# sub=10
# Denominator not be zero
# Thank you
