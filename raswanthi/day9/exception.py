#Exception Handling using Try and Except

a=int(input("Enter num1:"))
b=int(input("Enter num2:"))
print("sum : ",a+b)
print("diff : ",a-b)
print("multiplied : ",a*b)

# try:
#     print("Divide",a/b)
# except Exception:                  
#     print("Can't divide by zero")
# except ZeroDivisionError:
#     print("Cant divide by zero")

# Output:
'''
Enter num1:2
Enter num2:0
sum : 2
diff : 2
multiplied : 0
Can't divide by zero
'''

try:
    print("Divide",a/b)

except ZeroDivisionError:
    print("Cant divide by zero")
except Exception:
    print("Can't divide by zero")


#output:   
'''
Enter num1:3
Enter num2:0
sum : 3
diff : 3
multiplied : 0
Cant divide by zero
'''