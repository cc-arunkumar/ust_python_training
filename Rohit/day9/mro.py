# Base class representing a generic Employee
class Emp:
    def __init__(self):
        pass   # No attributes initialized here
    
    def perform_task(self):
        # Default implementation of perform_task
        print("employee completed the task")


# Subclass Manager overrides perform_task
class Manager(Emp):
    def perform_task(self):
        print("Manager completed the task")


# Subclass Developer inherits from Emp but does not override perform_task
class Developer(Emp):
    # If perform_task is not defined here, it will use Emp's version
    pass


# Subclass Tester overrides perform_task
class Tester(Emp):
    def perform_task(self):
        print("Tester completed the task")


# Create a list of different employee objects
employess = [Emp(), Manager(), Developer(), Tester()]

# Loop through each employee and call perform_task
for emp in employess:
    emp.perform_task()

# ==============sample output====================
# employee completed the task
# Manager completed the task
# employee completed the task
# Tester completed the task
