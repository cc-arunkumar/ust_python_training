#METHOD OVERLOADING

class mo:
    def __init__(self):
        pass
    
    #same name
    def add(self,a=1,b=2,c=3,d=4):
        print(a+b+c+d)
        print("Method 3 Called")

    def add(self,a=0,b=0,c=10):
        print(a+b+c)
        print("Method 2 Called")

    def add(self,a=0,b=0):
        print(a+b)
        print("Method 1 Called")
    
    
    
    

mo1=mo()
mo1.add(1,1)

"""
SAMPLE OUTPUT

2
Method 1 Called
"""
# No overloading -> only last method is always called or we will get error 