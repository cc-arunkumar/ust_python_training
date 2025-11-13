# Method Overloading

class Method_Overloading:
    def add(self,a,b=0):
        print("First method executing")
        print("sum=",a+b)



    def add(self,a,b,c=0):
        print("Second method executing")
        print("sum=",a+b+c)

    
    
    
    def add(self,a=0,b=0,c=0,d=0):
        print("Thrid Method executing")
        print(a,b,c,d)
        print("Sum=",a+b+c+d)

mo1=Method_Overloading()
# mo1.add(10)
mo1.add(10,20)
mo1.add(10,20,30)
mo1.add(10,0,20)
mo1.add(40,50,10,57)

# Sample output
# Thrid Method executing
# 10 20 0 0
# Sum= 30
# Thrid Method executing
# 10 20 30 0
# Sum= 60
# Thrid Method executing
# 10 0 20 0
# Sum= 30
# Thrid Method executing
# 40 50 10 57
# Sum= 157