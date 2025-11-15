#Employee Class
class Employee:
    def __init__(self):
         # Public attribute (can be accessed directly)
        self.name = "Anjan"

        # Protected attribute (by convention, should not be accessed directly outside the class,
        self._designation = "SDE - 1"
        # Private attribute (name mangling applied: stored internally as _Employee__salary)
        self.__salary = 80000
        
    #Show Method
    def show(self):
        print("Name:",self.name)
        print("Designation:",self._designation)
        print("Salary:",self.__salary)
    
a1 = Employee()
a1.show() # Acessing private vairable thorugh method
print(a1._designation)
print(a1._Employee__salary) # Accessing private variable wit mangling name

