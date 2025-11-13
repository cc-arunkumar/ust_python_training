class Employee:
    def __init__(self,name,_department,__salary):
        self.name="Taniya"
        self._department="IT"
        self.__salary=50000
        
    def getsalary(self):
        print("Salary :{self.__salary}")
        
    
    def setsalary(self,amount):
        if amount > 0:
            self.salary = amount
            print(f"Updated salary is {amount}")
        else:
            print("Invalid amount! salary should be greater than 0")
    def show_info(self):
        print(f"Name : {self.name}, department : {self._department}")
        print(f"Salary :{self._Employee__salary}")
        
emp1=Employee("Taniya","IT",50000)
emp1.show_info()
try:
    print(emp1.__salary)
except AttributeError:
    print("Trying to access private salary directly = ERROR")
    
emp1.setsalary(60000)
print(f"Accessing salary using getter: {emp1.getsalary()}")
# print(emp1.name)
# print(emp1._Employee__salary)
# print(emp1._department)

        
            