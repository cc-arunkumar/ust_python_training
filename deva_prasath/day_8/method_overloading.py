class test:
    
    def __init__(self, a=16, b=12, c=99):
        # Constructor initializing default values
        self.a = a
        self.b = b
        self.c = c
        
    def add(self, a=None, b=None, c=None):
        # This method adds self.a, self.b, and self.c if no arguments are passed
        if a is None and b is None and c is None:
            print("The sum is", self.a + self.b + self.c)
            print("Sum using default values")
        # This method adds self.a and b if only two arguments are passed
        elif c is None:
            print("The sum is", self.a + b)
            print("Sum using first method")
        # This method adds a, b, and c if all three arguments are provided
        else:
            print("The sum is", a + b + c)
            print("Sum using second method")
    
# Create an object of class test with default values
m1 = test()

# Call the 'add' method with 2 arguments, triggering the first method
m1.add(5, 10)

# Call the 'add' method without any arguments, triggering the method with default values
m1.add()

# Call the 'add' method with 3 arguments, triggering the second method
m1.add(5, 10, 15)
