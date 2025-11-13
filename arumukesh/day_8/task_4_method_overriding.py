class Employee:
    def __init__(self,name):
        self.name=name
    def disp(self):
        print(f"{self.name} is an employee")
class Developer(Employee):
    def __init__(self,name):
        self.name=name
    def disp(self):
        print(f"{self.name} is an developer")

class DevManager(Developer):
    def __init__(self,name):
        self.name=name
    def disp(self):
        print(f"{self.name} is an Manager")

emp1=DevManager("arun")
emp1.disp()


emp2=Developer("anoushka")
emp2.disp()
