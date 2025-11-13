class Overloading:
    def __init__(self):
        pass
    
    def add(self,a,b,c):
        print("printing funct2")
        self.sum=a+b+c
        print("Add:",self.sum)
        
    def add(self,a,b):
        print("printing funct1")
        self.sum=a+b
        print("Add:",self.sum)
    


o1=Overloading()
o1.add(10,20)
o1.add(10,20) 
o1.add(10,30)      
        
        
# printing funct1
# Add: 30
# printing funct1
# Add: 30
# printing funct1
# Add: 40