class Test:
    def add(self,a=0,b=0,c=0):
        print("three parameters: ",a+b+c)
        
    def add(self,a=0,b=0):
        print("two parameters: ",a+b)
    

t=Test()
#t.add(10) # produces error
t.add(10,20)
t.add(10,20,30)

