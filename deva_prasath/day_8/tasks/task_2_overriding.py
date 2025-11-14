#Defining parent class
class Employee:
    def show(self):
        print("Employee class is printed")

#sub class
class Developer:
    #overrided function
    def show(self):
        print("Developer class is printed")

#subclass
class Manager:
    #overrided function
    def show(self):
        print("Manager class is printed")
        
        
a=Employee()
b=Developer()
c=Manager()
#parent class call
a.show()
#subclass call
b.show()
#another sub class call
c.show()