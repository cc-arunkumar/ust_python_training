skills_data = [
    ("E101", "Python", "Advanced"),
    ("E101", "SQL", "Intermediate"),
    ("E102", "Excel", "Expert"),
    ("E102", "PowerBI", "Advanced"),
    ("E103", "Python", "Beginner"),
    ("E103", "Excel", "Intermediate")
]

employee_skills = {}
skill_to_employees = {}
unique_skills = set()

for emp_id, skill, level in skills_data:
    if emp_id not in employee_skills:
        employee_skills[emp_id] = {}
        
    if skill not in employee_skills[emp_id]:
        employee_skills[emp_id][skill] = level
        unique_skills.add(skill)
        
        if skill not in skill_to_employees:
            skill_to_employees[skill] = set()
        skill_to_employees[skill].add(emp_id)
        

def get_employees_with_a_skill(skill_name):
    return skill_to_employees.get(skill_name, set())



def add_or_update_skill(emp_id, skill, level):
    if emp_id not in employee_skills:
        employee_skills[emp_id] = {}
        
    is_new_skill = skill not in employee_skills[emp_id]
    employee_skills[emp_id][skill] = level
    
    if is_new_skill:
        unique_skills.add(skill)
        if skill not in skill_to_employees:
            skill_to_employees[skill] = set()
        skill_to_employees[skill].add(emp_id)
        
add_or_update_skill("E103", "PowerBI", "Intermediate")
add_or_update_skill("E101", "Python", "Expert")

print("Employee Skill Matrix:")
for emp_id, skills in employee_skills.items():
    print(f"{emp_id}: {skills}")

print("\nEmployees who know Python:")
print(get_employees_with_a_skill("Python"))

employees_with_3plus_skills = [emp_id for emp_id, skills in employee_skills.items() if len(skills) >= 3]
print("\nEmployees with 3 or more skills:")
print(employees_with_3plus_skills)

print("\nAll unique skills across the company:")
print(unique_skills)


#sample output
# Employee Skill Matrix:
# E101: {'Python': 'Expert', 'SQL': 'Intermediate'}
# E102: {'Excel': 'Expert', 'PowerBI': 'Advanced'}
# E103: {'Python': 'Beginner', 'Excel': 'Intermediate', 'PowerBI': 'Intermediate'}

# Employees who know Python:
# {'E101', 'E103'}

# Employees with 3 or more skills:
# ['E103']

# All unique skills across the company:
# {'PowerBI', 'Python', 'SQL', 'Excel'}