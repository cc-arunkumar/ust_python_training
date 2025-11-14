class test:
    
    def __init__(self,a=16,b=12,c=99):
        self.a=a
        self.b=b
        self.c=c
        
    def add(self,a,b,c):
        print("The sum is ",self.a+self.b+self.c)
        print("Second add method")
    
    def add(self,a,b):
        print("The sum is",self.a+b)
        print("First add method")
            
m1=test()
m1.add(5,10)