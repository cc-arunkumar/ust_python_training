#implementing over loading

class MethodOverloading:

    def add(self,a=0,b=0):
        sum=a+b
        print("This paramteter is called when two parameters are given",sum)
        
    def add(self,a=0,b=0,c=0):
        sum=a+b
        print("This paramater is called when three parameters are given",sum)
        

mo1=MethodOverloading()
mo1.add(10,20)      
mo1.add(10,20,30)  

#o/p:
# This paramater is called when three parameters are given 30
# This paramater is called when three parameters are given 30