

class Employee:
    def __init__(self, name, department):
        self.name=name
        self.department=department
    
    def get_details(self):
        print(f"Employee name : {self.name}")
        print(f"Employee department : {self.department}")
        
class Developer(Employee):
    def __init__(self, name, department ,platform):
        super().__init__(name, department)
        self.platform =platform
        
        
            
class FrontEnd(Developer):
    def __init__(self, emp_id, name, department, platform,technology):
        super().__init__(emp_id, name, department, platform)
        self.technology= technology
        
class Backend(Developer):
    def __init__(self, name, department, platform,language):
        super().__init__(name, department, platform)
        self.language=language

d1=Developer("Sohan","IT","Frontend")
print(f"{d1.name} {d1.department},{d1.platform}")

#Output
# Sohan IT,Frontend