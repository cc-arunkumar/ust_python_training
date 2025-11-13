class Test:
    def __init__(self):
        self.a=90
        self.b=80
    
    def add_more(self):
        self.c=87
        self.d=65
    
t1 =Test()
t1.add_more()
print(t1.__dict__)