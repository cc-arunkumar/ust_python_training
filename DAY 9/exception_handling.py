import sys

print("Welcome to UST Calculator")

a=int(input("Enter Numberator :"))
b=input("Enter Denominator :")


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