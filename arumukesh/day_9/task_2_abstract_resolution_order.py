from abc import ABC,abstractmethod
# importing required pkgs
# creating base class
class Emp(ABC):
    def __init__(self,emp_id,name):
        self.emp_id=emp_id
        self.name=name

# declaring the abstract method
    @abstractmethod
    def show(self):
        print("f{self.name} is a Employee")

# Creating multiple child classes 
class Mgr(Emp):
    def show(self):
        print(f"{self.name} is a manager")


class Dev(Emp):
    def show(self):
        print(f"{self.name} is a Developer")


class Tester(Emp):
    def show(self):
        print(f"{self.name} is a Tester")

# looping over the list to get output

emp_list=[Dev("101","Arun"),Mgr("101","bill"),Tester("103","Swathi")]

for emp in emp_list:
    emp.show()

# Arun is a Developer
# bill is a manager
# Swathi is a Tester