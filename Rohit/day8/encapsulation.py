class Employee:
    def __init__(self):
       self.name = "Rohit"
       self._designation="SDE-1"
       self.__salary=50000
       
    def show_employee_details_within_same_class(self):
        print("Name: ",self.name)
        print("designation: " ,self._designation)
        print("salary : ",self.__salary)


emp1=Employee()
# emp1.show_employee_details_within_same_class()

print("Name: ",emp1.name)
print("Designation : ",emp1._designation)
print("Salary: ",emp1._Employee__salary)
