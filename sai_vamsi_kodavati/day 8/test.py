class Test:
    def __init__(self):
        self.a = 10
        self.b = 20

    def new(self):
        self.c = 30
        self.d = 40

t1 = Test()

print(t1.__dict__)

# Sample Output

# {'a': 10, 'b': 20}