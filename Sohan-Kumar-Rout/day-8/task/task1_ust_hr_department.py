#Task : UST HR Department

#Code 
class Employee:
    def __init__(self,name,_department,__salary):
        self.name=name
        self._department=_department
        self.__salary=__salary
        
    def get_salary(self):
        return self.__salary
        
    def set_salary(self,amount):
        if amount >0 :
           self.__salary=float(input("Enter your salary :"))
            
    def show_info(self):
        print(f"Employee Name : {self.name} has department {self._department}")
    
emp1=Employee("Sohan","IT",45000)
emp1.show_info()
try :
    print(emp1.__salary)
except AttributeError:
    print("Tried Printing salary directly -> ERROR")
emp1.set_salary(0)
print(f"Acessing salary using getter : {emp1.get_salary()}")
    

#Output
# Employee Name : Sohan has department IT
# Tried Printing salary directly -> ERROR
# Acessing salary using getter : 45000
