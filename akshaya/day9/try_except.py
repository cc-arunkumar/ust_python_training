# try_except_block
a=int(input("enter a number:"))
b=int(input("enter a number:"))
print(a+b)
print(a-b)
print(a*b)

try:
    print(a/b)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
    
    
    
# sample output   
# enter a number:10
# enter a number:20
# 30
# -10
# 200
# 0.5

# enter a number:10
# enter a number:0
# 10
# 10
# 0
# Error: Cannot divide by zero!