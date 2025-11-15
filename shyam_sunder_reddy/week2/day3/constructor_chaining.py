#Parent classs for constructor chaining
class Employee:
    def __init__(self,id,name,department):
        self.id=id
        self.name=name
        self.department=department

#Child class
class Developer(Employee):
    def __init__(self,id,name,department,platform):
        #Contructor chaining
        super().__init__(id,name,department)
        self.platform=platform

#child class 
class FrontEndDev(Developer):
    def __init__(self,id,name,department,platform,technology):
        #Contructor chaining
        super().__init__(id,name,department,platform)
        self.technology=technology
        
#Child class
class BackEndDev(Developer):
    def __init__(self,id,name,department,platform,languagae):
        #Contructor chaining
        super().__init__(id,name,department,platform)
        self.language=languagae
    
e1=Employee(1,"shyam","IT")
d1=Developer(2,"ram","IT","web")
f1=FrontEndDev(3,"bheem","IT","web","react")
b1=BackEndDev(4,"anjan","IT","web","python")

print(e1.__dict__)
print(d1.__dict__)
print(f1.__dict__)
print(b1.__dict__)

#Sample output
# {'id': 1, 'name': 'shyam', 'department': 'IT'}
# {'id': 2, 'name': 'ram', 'department': 'IT', 'platform': 'web'}
# {'id': 3, 'name': 'bheem', 'department': 'IT', 'platform': 'web', 'technology': 'react'}
# {'id': 4, 'name': 'anjan', 'department': 'IT', 'platform': 'web', 'language': 'python'}

