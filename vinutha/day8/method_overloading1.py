# Demonstration of method overloading in Python
class Methodoverloading:
    # First definition of add() with 2 parameters (a, b)
    def add(self, a, b=0):
        print("2 parameter")
        sum = a + b
        print(sum)

    # Second definition of add() with 3 parameters (a, b, c)
    def add(self, a, b, c=0):
        sum = a + b + c
        print("3 parameter")
        print(sum)


# Create object of Methodoverloading
m1 = Methodoverloading()

# Call add() with 2 arguments
m1.add(10, 20)       # Output will be from the second definition (3 parameter)

# Call add() with 3 arguments
m1.add(10, 20, 30)   # Output will also be from the second definition (3 parameter)


# #3 parameter
# 30
# 3 parameter
# 60