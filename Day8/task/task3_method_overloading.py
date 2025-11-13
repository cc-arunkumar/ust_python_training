class Method:
    def add(self,a,b,c=1,d=0):
        print("the sum is:",a+b+c+d)
    def add(self,a,b=0):
        print("the sum is:",a+b)
    
    def add(self,a,b,c=10):
        print("The sum is",a+b+c)

    # def add(self,a,b,c=1,d=0):
    #     print("the sum is:",a+b+c+d)

m1 = Method()
m1.add(10,20)

# sample output
# The sum is 40 //The method which comes at last got the priority