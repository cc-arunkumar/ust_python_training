class Test:
    def __init__(self):
        self.a = 10
        self.b = 20
    
    def add_method(self):
        self.c = 30
        self.d = 40
        

t1 = Test()
print(t1.__dict__)
t1.add_method()
print(t1.__dict__)

