class Employee:
    def __init__(self):
        #public 
        self.name="shyam"
        #protected
        self._designation="SDE-1"
        #private
        self.__salary=425000
    
    def show_details(self):
        print("Name: ",self.name)
        print("Designation: ",self._designation)
        print("salary: ",self.__salary)
    
emp1=Employee()
print("name: ",emp1.name)
#should not be accesed
print("Designation: ",emp1._designation)
# print("Salary: ",emp1.__salary)
#calling with mangaled name
print("Salary: ",emp1._Employee__salary)










