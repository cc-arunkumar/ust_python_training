from typing import List

class Employee:
    def __init__(self, emp_id, name, base_salary):
        self.emp_id = emp_id
        self.name = name
        self.base_salary = base_salary
        
    def get_details(self):
        print(self.emp_id, self.name, self.base_salary)


class Developers:
    def __init__(self, programming_language: List[str]):
        self.programming_language = programming_language or []
        
    def show_skills(self):
        print("Skills:", ", ".join(self.programming_language))


    

class Managers:

    def __init__(self,team_size,department):
        self.team_size = team_size
        self.department = department
    def show_team_info(self):
        print(self.team_size," ", self.department)

class DevManagers (Developers,Managers):
    def __init__(self,team_size,department,programming_language):
        Developers.__init__(self, programming_language)
        Managers.__init__(self,team_size,department)

# emp1 = Managers("3305", "Rohit", "123000", ["Java", "Python"])
emp1 = DevManagers(5,"IT",{"Java", "Python"})
emp1.show_team_info()
emp1.show_skills()
