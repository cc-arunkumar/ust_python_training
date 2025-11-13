#Method Overloading

class Methodoverloading:
    
    #method to add 3 parameters
    def add(self ,a,b,c=0):
        sum = a+b+c
        print(sum)
        print("The default value its taking")
     
     #method to add 2 parameters   
    def add(self,a,b=0):
        sum = a+b
        print(sum)
        print("welcome Home")
        
       
m1 = Methodoverloading()
m1.add(10,200)
m1.add(20,30)
    
#output
# 210
# welcome Home
# 50
# welcome Home