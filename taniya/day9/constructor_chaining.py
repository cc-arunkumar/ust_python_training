#Python Inheritance Task
# Task:
# Create a class hierarchy to represent employees at UST.
# Requirements:
# - Create a base class Employee with attributes: id, name, department, and a method show() to return basic details.
# - Create a subclass Developer with an additional attribute platform, and override show() to include platform info.
# - Create two more subclasses:
# - FrontEndDeveloper → adds technology
# - BackEndDeveloper → adds database
# - Override show() in each subclass to display all relevant details
# - Create objects of each class using hardcoded input and call show() on each to demonstrate polymorphism.



# Base class representing a generic employee
class Employee:
    def __init__(self,id,name,department):
        self.id=id
        self.name=name
        self.department=department
    # Returns basic employee details as a string
    
    def show(self):
        return(f"Employee ID: {self.id}, Employee Name: {self.name}, Department: {self.department}")
# Developer class inherits from Employee and adds platform info

class Developer(Employee):
    def __init__(self, id, name, department,platform):
        Employee.__init__(self,id, name, department)
        self.platform=platform
    # Prints base employee details and platform

    def show(self):
        print(Employee.show(self))
        print(f"Platform:{self.platform}")

# FrontEndDeveloper inherits from Developer and adds technology info
    
class FrontEndDeveloper(Developer):
    def __init__(self, id, name, department, platform,technology):
        Developer.__init__(self,id, name, department, platform)
        self.technology=technology
    # Prints developer details and technology

    def show(self):
        print(Developer.show(self))
        print(f"Technology: {self.technology}")
# BackEndDeveloper inherits from Developer and adds database info        
class BackEndDeveloper(Developer):
    def __init__(self, id, name, department, platform,database):
        super().__init__(id, name, department, platform)
        self.database=database
    # Prints developer details and database
    def show(self):
        print(Developer.show(self))
        print(f"Database: {self.database}")

# Create objects of each class
emp = Employee(101, "Taniya", "HR")
dev = Developer(102, "Rohit", "IT", "Windows")
fe_dev = FrontEndDeveloper(103, "Prithvi", "IT", "Web", "React")
be_dev = BackEndDeveloper(104, "Harsh", "IT", "Server", "SQL")   

print(emp.show())  # Returns a string

dev.show()         # Prints platform, but doesn't print base info due to missing print
fe_dev.show()      # Prints platform and technology
be_dev.show()      # Prints platform and database    
 
#Output
# Employee ID: 101, Employee Name: Taniya, Department: HR
# Employee ID: 102, Employee Name: Rohit, Department: IT
# Platform:Windows
# Employee ID: 103, Employee Name: Prithvi, Department: IT      
# Platform:Web
# None
# Technology: React
# Employee ID: 104, Employee Name: Harsh, Department: IT        
# Platform:Server
# None
# Database: SQL    