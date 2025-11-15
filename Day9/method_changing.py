# Parent class
class Employee:
    def __init__(self,id,name,dept):
        self.id = id
        self.name = name
        self.dept = dept

# Child class of Employee
class Developer(Employee):
    def __init__(self, id, name, dept, platform):
        super().__init__(id, name, dept)
        self.platform = platform
    def show_skill_sets(self):
        print(f"Employee ID:{self.id}")
        print(f"Employee Name:{self.name}")
        print(f"Employee department:{self.dept}")
        print(f"Employee platform:{self.platform}")

# Child class of Developer
class FrontEnd(Developer):
    def __init__(self, id, name, dept, platform, techstack_fe):
        super().__init__(id, name, dept,platform)
        self.techstack_fe = techstack_fe
    def show_skill_sets(self):
        print(f"Employee ID:{self.id}")
        print(f"Employee Name:{self.name}")
        print(f"Employee department:{self.dept}")
        print(f"Employee platform:{self.platform}")
        print(f"Employee using tech stack for frontend:{self.techstack_fe}")

# Child class of Developer        
class BackEnd(Developer):
    def __init__(self, id, name,dept, platform,techstack_be):
        super().__init__(id, name,dept,platform)
        self.techstack_be = techstack_be
    def show_skill_sets(self):
        print(f"Employee ID:{self.id}")
        print(f"Employee Name:{self.name}")
        print(f"Employee department:{self.dept}")
        print(f"Employee platform:{self.platform}")
        print(f"Employee using tech for backend:{self.techstack_be}")

front_end = FrontEnd("E101","Gowtham","IT","ios","react")
front_end.show_skill_sets

back_end = BackEnd("E101","Maddie","IT","ios",".net")
back_end.show_skill_sets()

# sample output:

# Employee ID:E101
# Employee Name:Maddie
# Employee department:IT
# Employee platform:ios
# Employee using tech for backend:.net
