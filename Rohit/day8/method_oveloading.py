from abc import ABC,abstractmethod
class Method_overloading:
    def add(self, a=0, b=0, c=0):
        sum = a + b + c
        print(sum)
        print("add 2 is working")
    
    def add(self,a, b=0):
        sum = a + b
        print(sum)
        print("Add 1 is working")
# fun = Method_overloading()
   
# fun.add(3, 4)
# fun.add(3,4,5)

