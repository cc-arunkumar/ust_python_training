# Step 1: Define a class to demonstrate method overloading behavior
class MethodOverLoading:
    # Step 2: First version of add method (will be overridden)
    def add(self,a,b=0):
        self.a=a
        self.b=b
        sum=self.a+self.b
        print("method 1 is writing:")
        print("addition of sum:",sum)
        
    # Step 3: Second version of add method (overrides the first one)
    def add(self,a,b,c=0):
        self.a=a
        self.b=b
        self.c=c
        sum=self.a+self.b+self.c
        print("method 2 is writing")
        print("addition of sum:",sum)

# Step 4: Create an object and call add method with two arguments
add1=MethodOverLoading()
add1.add(3,4)

# Step 5: Create another object and call add method with three arguments
add2=MethodOverLoading()
add2.add(3,5,8)

# sample output
# method 2 is writing
# addition of sum: 7
# method 2 is writing
# addition of sum: 16