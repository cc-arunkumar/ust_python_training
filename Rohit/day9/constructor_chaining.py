# Base class representing a generic Employee
class Emp:
    def __init__(self, id, name, department):
        # Initialize employee attributes
        self.id = id
        self.name = name
        self.department = department
        # Print employee details
        print(self.id, " ", self.name, " ", self.department)


# Subclass representing Developers (inherits from Emp)
class Dev(Emp):
    def __init__(self, id, name, department, platform):
        # Call parent constructor to initialize common attributes
        super().__init__(id, name, department)
        # Add developer-specific attribute
        self.platform = platform
        # Print developer details including platform
        print(id, " ", name, " ", department, " ", self.platform)


# Subclass representing Frontend Developers (inherits from Dev)
class Frontend(Dev):
    def __init__(self, id, name, department, platform, technology):
        # Call Dev constructor
        super().__init__(id, name, department, platform)
        # Add frontend-specific attribute
        self.technology = technology
        # Print frontend developer details including technology
        print(id, " ", name, " ", department, " ", platform, " ", self.technology)


# Subclass representing Backend Developers (inherits from Frontend)
class Backend(Frontend):
    def __init__(self, id, name, department, platform, technology, language):
        # Call Frontend constructor (which also calls Dev and Emp)
        super().__init__(id, name, department, platform)
        # Add backend-specific attributes
        self.technology = technology
        self.language = language
        # Print backend developer details including technology and language
        print(id, " ", name, " ", department, " ", platform, " ", self.technology, " ", self.language)


# Create a Backend object
backend_dev = Backend("R5050", "Sneha", "IT", "Server", "SpringBoot", "Java")



# ============sample output======================
# R5050 Sneha IT
# R5050 Sneha IT Server
# R5050 Sneha IT Server SpringBoot
# R5050 Sneha IT Server SpringBoot Java
