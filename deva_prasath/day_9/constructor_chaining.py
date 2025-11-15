#Method Resolution order - if child class does not have any function it will call parent class

#Defining parent class
class Employee:
    def __init__(self,id,name,dept):
        self.id=id
        self.name=name
        self.dept=dept
        
    def perform_task(self):
        print("Id is",self.id)
        print("Name is ",self.name)
        print("Dept is",self.dept)


#subclass
class Developer(Employee):
    def __init__(self, id, name, dept,platform):
        super().__init__(id,name,dept)
        self.platform=platform

    #overrided function
    def platform_task(self):
        print("Platform is ",self.platform)
        
        
        
#subclass
class FrontendDev(Developer):
    #overrided function
    
    def __init__(self,id,name,dept,platform,ai_tooli):
        super().__init__(id,name,dept,platform)
        self.ai_tooli=ai_tooli
    
    def ai_tool(self):
        print("AI tool is",self.ai_tooli)

class BackenDev(Developer):
    
    def __init__(self, id, name, dept,platform,versioni):
        super().__init__(id, name, dept,platform)
        self.versioni=versioni
    
    def version(self):
        print("Version",self.versioni)


emp=Employee(101,"Dev","IT")
emp.perform_task()
print("------------------------------")
dev=Developer(201,"Raj","IT","MERN stack")
dev.perform_task()
dev.platform_task()
print("------------------------------")

fdev=FrontendDev(301,"Walter","Frontend","React","Copilot")
fdev.perform_task()
fdev.ai_tool()
print("------------------------------")

bdev=BackenDev(401,"Gokul","Backend","Django","3.33")
bdev.perform_task()
bdev.version()




#Sample output

# Id is 101
# Name is  Dev
# Dept is IT
# ------------------------------
# Id is 201
# Name is  Raj
# Dept is IT
# Platform is  MERN stack
# ------------------------------
# Id is 301
# Name is  Walter
# Dept is Frontend
# AI tool is Copilot
# ------------------------------
# Id is 401
# Name is  Gokul
# Dept is Backend
# Version 3.33