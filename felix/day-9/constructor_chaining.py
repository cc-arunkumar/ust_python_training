# Creating parent class
class Employee:
    def __init__(self,id,name,department):
        self.id = id
        self.name = name
        self.department = department
        print("ID: ",self.id)
        print("Name: ",self.name)
        print("Department: ",self.department)
        
        
# creating child class of developer
class Developer(Employee):
    def __init__(self, id, name, department,platform):
        super().__init__(id, name, department)
        self.platform = platform
        print(self.platform)
        
    
# Creating child class of Developer
class FrontEndDeveloper(Developer):
    def __init__(self, id, name, department, platform):
        super().__init__(id, name, department, platform)
        print("Frontend developer")
        
    
# Creating child class of developer 
class BackEndDeveloper(Developer):
    def __init__(self, id, name, department, platform):
        super().__init__(id, name, department, platform)
        print("Backend developer")
        
        
# Creating objects for classes
obj1 = FrontEndDeveloper(101,"Felix","IT","APP Developer")
print("------------------------")
obj2 = BackEndDeveloper(102,"Arun","IT","Web Developer")


# output

# ID:  101
# Name:  Felix
# Department:  IT
# APP Developer
# Frontend developer      
# ------------------------
# ID:  102
# Name:  Arun
# Department:  IT
# Web Developer
# Backend developer