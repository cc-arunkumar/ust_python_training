a=int(input("Enter the value:"))
b=int(input("Enter the value:"))

def add(a,b):
    print("Addition:")
    print(a+b)


def div(a,b):
        print("Division:")
        try:
            print(a/b)
        except ZeroDivisionError:
            print("Dinominator cannot be zero")

add(a,b)
div(a,b)

# sample output:
# Enter the value:10
# Enter the value:5
# Addition:
# 15
# Division:
# 2.0
# ---------------------------------------------------
# Enter the value:100
# Enter the value:0
# Addition:
# 100
# Division:
# Dinominator cannot be zero