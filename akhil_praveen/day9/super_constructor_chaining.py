class Employee:
    def __init__(self,id,name,dept):
        self.id = id
        self.name =name
        self.dept =dept
        
class Developers(Employee):
    def __init__(self, id, name, dept,platform):
        super().__init__(id, name, dept)
        self.platform = platform
        
class Frontend(Developers):
    def __init__(self, id, name, dept, platform,tech):
        super().__init__(id, name, dept, platform)
        self.techno =tech
    def show(self):
        print("Id: ",self.id)
        print("name: ",self.name)
        print("dept: ",self.dept)
        print("platform: ",self.platform)
        print("technology: ",self.techno)
        
class Backend(Developers):
    def __init__(self, id, name, dept, platform,lang):
        super().__init__(id, name, dept, platform)
        self.language =lang
    def show(self):
        print("Id: ",self.id)
        print("name: ",self.name)
        print("dept: ",self.dept)
        print("platform: ",self.platform)
        print("language: ",self.language)
        
        
front1 = Frontend(101,"Akhil","IT","Web developer","React")
front1.show()
back1 = Backend(102,"Arjun","IT","Web developer","Python")
back1.show()

# Output
# Id:  101
# name:  Akhil
# dept:  IT
# platform:  Web developer
# technology:  React
# Id:  102
# name:  Arjun
# dept:  IT
# platform:  Web developer
# language:  Python