class Employee:
    def __init__(self,id,name,department):
        self.id=id
        self.name=name
        self.department=department
        
        # class develoepr extends employee
class Developer(Employee):
    def __init__(self, id, name, department,platform):
        super().__init__(id, name, department)
        self.platform=platform
      

        
        # class frontend extends develoepr
class Frontend(Developer):
    def __init__(self, id, name, department, platform,technology):
        super().__init__(id, name, department, platform)
        self.technology=technology
        

        
    # class backend extends to developer
class Backend(Developer):
    def __init__(self, id, name, department, platform,language):
        super().__init__(id, name, department, platform)
        self.langauge=language
        



# creating and calling the object instances with the paramters 
employee=Employee(8901,"Arun","Finance")
print(employee.__dict__)
print("====================================")
developer=Developer(8901,"Arun","Finance","Android developer")
print(developer.__dict__)
print("====================================")
frontend=Frontend(8901,"Arun","Finance","Android developer","Angular")
print(frontend.__dict__)
print("====================================")
backend=Backend(8901,"Arun","Finance","Android developer","Nodejs")
print(backend.__dict__)
print("====================================")

# sample execution 
# {'id': 8901, 'name': 'Arun', 'department': 'Finance'}
# ====================================
# {'id': 8901, 'name': 'Arun', 'department': 'Finance', 'platform': 'Android developer'}
# ====================================
# {'id': 8901, 'name': 'Arun', 'department': 'Finance', 'platform': 'Android developer', 'technology': 'Angular'}
# ====================================
# {'id': 8901, 'name': 'Arun', 'department': 'Finance', 'platform': 'Android developer', 'langauge': 'Nodejs'}
# ====================================