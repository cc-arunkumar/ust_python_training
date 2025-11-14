class Employee:
    def __init__(self,id,name,dept):
        self.id=id
        self.name=name
        self.dept=dept

#calling Developer class

class Developer(Employee):
    def __init__(self, id, name, dept,platform):
        super().__init__(id, name, dept)
        self.platform=platform

#calling Frontend Developer
class FrontendDeveloper(Employee):
    def __init__(self, id, name, dept,technology):
        super().__init__(id, name, dept)
        self.technology=technology

#calling Backend Developer
class BackendDeveloper(Employee):
    def __init__(self, id, name, dept,language):
        super().__init__(id, name, dept)
        self.language=language
        
emp=Employee(101,"Shakeel","IT")
print(emp.__dict__)

bkddev=BackendDeveloper(102,"Sameer","IT","Python")
print(bkddev.__dict__)

#sample output
# {'id': 101, 'name': 'Shakeel', 'dept': 'IT'}
# {'id': 102, 'name': 'Sameer', 'dept': 'IT', 'language': 'Python'}