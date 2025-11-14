# Construction Chaining
class Employee:
    def __init__(self,id,name,department):
        self.id=id
        self.name=name
        self.department=department
class Developer(Employee):
    def __init__(self, id, name, department,platform):
        super().__init__(id, name, department)  
        self.platform=platform
class FrontEndDeveloper(Developer):
    def __init__(self, id, name, department, platform,technology):
        super().__init__(id, name, department, platform)
        self.technology=technology
class BackEndDeveloper(Developer):
    def __init__(self, id, name, department, platform,language):
        super().__init__(id, name, department, platform)
        self.language=language
e1=Employee(1,"arjun reddy","It")
d1=Developer(2,"dinga","sde:1","It")
f1=FrontEndDeveloper(3,"dingi","associate developer","technical","HTML")
b1=BackEndDeveloper(4,"malli","SDE2","IT","rest api")
print("print the details of developer",d1.__dict__)

# sample output
# print the details of developer {'id': 2, 'name': 'dinga', 'department': 'sde:1', 'platform': 'It'}