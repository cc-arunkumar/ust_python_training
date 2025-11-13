# class MethodOverloading:
#     def add(self,a,b=0):
#         print("sum:",a+b)
#         print("add1 is working")
#     def add(self,a,b,c=0):
#         print("sum:",a+b+c)
#         print("add2 is working")
# mo1=MethodOverloading()
# mo1.add(10,20)
# mo1.add(30,20,40)

class MethodOverloading:
   
    def add(self,a=0,b=0,c=0):
        print("sum:",a+b+c)
        print("add2 is working")
        
    def add(self,a=0,b=0):
        print("sum:",a+b)
        print("add1 is working") 
mo1=MethodOverloading()
mo1.add(10,20)
mo1.add(30,20,40)


