class Test:
    def __init__(self):
        self.a=10
        self.b=20
    
    def new_elements(self):
        self.c=30
        self.d=40


t1=Test()
t1.new_elements()
print(t1.__dict__)


"""
SAMPLE OUTPUT
{'a': 10, 'b': 20, 'c': 30, 'd': 40}
"""