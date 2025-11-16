# Employee class
# Initializes id name and dept
# Method show_info prints employee details


class Employee:
    def __init__(self, id, name, dept):
        self.id = id
        self.name = name
        self.dept = dept

    def show_info(self):
        print(f"ID: {self.id}, Name: {self.name}, Dept: {self.dept}")


# Developer class inherits Employee
# Adds platform attribute
# Method platform_info prints platform

class Developer(Employee):
    def __init__(self, id, name, dept, platform):
        super().__init__(id, name, dept)
        self.platform = platform

    def platform_info(self):
        print(f"Platform: {self.platform}")
        
# FrontEndDeveloper class inherits Developer
# Adds react attribute
# Method tech_info prints frontend technology


class FrontEndDeveloper(Developer):
    def __init__(self, id, name, dept, platform, react):
        super().__init__(id, name, dept, platform)
        self.react = react

    def tech_info(self):
        print(f"Tech: {self.react}")
        
# BackEndDeveloper class inherits Developer
# Adds python attribute
# Method lang_info prints backend language


class BackEndDeveloper(Developer):
    def __init__(self, id, name, dept, platform, python):
        super().__init__(id, name, dept, platform)
        self.python = python

    def lang_info(self):
        print(f"Lang: {self.python}")
        
# Objects created
# emp1 is a FrontEndDeveloper with id 1 name yashu dept IT platform web application tech React
# emp2 is a BackEndDeveloper with id 2 name tharun dept IT platform ios language Python


emp1 = FrontEndDeveloper(1, "yashu", "IT", "web application", "React")
emp2 = BackEndDeveloper(2, "tharun", "IT", "ios", "Python")

emp1.show_info()
emp1.platform_info()
emp1.tech_info()

emp2.show_info()
emp2.platform_info()
emp2.lang_info()


# Output

# ID: 1, Name: yashu, Dept: IT
# Platform: web application
# Tech: React
# ID: 2, Name: tharun, Dept: IT
# Platform: ios
# Lang: Python
