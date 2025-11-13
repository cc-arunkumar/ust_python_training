#Task : Method overloading

class Employee:
    
    def add(self,a=0,b=0):
         print(f"sum1={a+b}")
    def add(self,a=0,b=0,c=0):
         print(f"sum2={a+b+c}")
        
m1=Employee()
m1.add(2,3)
m1.add(2,3,4)

#Output
# sum2=5
# sum2=9





