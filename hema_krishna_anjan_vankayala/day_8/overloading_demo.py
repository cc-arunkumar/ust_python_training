# Define a class
class Test:
    # First add method 
    def add(self,a,b=0):
        
        print("Sum of Two Numbers")
    # Second add method
    def add(self,a,b,c=0):
        print("Sum of Three Numbers")
# Create an object of class Test
m1 = Test()
# m1.add(1) # Error

# Call add method with two arguments
m1.add(1,2)  # Output: "Sum of Three Numbers"

# Call add method with three arguments
m1.add(1,2,3) # # Output: "Sum of Three Numbers"
