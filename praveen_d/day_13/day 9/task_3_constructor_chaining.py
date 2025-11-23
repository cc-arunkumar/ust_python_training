class Employee:
    def __init__(self,emp_id,name,base_salary):
        self.emp_id=emp_id
        self.name=name
        self.base_salary=base_salary

    def get_details(self):
        print(f"Employee Id:{self.emp_id}")
        print(f"Employee name:{self.name}")
        print(f"Employee salary:{self.base_salary}")

# 2. Developers have:
# programming_languages (list)
# Method: show_skills()
class Developer(Employee):
    def __init__(self,emp_id,name,base_salary,languages):
        super().__init__(emp_id,name,base_salary)
        self.programming_languages=languages

    def show_skills(self):
        print(f"Skills:{self.programming_languages}")

# 3. Managers have:

class FrontEnd(Developer):
    def __init__(self,emp_id,name,base_salary,team_size,department):
        super().__init__(emp_id,name,base_salary,department)
        self.team_size=team_size
        self.department=department

    def show_team_info(self):
        print("Frontend developer")
      

# # 4. Some managers are also developers (they code in emergencies).
class BackEnd(Developer):
    def __init__(self,emp_id,name,base_salary,team_size,department,languages):
        super().__init__(emp_id,name,base_salary,languages)
        self.team_size=team_size
        self.department=department

    def show_team_info(self):
        print("Backend developer")

print("-------------------------------------------------------------------------")

dev= Developer(101,"Amit",400000,"Java")
dev.get_details()
dev.show_skills()

print("-------------------------------------------------------------------------")

front_end=FrontEnd(101,"Arun",100000,30,"Cybersecurity")
front_end.show_team_info()

print("-------------------------------------------------------------------------")

back_end=BackEnd(101,"Amit",500000,20,"Full stack","Java")
back_end.show_team_info()


# PS C:\UST python> & C:/Users/303489/AppData/Local/Programs/Python/Python312/python.exe "c:/UST python/Praveen D/day 9/task_3_constructor_chaining.py"
# -------------------------------------------------------------------------
# Employee Id:101
# Employee name:Amit
# Employee salary:400000
# Skills:Java
# -------------------------------------------------------------------------
# Frontend developer
# -------------------------------------------------------------------------
# Backend developer