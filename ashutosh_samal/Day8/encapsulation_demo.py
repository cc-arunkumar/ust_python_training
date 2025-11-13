#encapsulation example
#employee class creation
class Employee:
    def __init__(self):
        self.name = "Ashutosh"
        self._designation = "SDE-1"
        self.__salary = 30000
    
    #function to print details
    def show_employee_details_within_same_class(self):
        print(f"Name:,{self.name}")
        print(f"Designation: {self._designation}")
        print(f"Salary: {self.__salary}")

#object creation        
emp1 = Employee()

#print details of employee
print("Name: ",emp1.name)
print("Salary: ",emp1._designation)
print("Salry: ",emp1._Employee__salary)



#Sample Execution
# Name:  Ashutosh
# Salary:  SDE-1
# Salry:  30000