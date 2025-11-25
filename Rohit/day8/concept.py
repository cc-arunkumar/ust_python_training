# Define a class named Test
class Test:
    def __init__(self):
        # Initialize attributes when object is created
        self.a = 90   # Public attribute 'a'
        self.b = 80   # Public attribute 'b'
    
    def add_more(self):
        # Add more attributes dynamically after object creation
        self.c = 87   # New attribute 'c'
        self.d = 65   # New attribute 'd'


# Create an object of Test class
t1 = Test()

# Call add_more() to add extra attributes to the object
t1.add_more()

# Print the __dict__ attribute of the object
# __dict__ is a built-in dictionary that stores all instance attributes and their values
print(t1.__dict__)

# ======================sample output==================
# {'a': 90, 'b': 80, 'c': 87, 'd': 65}
