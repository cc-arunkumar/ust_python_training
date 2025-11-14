#Here both Constuctor and Method Chaining Examples are provided.
class Employee:
    def __init__(self, id, name, dept):
        self.id = id
        self.name = name
        self.dept = dept        
    def display_info(self):
        print(f"Employee ID: {self.id}, Name: {self.name}, Department: {self.dept}")
        
class Developer(Employee):
    def __init__(self, id, name, dept, platform):
        super().__init__(id, name, dept)
        self.platform = platform        
    def display_info(self):
        super().display_info()
        print(f"Developer works on the platform {self.platform}")

class FrontendDeveloper(Developer):
    def __init__(self, id, name, dept, platform, framework):
        super().__init__(id, name, dept, platform)
        self.framework = framework        
    def display_info(self):
        super().display_info()
        print(f"Frontend Developer uses the framework {self.framework}")

class BackendDeveloper(Developer):
    def __init__(self, id, name, dept, platform, language):
        super().__init__(id, name, dept, platform)
        self.language = language        
    def display_info(self):
        super().display_info()
        print(f"Backend Developer works with the database {self.language}")

fe1 = FrontendDeveloper(101, "Alice", "Development", "Web", "React")
fe1.display_info()
print("---------------------------------------------------")
be1 = BackendDeveloper(102, "Bob", "Development", "Web", "Python")
be1.display_info()

#Console Output:
# Employee ID: 101, Name: Alice, Department: Development
# Developer works on the platform Web
# Frontend Developer uses the framework React
# ---------------------------------------------------
# Employee ID: 102, Name: Bob, Department: Development
# Developer works on the platform Web
# Backend Developer works with the database Python   