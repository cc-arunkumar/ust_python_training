# super_constructor_chainning
# Base Class
class Employee:
    def __init__(self, id, name, department):
        self.id = id
        self.name = name
        self.department = department


# Intermediate Class -Developer
class Developer(Employee):
    def __init__(self, id, name, department, platform):
        # Calling parent class constructor
        super().__init__(id, name, department)
        self.platform = platform


# Child Class - Frontend Developer
class FrontEndDeveloper(Developer):
    def __init__(self, id, name, department, platform, Technologies):
        # Calling Developer constructor
        super().__init__(id, name, department, platform)
        self.Technologies = Technologies


# Child Class - Backend Developer
class BackEndDeveloper(Developer):
    def __init__(self, id, name, department, platform, Language):
        # Calling Developer constructor
        super().__init__(id, name, department, platform)
        self.Language = Language


# Creating Objects
emp = Employee(101, "niru", "HR")
dev = Developer(102, "sai", "IT", "Full Stack")
front_end = FrontEndDeveloper(103, "Abhi", "IT", "Web Developer", "React")
back_end = BackEndDeveloper(104, "shake", "IT", "Server Developer", "Python")


# Printing Object Data using __dict__
print("Employee Details:", emp.__dict__)
print("Developer Details:", dev.__dict__)
print("Frontend Developer Details:", front_end.__dict__)
print("Backend Developer Details:", back_end.__dict__)



# Sample Output:
# Employee Details: {'id': 101, 'name': 'niru', 'department': 'HR'}
# Developer Details: {'id': 102, 'name': 'sai', 'department': 'IT', 'platform': 'Full Stack'}
# Frontend Developer Details: {'id': 103, 'name': 'Abhi', 'department': 'IT', 'platform': 'Web Developer', 'Technologies': 'React'}
# Backend Developer Details: {'id': 104, 'name': 'shake', 'department': 'IT', 'platform': 'Server Developer', 'Language': 'Python'}