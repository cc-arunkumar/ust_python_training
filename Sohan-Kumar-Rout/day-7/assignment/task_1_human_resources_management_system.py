#Task : Human Resource Management  System 

#Code
class Employee:
    def __init__(self,emp_id , name, base_salary):
        self.emp_id=emp_id
        self.name=name
        self.base_salary=base_salary
    
    #Printing employee details
    def get_details(self):
        print(f"Employee id : {self.emp_id}")
        print(f"Employee name : {self.name}")
        print(f"Employee base Salary : {self.base_salary}")
        
class Developer(Employee):
    def __init__(self, emp_id, name, base_salary,programming_languages):
        Employee.__init__(self,emp_id, name, base_salary)
        self.programming_languages=programming_languages
        
        
    def show_skills(self):
        print(f"{self.name} has this skill : {",".join(self.programming_languages)}")
        
class Manager(Employee):
    def __init__(self, emp_id, name, base_salary,team_size,department):
        Employee.__init__(self,emp_id, name, base_salary)
        self.team_size=team_size
        self.department=department
        
    #Showing team info 
    def show_team_info(self):
        print(f"Team Size : {self.team_size}")
        print(f"Department : {self.department}")

class DeveloperManager(Developer, Manager):
    def __init__(self, emp_id, name, base_salary, programming_languages,team_size,department):
        Developer.__init__(self,emp_id, name, base_salary,programming_languages)
        Manager.__init__(self,emp_id, name, base_salary,team_size,department)

emp=Employee(101,"Sohan Kumar",45000)
emp.get_details()

dev = Developer(102,"Ahaan Mohanty",56000,["Java","Python"])
dev.get_details()
dev.show_skills()


mag = Manager(103,"Asutosh Mohanty",89000,23,"IT")
mag.get_details()
mag.show_team_info()

mag_dev = DeveloperManager(104, "Monalisa Rout",1000000,["Javascript","React"],34,"HR")
mag_dev.get_details()
mag_dev.show_skills()
mag_dev.show_team_info()

#Output
# Employee id : 101
# Employee name : Sohan Kumar
# Employee base Salary : 45000
# Employee id : 102
# Employee name : Ahaan Mohanty
# Employee base Salary : 56000
# Ahaan Mohanty has this skill : Java,Python
# Employee id : 103
# Employee name : Asutosh Mohanty
# Employee base Salary : 89000
# Team Size : 23
# Department : IT
# Employee id : 104
# Employee name : Monalisa Rout
# Employee base Salary : 1000000
# Monalisa Rout has this skill : Javascript,React
# Team Size : 34
# Department : HR

        