# 🧩 Question:
# Create a class MethodOverloading with a method 'add' that can handle:
# - Two arguments (a, b)
# - Three arguments (a, b, c)
# Demonstrate method overloading using default arguments or *args,
# since Python does not support traditional method overloading.

# Here 
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
# Output
# sum: 30
# add2 is working
# sum: 90
# add2 is working

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
# Output
# mo1.add(30,20,40)
#     ~~~~~~~^^^^^^^^^^
# TypeError: MethodOverloading.add() takes from 1


