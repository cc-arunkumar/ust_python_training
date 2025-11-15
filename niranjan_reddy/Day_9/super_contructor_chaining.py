# Super() Constructor Chaining

# Creating Employee class
class Employee:
    def __init__(self,id,name,dept):
        self.id=id
        self.name=name
        self.dept=dept


# Creating developer child class inherit from employee class
class Developer(Employee):
    def __init__(self, id, name, dept,platform):
        super().__init__(id, name, dept)
        self.platform=platform

# Creating FrontEnddev child class inherit from Developer class

class FrontEndDev(Developer):
    def __init__(self, id, name, dept, platform,technologies):
        super().__init__(id, name, dept, platform)
        self.technologies=technologies

# Creating BackEnddev child class inherit from Developer class
class BackEndDev(Developer):
    def __init__(self, id, name, dept, platform,language):
        super().__init__(id, name, dept, platform)
        self.language=language


backend=BackEndDev(101,"Niranjan","IT","web_developer","python")

print("Back end developer -Details",backend.__dict__)

dev=Developer(102,"Sai","IT","Full stack developer")

print("Developer details",dev.__dict__)

# Sample output

# Back end developer -Details {'id': 101, 'name': 'Niranjan', 'dept': 'IT', 'platform': 'web_developer', 'language': 'python'}
# Developer details {'id': 102, 'name': 'Sai', 'dept': 'IT', 'platform': 'Full stack developer'}
