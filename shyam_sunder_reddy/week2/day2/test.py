class Test:
    def __init__(self):
        self.a=10
        self.b=20
    
    #adding attributes after creating the object
    def add_more(self):
        self.c=30
        self.d=40

t1=Test()
print(t1.__dict__)
t1.add_more()
print(t1.__dict__)
