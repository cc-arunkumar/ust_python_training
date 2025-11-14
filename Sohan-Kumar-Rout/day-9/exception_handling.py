
#Task: Zero divison error handling

a=int(input("Enter the numerator"))
b=int(input("Enter the denominator"))
print("Welcome to the UST calculator app")
print(f"add: {a+b}")
print(f"sub: {a-b}")
print(f"product: {a*b}")
try:
    print(f"divison: {a/b}")
except ZeroDivisionError:
    print("This is a zero divison error")
print("Thank you for using UST calculator")

#Sample Execution
# Enter the denominator0
# add: 4
# sub: 4
# This is a zero divison error
