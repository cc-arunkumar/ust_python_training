#Excpetion Handling in Python
# import sys 
# sys.exit()
a=int(input())
b=int(input())
try:

    print(a/b)
except ZeroDivisionError:
    print("Zero Division Error")
    print(12/0)
except Exception as e :
    print(e)
finally:
    print("Execution Completed")

