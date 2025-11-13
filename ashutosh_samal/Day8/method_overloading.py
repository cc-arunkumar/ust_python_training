#Method overloading
#class creation
class Demo:
    def add(self,a=0,b=0):
        print("sum of 2 parameters")
        print(f"sum: {a+b}")
    def add(self,a=0,b=0,c=0):
        print("sum of 3 parameters")
        print(f"sum: {a+b+c}")
        
#object creation and function calling        
t1 = Demo()
t1.add(10,20)
t1.add(10,20,30)

#Sample Execution
# sum of 3 parameters
# sum: 30
# sum of 3 parameters
# sum: 60