#Task : Encapsulation

#Code 
class Employee:
    def __init__(self):
        self.name ="Sohan Kumar Rout"
        self._desgination="SDE-1"
        self.__salary =50000
        
    def show_employee_details_within_same_class(self):
        print("Name : ", self.name)
        print("Designation : " ,self._designation)
        print("Salary : ", self.__salary)
emp1=Employee()
print("Name : ",emp1.name)
print("Designation : ", emp1._desgination)
# print("Salary : ", emp1.__salary)  #This will give a attribute error
print("Salart : ",emp1._Employee__salary) 

#Output
# Name :  Sohan Kumar Rout
# Designation :  SDE-1
# Salart :  50000 


        