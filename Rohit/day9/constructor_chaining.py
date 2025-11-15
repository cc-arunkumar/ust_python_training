class Emp:
    def __init__(self,id ,name, department):
        self.id = id
        self.name=name
        self.department=department
        print(self.id," ", self.name, " ", self.department)
class Dev(Emp):
    def __init__(self,id ,name, department,platform):
        super().__init__(id,name,department)
        self.platform = platform
        print(id," ", name, " ", department," ", self.platform)

class Frontend(Dev):
    def __init__(self, id, name, department, platform,technology):
        super().__init__(id, name, department, platform)
        self.technology = technology
        print(id," ", name, " ", department," ", platform, " ",self.technology)
        
class Backend(Frontend):
    def __init__(self, id, name, department, platform, technology,language):
        super().__init__(id, name, department, platform)
        self.technology=technology
        self.language=language
        print(id," ", name, " ", department," ", platform, " ",self.technology," ",self.language)
    
    
dev1 = Dev("R1010","ROhit","IT","Fullsatck")
