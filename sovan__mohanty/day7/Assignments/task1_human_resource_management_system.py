#Task 1 Human Resource Management System

#Creating parent class Employee

class Employee:
    def __init__(self,emp_id,name,base_salary):
        self.emp_id=emp_id
        self.name=name
        self.base_salary=base_salary
    #function to get employee details
    def get_details(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Employee Name: {self.name}")
        print(f"Employee Base Salary: {self.base_salary}")
        

#Creating Developer class derived from Employee class
class Developer(Employee):
    def __init__(self, emp_id, name, base_salary, programming_languages):
        Employee. __init__(self,emp_id, name, base_salary)
        self.programming_languages=programming_languages
    
    #function to show skills
    def show_skills(self):
        return self.programming_languages
    
#Creating Manager Class derived from Employee Class
class Manager(Employee):
    def __init__(self, emp_id, name, base_salary, team_size, department):
        Employee.__init__(self,emp_id, name, base_salary)
        self.team_size = team_size
        self.department = department
    
    #function to show team info
    def show_team_info(self):
        print(f"Team size: {self.team_size}")
        print(f"Department: {self.department}")

#Creating DeveloperManager which will derive both from Developer and Manager

class DevloperManager(Manager, Developer):
    def __init__(self, emp_id, name, base_salary, team_size, department, programming_languages):
       Manager.__init__(self,emp_id, name, base_salary, team_size, department)
       Developer.__init__(self,emp_id, name, base_salary, programming_languages)
#Developer
dev = Developer(101,"Rohan",900000,["Java","Python"])
dev.get_details()
print(dev.show_skills())

# Manager
mgr = Manager(102, "Rajeev", 80000, 14, "HR")
mgr.get_details()
mgr.show_team_info()

# Manager who is also developer
mgr_dev = DevloperManager(103, "Rishi", 90000, 5, "IT", ["Java", "C++"])
mgr_dev.get_details()
mgr_dev.show_team_info()
print(mgr_dev.show_skills())

#Sample Execution
# Employee ID: 101
# Employee Name: Rohan
# Employee Base Salary: 900000
# ['Java', 'Python']
# Employee ID: 102
# Employee Name: Rajeev
# Employee Base Salary: 80000
# Team size: 14
# Department: HR
# Employee ID: 103
# Employee Name: Rishi
# Employee Base Salary: 90000
# Team size: 5
# Department: IT
# ['Java', 'C++']


    
    