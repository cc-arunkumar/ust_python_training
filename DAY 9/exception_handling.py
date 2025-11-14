import sys

print("Welcome to UST Calculator")

a=int(input("Enter Numberator :"))
b=int(input("Enter Denominator :"))


print("Add :",a+b)
print("Subtract :",a-b)
print("Multiply :",a*b)

try:
    print("Division :",a/b)

except ZeroDivisionError:
    print("Division Error :Enter Denominator > 0")

# except Exception as e:
#     print("Pleassee do see :",e)
    
print("Thanks For using UST Calculator")



"""
SAMPLE OUTPUT

Welcome to UST Calculator
Enter Numberator :10
Enter Denominator :0
Add : 10
Subtract : 10
Multiply : 0
Division Error :Enter Denominator > 0
Thanks For using UST Calculator

"""