class Emp:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def display_info(self):
        print(f"Employee Name: {self.name}, Employee ID: {self.emp_id}")
class Dev(Emp):
    def __init__(self, name, emp_id, platform):
        super().__init__(name, emp_id)
        self.programming_language = platform

    def display_info(self):
        super().display_info()
        print(f"Programming Language: {self.programming_language}")
        
class frontend(Dev):
    def __init__(self, name, emp_id, platform, framework):
        super().__init__(name, emp_id, platform)
        self.framework = framework

    def display_info(self):
        super().display_info()
        print(f"Framework: {self.framework}")
        
class backend(Dev):
    def __init__(self, name, emp_id, platform, database):
        super().__init__(name, emp_id, platform)
        self.database = database

    def display_info(self):
        super().display_info()
        print(f"Database: {self.database}")
        
        
print("------------------------------------------")
emp1=Emp("Harsh", "E001")
emp1.display_info()
print("------------------------------------------")
dev1=Dev("Rohit", "D101", "Python")
dev1.display_info()
print("------------------------------------------")
fe1 = frontend("Harsh", "F101", "JavaScript", "React")
fe1.display_info()
print("------------------------------------------")
be1 = backend("Rohit", "B201", "Python", "PostgreSQL")
be1.display_info()
print("------------------------------------------")