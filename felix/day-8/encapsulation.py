class Employee:
    def __init__(self):
        # public --> No restriction 
        self.name = "Felix"
        
        # protected --> Convension : Should not be accessed outside the class or subclass
        self._designation = "SDE-1"
        
        # private --> Nmae mangaling :cannot be accessed directly outside the class
        self.__salary = 50000
        
    def show_employee_details_within_same_class(self):
        print("Name: ",self.name)
        print("Designation: ",self._designation)
        print("Salary: ",self.__salary)
        
emp1 = Employee()
print("Name: ",emp1.name)
print("Designation: ",emp1._designation) # Should't be accessed
# print("Salary: ",emp1.__salary)  # Not accessible with same name, accessible using mangled name(_ClassName__varname)
print("Salary: ",emp1._Employee__salary)