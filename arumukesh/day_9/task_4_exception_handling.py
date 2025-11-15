a=10
b=0

# Catching the possible exception 
try:
    print(a/b)
except ZeroDivisionError:
    print("division by zero")