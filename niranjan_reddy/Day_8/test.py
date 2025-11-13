class Test:
    def __init__(self):
        self.a=10
        self.b=20
    
    def add_more(self):
        self.c=30
        self.d=40

t1=Test()
t1.add_more()
print("Total values print in singke line ",t1.__dict__)


# Sample output
# Total values print in singke line  {'a': 10, 'b': 20, 'c': 30, 'd': 40}
