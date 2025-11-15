class Employee:
    def __init__(self,id,name,dept):
        self.id=id
        self.name=name
        self.dept=dept

# Developer class inherits from Employee

class Developer(Employee):
    def __init__(self, id, name, dept,platform):
        super().__init__(id, name, dept)
        self.platform=platform

# Frontend Developer Inherits from employee
class FrontendDeveloper(Employee):
    def __init__(self, id, name, dept,technology):
        super().__init__(id, name, dept)
        self.technology=technology

# Backend Developer Inherits from Employee
class BackendDeveloper(Employee):
    def __init__(self, id, name, dept,language):
        super().__init__(id, name, dept)
        self.language=language
        
emp=Employee(101,"Shakeel","IT")
# __dict__ shows all attributes of the object in dictionary form
print(emp.__dict__)

bkddev=BackendDeveloper(102,"Sameer","IT","Python")
print(bkddev.__dict__)

#sample output
# {'id': 101, 'name': 'Shakeel', 'dept': 'IT'}

# {'id': 102, 'name': 'Sameer', 'dept': 'IT', 'language': 'Python'}
