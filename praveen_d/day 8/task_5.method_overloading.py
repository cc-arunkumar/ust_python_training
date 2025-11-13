class MethodOverloading:
    def add(self,a=0,b=0,c=0):
        print("Sum2 =",a+b+c)
    def add(self,a=0,b=0):
        print("Sum1 = ",a+b)
    
        
mo1 = MethodOverloading()
mo1.add(10,20)
mo1.add(10,20,30)