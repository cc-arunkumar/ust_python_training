#A simple task using Constructor Chaining concept

class Employee:
    def __init__(self,id,name,dept):
        self.id=id 
        self.name=name 
        self.dept=dept 
        
class Developer(Employee):
    def __init__(self, id, name, dept, platform):
        super().__init__(id, name, dept) #constructor chaining
        self.platform=platform
        
class FrontEndDeveloper(Developer):
    def __init__(self, id, name, dept, platform,technology):
        super().__init__(id, name, dept, platform)
        self.technology=technology
        
class BackEndDeveloper(Developer):
    def __init__(self, id, name, dept, platform,language):
        super().__init__(id, name, dept, platform)
        self.languge=language
        
#giving inputs for each class
emp1=Employee("E01","Nisha","IT")
dev1=Developer("E02","Ravi","IT","Python-Fullstack")
frontdev=FrontEndDeveloper("E03","John","IT","Python-Fullstack","React")
backdev=BackEndDeveloper("E04","Jery","IT","Python-fullstack","Python")

print(emp1.__dict__)
print(dev1.__dict__)
print(frontdev.__dict__)
print(backdev.__dict__)


#output:
'''
{'id': 'E01', 'name': 'Nisha', 'dept': 'IT'}
{'id': 'E02', 'name': 'Ravi', 'dept': 'IT', 'platform': 'Python-Fullstack'}
{'id': 'E03', 'name': 'John', 'dept': 'IT', 'platform': 'Python-Fullstack', 'technology': 'React'}{'id': 'E04', 'name': 'Jery', 'dept': 'IT', 'platform': 'Python-fullstack', 'languge': 'Python'}
'''

