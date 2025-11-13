#Task UST HR Employee salary Management

#class employee creation
class Employee:
    def __init__(self,name,department,salary):
        self.name = name
        self._departmrnt = department
        self.__salary = salary
    
    #function to get salary
    def get_salary(self):
        print(f"Accessing salary using getter:{self.__salary}")
    
    #function to set salary
    def set_salary(self,amount):
        if amount>0:
            self.__salary = amount
            print("Salary updated")
    
    #function to print information
    def show_info(self):
        print(f"Name:{self.name}")
        print(f"Department:{self._departmrnt}")

#object creation and function calling
emp1 = Employee("Ashutosh","Developer",30000)
emp1.show_info()
emp1.get_salary()
emp1.set_salary(50000)
emp1.get_salary()
# print(emp1.__salary)    #AttributeError: 'Employee' object has no attribute '__salary'. Did you mean: 'get_salary'?



# Sample Execution
# Name:Ashutosh
# Department:Developer
# Accessing salary using getter:30000
# Salary updated
# Accessing salary using getter:50000
# AttributeError: 'Employee' object has no attribute '__salary'. Did you mean: 'get_salary'?