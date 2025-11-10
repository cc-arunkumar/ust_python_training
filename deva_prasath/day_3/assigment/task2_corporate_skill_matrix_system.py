# Corporate Skill Matrix System

# UST’s L&D team wants to maintain a skill matrix for all employees.
# Every employee can have multiple skills at different proficiency levels.

skills_data = [
    ("E101","Python","Advanced"),
    ("E101","SQL","Intermediate"),
    ("E102","Excel","Expert"),
    ("E102","PowerBI","Advanced"),
    ("E103","Python","Beginner"),
    ("E103","Excel","Intermediate")
]
employee_skills = {}      
skill_to_employees = {}   
unique_skills = set()

for emp_id,skill,level in skills_data:
    if emp_id not in employee_skills:
        employee_skills[emp_id] = {}
    employee_skills[emp_id][skill] = level

    if skill not in skill_to_employees:
        skill_to_employees[skill] = set()
    skill_to_employees[skill].add(emp_id)

    unique_skills.add(skill)

def update_skill(emp_id, skill, level):
    if emp_id not in employee_skills:
        employee_skills[emp_id] = {}
    employee_skills[emp_id][skill] = level

    if skill not in skill_to_employees:
        skill_to_employees[skill] = set()
    skill_to_employees[skill].add(emp_id)

    unique_skills.add(skill)

update_skill("E101", "PowerBI", "Intermediate")  
update_skill("E103", "Python", "Intermediate")   

query_skill = "Python"
print("\nEmployees who know", query_skill, ":")
if query_skill in skill_to_employees:
    for emp in skill_to_employees[query_skill]:
        print(" -", emp)
else:
    print(" None")

print("Unique skills in the company:")
for skill in sorted(unique_skills):
    print(" -", skill)

print("Employees with 3 or more skills:")
found = False
for emp, skills in employee_skills.items():
    if len(skills) >= 3:
        print(" -", emp)
        found = True
if not found:
    print(" None")

print("Employee Skills:")
for emp, skills in employee_skills.items():
    print(" -", emp)
    for skill_name, level in skills.items():
        print(skill_name, level)

#Sample output

# Employees who know Python :
#  - E101
#  - E103
# Unique skills in the company:
#  - Excel
#  - PowerBI
#  - Python
#  - SQL
# Employees with 3 or more skills:
#  - E101
# Employee Skills:
#  - E101
# Python Advanced
# SQL Intermediate
# PowerBI Intermediate
#  - E102
# Excel Expert
# PowerBI Advanced
#  - E103
# Python Intermediate
# Excel Intermediate
