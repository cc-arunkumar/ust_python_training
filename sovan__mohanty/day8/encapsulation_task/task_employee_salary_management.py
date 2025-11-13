#Task Employee Salary Management

#Create class Employee
class Employee:
    def __init__(self):
        self.name="Sovan"
        self._department="IT"
        self.__salary=75000
    def get_salary(self):
        return self.__salary
    def set_salary(self,amount):
        if(amount>0):
            self.__salary=float(input("Enter the new salary"))
    def show_info(self):
        print("Name: ",self.name)
        print("Department: ",self._department)
e=Employee()
e.show_info()
try:
    print(e.__salary)

except AttributeError:
    print("Trying to access private salary directly -> ERROR")
e.set_salary(0)
print("Accessing salary using getter: ",e.get_salary())

#Sample Execution
# Name:  Sovan
# Department:  IT
# Trying to access private salary directly -> ERROR
# Accessing salary using getter:  75000
        