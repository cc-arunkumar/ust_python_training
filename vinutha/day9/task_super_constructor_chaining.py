# Constructor Chainig

# Base class Employee
class Employee:
    def __init__(self, id, name, dept):
        # Initialize common employee attributes
        self.id = id
        self.name = name
        self.dept = dept

    def show_info(self):
        # Display employee details
        print(f"ID: {self.id}, Name: {self.name}, Dept: {self.dept}")


# Developer class inherits from Employee
class Developer(Employee):
    def __init__(self, id, name, dept, platform):
        # Call parent constructor to set id, name, dept
        super().__init__(id, name, dept)
        # Add developer-specific attribute
        self.platform = platform

    def platform_info(self):
        # Display platform information
        print(f"Platform: {self.platform}")


# FrontEndDeveloper inherits from Developer
class FrontEndDeveloper(Developer):
    def __init__(self, id, name, dept, platform, react):
        # Call Developer constructor
        super().__init__(id, name, dept, platform)
        # Add frontend-specific technology attribute
        self.react = react

    def tech_info(self):
        # Display frontend technology info
        print(f"Tech: {self.react}")


# BackEndDeveloper inherits from Developer
class BackEndDeveloper(Developer):
    def __init__(self, id, name, dept, platform, python):
        # Call Developer constructor
        super().__init__(id, name, dept, platform)
        # Add backend-specific language attribute
        self.python = python

    def lang_info(self):
        # Display backend language info
        print(f"Lang: {self.python}")


# Create objects of FrontEndDeveloper and BackEndDeveloper
emp1 = FrontEndDeveloper(1, "Vinnu", "IT", "Android", "React")
emp2 = BackEndDeveloper(2, "hima", "IT", "Android", "Python")

# Show frontend developer details
print("**Frontend**")
emp1.show_info()       
emp1.platform_info()   
emp1.tech_info()       

# Show backend developer details
print("**Backend**")
emp2.show_info()       
emp2.platform_info()   
emp2.lang_info()       


#output:
# ID: 1, Name: Vinnu, Dept: IT
# Platform: Android
# Tech: React
# **Backend**
# ID: 2, Name: hima, Dept: IT
# Platform: Android
# Lang: Python