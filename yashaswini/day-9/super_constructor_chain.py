#Super Constructor Chain

# Base class
class Employee:
    def __init__(self, id, name, department):
        # Initialize common employee attributes
        self.id = id
        self.name = name
        self.dept = department

    def show_info(self):
        # Display employee details
        print(f"ID: {self.id}, Name: {self.name}, Department: {self.dept}")


# Developer inherits from Employee
class Developer(Employee):
    def __init__(self, id, name, department, platform):
        # Call Employee constructor using super()
        super().__init__(id, name, department)
        # Add Developer-specific attribute
        self.platform = platform

    def platform_info(self):
        # Display developer's platform
        print(f"Platform: {self.platform}")


# FrontEndDeveloper inherits from Developer
class FrontEndDeveloper(Developer):
    def __init__(self, id, name, department, platform, react):
        # Call Developer constructor using super()
        super().__init__(id, name, department, platform)
        # Add FrontEndDeveloper-specific attribute
        self.react = react

    def tech_info(self):
        # Display frontend technology
        print(f"Tech: {self.react}")


# BackEndDeveloper inherits from Developer
class BackEndDeveloper(Developer):
    def __init__(self, id, name, department, platform, python):
        # Call Developer constructor using super()
        super().__init__(id, name, department, platform)
        # Add BackEndDeveloper-specific attribute
        self.python = python

    def lang_info(self):
        # Display backend language
        print(f"Lang: {self.python}")


# Create objects of FrontEndDeveloper and BackEndDeveloper
emp1 = FrontEndDeveloper(101, "Shiv", "IT", "Android", "React")
emp2 = BackEndDeveloper(102, "Ram", "IT", "Android", "Python")

# Call methods for FrontEndDeveloper
emp1.show_info()       # From Employee
emp1.platform_info()   # From Developer
emp1.tech_info()       # From FrontEndDeveloper

print("\n*****************\n")

# Call methods for BackEndDeveloper
emp2.show_info()       # From Employee
emp2.platform_info()   # From Developer
emp2.lang_info()       # From BackEndDeveloper


#o/p:
# ID: 101, Name: Shiv, Department: IT
# Platform: Android
# Tech: React

# *****************

# ID: 102, Name: Ram, Department: IT
# Platform: Android
# Lang: Python