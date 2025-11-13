#Method Overloading demonstration



class MethodOverloading:

        
    def add(self,a=0,b=0):
        sum=a+b
        print("this is called when three parameters are given",sum)
        
    def add(self,a=0,b=0,c=0):
        sum=a+b+c
        print("this is called when two parameters are given",sum)
        
mo1=MethodOverloading()

mo1.add(10,20)
mo1.add(10,20,30)


# this is called when 2 parameters are given 30
# this is called when 2 parameters are given 60
