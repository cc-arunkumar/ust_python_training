# Base class representing a general employee
class Emp():
    def __init__(self, emp_id, name):
        # Initialize common attributes for all employees
        self.emp_id = emp_id
        self.name = name

    # Method to display employee info (will be overridden in child classes)
    def show(self):
        print(f"{self.name} is an Employee")


# Developer class inheriting from Emp
class Dev(Emp):
    def __init__(self, emp_id, name, dept):
        # Call the parent constructor to set emp_id and name
        super().__init__(emp_id, name)
        self.dept = dept  # Additional attribute for developers

    # Method overriding - Dev class provides its own show()
    def show(self):
        print(f"{self.name} is a Developer in the {self.dept} department")


# Front-end developer inheriting from Dev
class FrontEndDev(Dev):
    def __init__(self, emp_id, name, dept, tech):
        # Initialize attributes of Dev class first
        super().__init__(emp_id, name, dept)
        self.tech = tech  # Front-end specific skill/technology

    # Method overriding
    def show(self):
        print(f"{self.name} is a Front-End Developer in {self.dept}, working with {self.tech}")


# Back-end developer inheriting from Dev
class BackEndDev(Dev):
    def __init__(self, emp_id, name, dept, lang):
        # Initialize parent (Dev) attributes
        super().__init__(emp_id, name, dept)
        self.lang = lang  # Back-end specific language

    # Method overriding
    def show(self):
        print(f"{self.name} is a Back-End Developer in {self.dept}, using {self.lang}")


# Creating an object of BackEndDev class
emp1 = BackEndDev("E101", "Akash", "IT", "Python")

# Calling the overridden show() method
emp1.show()
