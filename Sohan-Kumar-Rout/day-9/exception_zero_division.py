#Task : Zero Division Error

#Code 
a = int(input("Enter the number"))
b = int(input("Enter the another number"))

print(f"Welcome to UST Calculator ...")
print(f" Add {a+b}")
print(f" Sub {a-b}")
print(f" Multiplication {a*b}")
try:
    print(f"Division {a/b}")
except ZeroDivisionError:
    print("This is a Zero Divison error")
    
print("Thank You UST ")

#Output 
# Welcome to UST Calculator ...
#  Add 20
#  Sub 20
#  Multiplication 0
# This is a Zero Divison error
# Thank You UST 




