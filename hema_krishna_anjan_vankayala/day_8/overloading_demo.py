class Test:
    def add(self,a,b=0):
        
        print("Sum of Two Numbers")
    
    def add(self,a,b,c=0):
        print("Sum of Three Numbers")

m1 = Test()
# m1.add(1) # Error
m1.add(1,2)
m1.add(1,2,3)