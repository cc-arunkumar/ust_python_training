# Method Overloading

class MetOverloading:
    def add(self,a,b,c=0):
        print("Second Method running")
        print("Sum:",a+b+c)
    
    def add(self,a,b=0):
        print("First  Method running")
        print("Sum:",a+b)

mo1=MetOverloading()
mo1.add(10,20)
mo1.add(20,30,50)