#Method Overloading
# This program attempts to demonstrate method overloading, but in Python the latest method definition overrides earlier ones.
# Hence, only the second add() method is executed, showing polymorphism through default arguments instead of true overloading.

class Methodoverloading:
    
    # Method to add 3 parameters (with default value for c)
    def add(self ,a,b,c=0):
        sum = a+b+c
        print(sum)
        print("The default value its taking")
     
    # Method to add 2 parameters
    
    def add(self,a,b=0):
        sum = a+b
        print(sum)
        print("welcome Home")
        
# Create object      
m1 = Methodoverloading()


# Call add method with two arguments
m1.add(10,200)
m1.add(20,30)
    
#output
# 210
# welcome Home
# 50
# welcome Home