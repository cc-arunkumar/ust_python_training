class MO:
    def __init__(self):
        pass
    
    def add(self, a, b, c=0):
        self.sum = a+b+c
        print("Running second function : ", self.sum)
        
    def add(self, a, b=0):
        self.sum = a + b
        print("Running 1st function :", self.sum)
    
mo1 = MO()
mo1.add(10,20)
mo1.add(10,10)
mo1.add(10,20,30)
