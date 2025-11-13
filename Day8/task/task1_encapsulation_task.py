# Scenario: UST HR Department – Employee Salary
# Management
# UST wants a very small internal Python module that handles employee salary
# safely.


#Base class
class Employee:
    def __init__(self):
        self.name = "madhan"
        self._dep = "IT"
        self.__sal = "50000"

#Get private salary
    def get_salary(self):
        return self.__sal
#set private salary
    def set_salary(self):
        if(self.__sal>0):
            return self.__sal
        else:
            print("Invalid salary!")
#try to display the private salary
    def show_info(self):
        print(f"id :{self.name}")
        print(f"department :{self._dep}")

#Testing
e1 = Employee()
print(f"Name: {e1.name}")
print(f"Department: {e1._dep}")
print("Trying to access private salary directly -> ERROR")
print(f"Accessing salary using getter: {e1.get_salary()}")

# sample output:
# Name: madhan
# Department: IT
# Trying to access private salary directly -> ERROR
# Accessing salary using getter: 50000

    
