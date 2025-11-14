# Encapsulation Task
#  Scenario: UST HR Department – Employee Salary 
# Management
#  UST wants a very small internal Python module that handles employee salary 
# safely.
#  Why?
#  Because salary is sensitive, and HR must protect it so:
#  nobody can set salary to a negative number
#  nobody can view salary without permission
#  the internal raw salary value must not be exposed directly outside the class



#Defining class employee
class Employee:
    #initialising connstructor
    def __init__(self,name,_department,__salary):
        self.name=name
        self._department=_department
        self.__salary=__salary
        
    #getter method for private variable
    def get_salary(self):
        return self.__salary

    #salary incremented
    def set_salary(self,amt):
        if amt>0:
            self.__salary+=amt
    
    #method to show the attributes
    def show(self):
        print(f"Name: ",self.name)
        print(f"Department: ",self._department)
        

#object created
emp1=Employee("Kani","IT",10000)

#calling obj method
emp1.show()


try:
    #trying to access private variable
    print(emp1.__salary)  #AttributeError: 'Employee' object has no attribute '__salary'. Did you mean: 'get_salary'?

except Exception as e:
    print(f"Trying to access private salary directly: ",e)


emp1.set_salary(20000)
print(f"Accessing salary using getter:",emp1.get_salary())


#Sample output

# Name:  Kani
# Department:  IT
# Trying to access private salary directly:  'Employee' object has no attribute '__salary'
# Accessing salary using getter: 30000