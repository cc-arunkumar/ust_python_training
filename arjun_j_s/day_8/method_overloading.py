class MO:
    def add(self,a=0,b=0,c=0):
        print("Method 2 Executed")
        print("Sum is :",a+b+c)

    def add(self,a=0,b=0):
        print("Method 1 Executed")
        print("Sum is :",a+b)


m1 = MO()
m1.add()
m1.add(1,2)
m1.add(1,2,3)