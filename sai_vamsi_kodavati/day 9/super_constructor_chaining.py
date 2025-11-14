# super_constructor_chaining

class Employee:
    def __init__(self,id,name,dept):
        self.id = id
        self.name = name
        self.dept = dept

class Developer(Employee):
    def __init__(self, id, name, dept, platform):
        super().__init__(id,name,dept)
        self.platform = platform

class FrontEndDev(Developer):
    def __init__(self,id,name,dept,platform,technology):
        super().__init__(id,name,dept,platform)
        self.technology = technology

class BackEndDev(Developer):
    def __init__(self,id,name,dept,platform,technology,language):
        super().__init__(id,name,dept,platform)
        self.technology = technology
        self.language = language

frontend = FrontEndDev(101,"Tharun","CSE","Web dev","React")
print(frontend.__dict__) 

backend = BackEndDev(102,"Sai Vamsi","CSE","VS Code","Fast","Python")
print(backend.__dict__)


# -------------------------------------------------------------------------------------

# Sample Output

# {'id': 101, 'name': 'Tharun', 'dept': 'CSE', 'platform': 'Web dev', 'technology': 'React'}
# {'id': 102, 'name': 'Sai Vamsi', 'dept': 'CSE', 'platform': 'VS Code', 'technology': 'Fast', 'language': 'Python'}




