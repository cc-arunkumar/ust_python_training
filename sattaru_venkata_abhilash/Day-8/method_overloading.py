class Method_overloading:
    def add (self, a,b,c=0):
        print("Second Method")
        print("sum=", a+b+c)

    def add(self,a,b=0):
        print("print overloading")
        print("sum",a+b)

    # def add (self, a,b,c=0):
    #     print("Second Method")
    #     print("sum=", a+b+c)

mo1=Method_overloading()
mo1.add(10,20)
mo1.add(10,40,50)
mo1.add(10,0)            
mo1.add(30,60)


# Sample Output:
# Method Overloading in Python
# sum = 30

# Method Overloading in Python
# sum = 100

# Method Overloading in Python
# sum = 10

# Method Overloading in Python
# sum = 90
