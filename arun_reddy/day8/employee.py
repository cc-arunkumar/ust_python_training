class Employee:
    def __init__(self):
        # public 
        self.name="Arun"
        # protected
        self._designation="SDE-1"
        # private 
        self.__salary=50000
    
    # can be accessed within the same class 
    def show_employee_details_within_same_class(self):
        print("Name :",self.name)
        print("Designation:",self._designation)
        print("Salary:",self.__salary)
    
    
emp1=Employee()
print("name: ",emp1.name)
print("designation:",emp1._designation)
print("salary:",emp1._Employee__salary) # cannot be acces directly by name ,accesed by using name mangling concept

# sample execution
# name:  Arun
# designation: SDE-1
# salary: 50000
        