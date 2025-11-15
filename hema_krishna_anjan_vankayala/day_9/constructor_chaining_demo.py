#Constructor Chaining 
class Employee:
    def __init__(self,id,name,department):
        self.name = name 
        self.id = id 
        self.department = department
        
class Developer(Employee):
    def __init__(self, id, name, department,platform):
        super().__init__(id, name, department) #Super constructor used to inherit the attributes from parent class
        self.platform = platform 
    
class FrontendDeveloper(Developer):
    def __init__(self, id, name, department, platform,language,technology):
        super().__init__(id, name, department, platform)
        self.language = language
        self.technology= technology

class BackendDeveloper(Developer):
    def __init__(self, id, name, department, platform,language,technology):
        super().__init__(id, name, department, platform)
        self.language = language
        self.technology= technology
front_dev = FrontendDeveloper(1,'Ayan','Finance','Eclipse','JavaScript','React')
backend_dev = BackendDeveloper(2,'Shaym','Cyber','VSCode','Python','Django')


print(front_dev.__dict__)
print(backend_dev.__dict__)
