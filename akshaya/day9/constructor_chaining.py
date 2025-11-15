# constructor chaining
class Employee():
    def __init__(self,id,name,dept):
        self.id=id
        self.name=name
        self.dept=dept
class Dev(Employee):
    def __init__(self,id,name,dept,platform):
        super().__init__(id,name,dept)
        self.platform=platform
    
class Frontend(Employee):
    def __init__(self,id,name,dept,technology):
        super().__init__(id,name,dept)
        self.technology=technology
        
class Backend(Employee):
    def __init__(self,id,name,dept,tech1):
        super().__init__(id,name,dept)
        self.tech1=tech1
    
d1=Dev(1,"arun","it","cyber")
fd1=Frontend(2,"tina","cs","python")
bd1=Backend(3,"milo","ai","java")
print(d1.__dict__)
print(fd1.__dict__)
print(bd1.__dict__)


# sample output
# {'id': 1, 'name': 'arun', 'dept': 'it', 'platform': 'cyber'}
# {'id': 2, 'name': 'tina', 'dept': 'cs', 'technology': 'python'}
# {'id': 3, 'name': 'milo', 'dept': 'ai', 'tech1': 'java'}
        