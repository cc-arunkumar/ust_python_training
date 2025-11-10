#corporate skill matrix

skills_data = [
    ("E201", "Python", "Advanced"),
    ("E201", "SQL", "Intermediate"),
    ("E201", "Java", "Beginner"),
    ("E202", "Excel", "Expert"),
    ("E202", "PowerBI", "Advanced"),
    ("E203", "Python", "Intermediate"),
    ("E203", "Excel", "Intermediate"),
    ("E203", "Tableau", "Beginner"),
    ("E204", "SQL", "Advanced")
]
employees = {}
for emp_id, skill, level in skills_data:
    if emp_id not in employees:
        employees[emp_id] = {}
    employees[emp_id][skill] = level
skill_to_employees = {}
for emp_id, skills in employees.items():
    for skill in skills:
        if skill not in skill_to_employees:
            skill_to_employees[skill] = []
        skill_to_employees[skill].append(emp_id)
unique_skills = set(skill for skills in employees.values() for skill in skills)
three_plus_skills = [emp for emp, skills in employees.items() if len(skills) >= 3]
print("Employees by skill:", skill_to_employees)
print("Unique skills:", unique_skills)
print("Employees with 3 or more skills:", three_plus_skills)
new_skill = ("E202", "Python", "Intermediate")
emp_id, skill, level = new_skill
if emp_id not in employees:
    employees[emp_id] = {}
employees[emp_id][skill] = level
if skill not in skill_to_employees:
    skill_to_employees[skill] = []
if emp_id not in skill_to_employees[skill]:
    skill_to_employees[skill].append(emp_id)
print("After adding/updating new skill:")
print("Employees by skill:", skill_to_employees)
print("Unique skills:", set(skill for skills in employees.values() for skill in skills))
 
 
#o/p:
# Employees by skill: {'Python': ['E201', 'E203'], 'SQL': ['E201', 'E204'], 'Java': ['E201'], 'Excel': ['E202', 'E203'], 'PowerBI': ['E202'], 'Tableau': ['E203']}
# Unique skills: {'PowerBI', 'Python', 'SQL', 'Tableau', 'Excel', 'Java'}
# Employees with 3 or more skills: ['E201', 'E203']
# After adding/updating new skill:
# Employees by skill: {'Python': ['E201', 'E203', 'E202'], 'SQL': ['E201', 'E204'], 'Java': ['E201'], 'Excel': ['E202', 'E203'], 'PowerBI': ['E202'], 'Tableau': ['E203']}
# Unique skills: {'PowerBI', 'Python', 'SQL', 'Tableau', 'Excel', 'Java'}