class Employee:
    def __init__(self,id,name,dept):
        self.id=id
        self.name=name
        self.dept=dept

    # def s
    
class Developer(Employee):
    def __init__(self, id, name, dept,platform):
        super().__init__(id, name, dept)
        self.platform=platform
    
    def show_details(self):
        print("ID :",self.id)
        print("Name :",self.name)
        print("Department :",self.dept)
        print("Platform :",self.platform)


class Frontend(Developer):
    def __init__(self, id, name, dept, platform,skill):
        super().__init__(id, name, dept, platform)
        self.skill=skill
    
    def show_details(self):
        print("ID :",self.id)
        print("Name :",self.name)
        print("Department :",self.dept)
        print("Platform :",self.platform)
        print("Skill set :",self.skill)

class Backend(Developer):
    def __init__(self, id, name, dept, platform,skill):
        super().__init__(id, name, dept, platform)
        self.skill=skill
    
    def show_details(self):
        print("ID :",self.id)
        print("Name :",self.name)
        print("Department :",self.dept)
        print("Platform :",self.platform)
        print("Skill set :",self.skill)

d1=Developer(1,"Gowtham","R/D","IOs")
d1.show_details()

f1=Frontend(2,"Mani","IT","IOS","React")
f1.show_details()

b1=Backend(3,"Dk","Devops","Android","Angular")
b1.show_details()


"""
SAMPLE OUTPUT

ID : 1
Name : Gowtham
Department : R/D
Platform : IOs
ID : 2
Name : Mani
Department : IT
Platform : IOS
Skill set : React
ID : 3
Name : Dk
Department : Devops
Platform : Android
Skill set : Angular
"""