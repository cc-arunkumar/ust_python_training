#Task super constructor chaining
# Base class representing a generic Employee
class Employee:
    def __init__(self, id, name, dept):
        # Initialize common employee attributes
        self.id = id
        self.name = name
        self.dept = dept

# Developer class inherits from Employee
class Dev(Employee):
    def __init__(self, id, name, dept, platform):
        # Call the parent (Employee) constructor to set id, name, dept
        super().__init__(id, name, dept)
        # Add an extra attribute specific to developers
        self.platform = platform

# FrontEndDev inherits from Dev (which itself inherits from Employee)
class FrontEndDev(Dev):
    def __init__(self, id, name, dept, platform, tech):
        # Call Dev constructor to initialize id, name, dept, platform
        super().__init__(id, name, dept, platform)
        # Add technology attribute specific to frontend developers
        self.tech = tech

# BackEndDev inherits from Dev (which itself inherits from Employee)
class BackEndDev(Dev):
    def __init__(self, id, name, dept, platform, lang):
        # Call Dev constructor to initialize id, name, dept, platform
        super().__init__(id, name, dept, platform)
        # Add language attribute specific to backend developers
        self.lang = lang

# Create a Developer object
d = Dev(101, "Sovan", "SDE", "Frontend")

# Print developer details using f-string formatting
print(f"Developer Details: {d.id}, {d.name}, {d.dept}, {d.platform}")



#Sample Execution
# Developer Details: 101, Sovan, SDE,Frontend