class Employee:
    def __init__(self,id,name,dept):
        self.id=id
        self.name=name
        self.dept=dept
class Developer(Employee):
    def __init__(self, id, name, dept,platform):
        super().__init__(id, name, dept)
        self.platform=platform
        
class FrontEnd(Developer):
    def __init__(self, id, name, dept,platform,tecnology):
        super().__init__(id, name, dept,platform)
        self.tecnology=tecnology

class BackEnd(Developer):
    def __init__(self, id, name, dept,platform,language):
        super().__init__(id, name, dept,platform)
        self.language=language

        

emp=BackEnd(1,"nani","IT","web","python")
print(emp.__dict__)