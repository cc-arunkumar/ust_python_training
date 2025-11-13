#Employee Class
class Employee:
    def __init__(self):
        self.name = "Anjan"
        self._designation = "SDE - 1"
        self.__salary = 80000
        
    
    def show(self):
        print("Name:",self.name)
        print("Designation:",self._designation)
        print("Salary:",self.__salary)
    
a1 = Employee()
a1.show() # Acessing private vairable thorugh method
print(a1._designation)
print(a1._Employee__salary) # Accessing private variable wit mangling name
