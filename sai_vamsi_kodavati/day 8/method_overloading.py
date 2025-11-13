# Method Overloading

class MethodOverloading:
    def add(self,a,b,c=0):
        print("Method Overloading1")
        print("Sum:",a+b+c)

    def add(self,a,b=0):
        print("Method Overloading2")
        print("sum:",a+b)

m1 = MethodOverloading()
m1.add(10,20)
m1.add(10,20)
m1.add(50,50)

# Method Overloading2
# sum: 60
# Method Overloading2
# sum: 30
# Method Overloading2
# sum: 100


