# Class to demonstrate method overloading behavior in Python
class Method_overloading:
    # First definition of add() with three optional parameters
    def add(self, a=0, b=0, c=0):
        sum = a + b + c
        print("sum is, ",sum)
        print("add 2 is working")
    
    # Second definition of add() with two parameters
    #  This overrides the previous definition of add()
    def add(self, a, b=0):
        sum = a + b
        print("sum is " ,sum)
        print("Add 1 is working")

# Create object of Method_overloading
# fun = Method_overloading()

# Call add with two arguments
# fun.add(3, 4)

# Call add with three arguments
# fun.add(3, 4, 5)


# =========sample output==============
#sum is  7
# Add 1 is working
#sum is, 7
# Add 1 is working
