class Employee:
    def __init__(self, name, _department, __salary):
        self.name = name
        self._department = _department
        self.__salary = __salary
            
    def get_salary(self):
        print("Salary is : ", self.__salary)
        
    def show_info(self):
        print("Name is : ", self.name)
        print("Department is :", self._department)
    
    def update_salary(self, amount):
        self.amount = amount
        if self.amount > 0:
            self.__salary = self.amount
            
    def updated_salary(self):
        print("Updated Salary is : ",self.__salary)


e1 = Employee("Prudhvi", "HR", 50000)
e1.show_info()
e1.update_salary(75000)
e1.updated_salary()
try:
    print(e1.__salary)
except AttributeError:
    print("AttributeError: 'Employee' object has no attribute 'get_salary'")



#Console Output:
# Name is :  Prudhvi
# Department is : HR
# Updated Salary is :  75000
# AttributeError: 'Employee' object has no attribute 'get_salary'
    
