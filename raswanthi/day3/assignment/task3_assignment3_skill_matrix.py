#Skill matrix
skills_data = [
    ("E101", "Python", "Advanced"),
    ("E101", "SQL", "Intermediate"),
    ("E102", "Excel", "Expert"),
    ("E102", "PowerBI", "Advanced"),
    ("E103", "Python", "Beginner"),
    ("E103", "Excel", "Intermediate")
]

employee_skills = {}
skill_employees = {}

for emp_id, skill, level in skills_data:
    if emp_id not in employee_skills:
        employee_skills[emp_id] = {}
    if skill not in employee_skills[emp_id]:  
        employee_skills[emp_id][skill] = level

        if skill not in skill_employees:
            skill_employees[skill] = set()
        skill_employees[skill].add(emp_id)

print("Employee to Skills Mapping:")
for emp_id, skills in employee_skills.items():
    print(f"{emp_id}: {skills}")

print("Skill to Employees Mapping:")
for skill, employees in skill_employees.items():
    print(f"{skill}: {employees}")

    
'''
output
Employee to Skills Mapping:
E101: {'Python': 'Advanced', 'SQL': 'Intermediate'}
E102: {'Excel': 'Expert', 'PowerBI': 'Advanced'}
E103: {'Python': 'Beginner', 'Excel': 'Intermediate'}
Skill to Employees Mapping:
Python: {'E101', 'E103'}
SQL: {'E101'}
Excel: {'E103', 'E102'}
PowerBI: {'E102'}
'''