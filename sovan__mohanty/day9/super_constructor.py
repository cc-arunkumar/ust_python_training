#Task super constructor chaining
class Employee:
    def __init__(self,id,name,dept):
        self.id=id
        self.name=name
        self.dept=dept
class Dev(Employee):
    def __init__(self, id, name, dept,platform):
        super().__init__(id, name, dept)
        self.platform=platform
class FrontEndDev(Dev):
    def __init__(self, id, name, dept, platform,tech):
        super().__init__(id, name, dept, platform)
        self.tech=tech
class BackEndDev(Dev):
    def __init__(self, id, name, dept, platform,lang):
        super().__init__(id, name, dept, platform)
        self.lang=lang
d=Dev(101,"Sovan","SDE","Frontend")
print(f"Developer Details: {d.id}, {d.name}, {d.dept},{d.platform}")


#Sample Execution
# Developer Details: 101, Sovan, SDE,Frontend