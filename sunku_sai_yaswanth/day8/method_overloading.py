# Method overloading
class Addition:
    def add(self,a=0,b=0,c=0):
        self.a=a
        self.b=b
        self.c=c
        sum=self.a+self.b+self.c
        print("The 3 args method is writing")
        
        print("addition of ",sum)
    def add(self,a=0,b=0):
        self.a=a
        self.b=b
        sum=self.a+self.b
        print("The 2args method is writing")
        
        print("addition of ",sum)


add1=Addition()
add1.add(2,3)
add2=Addition()
add2.add(3,3,3)


# The 2args method is writing
# addition of  5
# Traceback (most recent call last):
#   File "c:\Users\303459\Documents\ust\day8\method_overloading.py", line 21, in <module>
#     add2.add(3,3,3)
# TypeError: Addition.add() takes from 1 to 3 positional arguments but 4 were given