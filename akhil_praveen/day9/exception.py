
print("UST calculator....")
try:
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    print("add: ",a+b)
    print("Sub: ",a-b)
    print("Multiplication: ",a*b)
    print("Division: ",a/b)
    
except ZeroDivisionError:
    print("B(dinominator) cannot be zero!")
    
except Exception as e:
    print("Exception occured!")
    print(e)
    
print("Thank you for using UST calculator!")