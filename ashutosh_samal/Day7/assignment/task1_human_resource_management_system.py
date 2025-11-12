#Task 1 — Human Resource Management System(HRMS)
class Employee:
    def __init__(self,emp_id,name,base_salary):
        self.emp_id = emp_id
        self.name = name
        self.base_salary =base_salary
    
    #function to print details
    def get_details(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Employee Name: {self.name}")
        print(f"Employee Salary: {self.base_salary}")

#Creation of deeveloper class
class Developer(Employee):
    def __init__(self, emp_id, name, base_salary,programming_languages):
        Employee.__init__(self,emp_id, name,base_salary)
        self.programming_langusges = programming_languages
    
    #function to print skills    
    def show_skill(self):
        print(f"Skills of {self.name}: {self.programming_langusges}")

#Creation of manager class
class Manager(Employee):
    def __init__(self, emp_id, name, base_salary,team_size,department):
        Employee.__init__(self,emp_id, name, base_salary)
        self.team_size = team_size
        self.department = department
    
    #function to print team info
    def show_team_info(self):
        print(f"Team Size: {self.team_size} | Department: {self.department}")

#creation of DevManager class
class DeveloperManager(Manager,Developer):
    def __init__(self, emp_id, name, base_salary, team_size, department,programming_languages):
        Manager.__init__(self,emp_id, name, base_salary, team_size, department)
        Developer.__init__(self, emp_id, name, base_salary,programming_languages)

#Obj creation
emp1 = Manager("E100","Amit",90000,10,"IT")
emp2 = Developer("E101","Ankit",80000,"[Java,Python,SQL]")
emp3 = DeveloperManager("E103","Mukesh",100000,15,"IT","[Java,Python]")

#accessing methods
emp1.get_details()
emp1.show_team_info()
print("================================")

emp2.get_details()
emp2.show_skill()
print("================================")

emp3.get_details()
emp3.show_skill()
emp3.show_team_info()
print("================================")


#Sample Execution
# Employee ID: E100
# Employee Name: Amit
# Employee Salary: 90000
# Team Size: 10 | Department: IT    
# ================================  
# Employee ID: E101
# Employee Name: Ankit
# Employee Salary: 80000
# Skills of Ankit: [Java,Python,SQL]
# ================================  
# Employee ID: E103
# Employee Name: Mukesh
# Employee Salary: 100000
# Skills of Mukesh: [Java,Python]
# Team Size: 15 | Department: IT
# ================================