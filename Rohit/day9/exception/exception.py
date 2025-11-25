a = 10   # Assign value 10 to variable a
b = 0    # Assign value 0 to variable b

print("welcome to Ust calculator app")   # Print welcome message

try:
    # Try to perform integer division
    val = a // b
except ZeroDivisionError:
    # Catch the ZeroDivisionError exception if b = 0
    # Print the exception class itself (not the message)
    print(ZeroDivisionError)



# # ===========sample output===============
# welcome to Ust calculator app
# <class 'ZeroDivisionError'>