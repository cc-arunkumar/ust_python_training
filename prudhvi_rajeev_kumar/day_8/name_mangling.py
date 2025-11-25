class Employee:
    def __init__(self):
        self.name = "Prudhvi"                       #This is a Public Variable.
        self._designation = "SDE - 1"               #This is a protected Variable.
        self.__salary = 50000                       #This is a Private variable
    
    def get_employee_details(self):
        print("Name : ", self.name)
        print("Designamtion is : ", self._designation)
        print("Salary is : ", self.__salary)
        

c1 = Employee()
print("Name : ", c1.name)
print("Designation is : ", c1._designation)
print("Salary is : ", c1._Employee__salary)          #Here we are doing the Name Mangling.




#Sample Output :
# Name :  Prudhvi
# Designation is :  SDE - 1
# Salary is :  50000
