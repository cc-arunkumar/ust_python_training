skills_data = [
    ("E101", "Python", "Advanced"),
    ("E101", "SQL", "Intermediate"),
    ("E102", "Excel", "Expert"),
    ("E102", "PowerBI", "Advanced"),
    ("E103", "Python", "Beginner"),
    ("E103", "Excel", "Intermediate")
]

employee_skills = {}

for eid, skill, level in skills_data:
    if eid not in employee_skills:
        employee_skills[eid] = {}
    employee_skills[eid][skill] = level

unique_skills = set()
for skills in employee_skills.values():
    for s in skills:
        unique_skills.add(s)

search_skill = input("Enter skill to search: ")
knows_skill = []
for eid, skills in employee_skills.items():
    if search_skill in skills:
        knows_skill.append(eid)


def add_or_update_skill(eid, skill, level):
    if eid not in employee_skills:
        employee_skills[eid] = {}
    employee_skills[eid][skill] = level
    print(eid, "skill added:", skill, "-", level)

add_or_update_skill("E103", "PowerBI", "Advanced")

multi_skill_emp = []
for eid, skills in employee_skills.items():
    if len(skills) >= 3:
        multi_skill_emp.append(eid)

print("\nEmployee Skill Matrix:")
for eid, skills in employee_skills.items():
    print(eid, ":", skills)

print("\nEmployees who know", search_skill, ":", knows_skill)
print("\nEmployees with 3 or more skills:", multi_skill_emp)
print("\nAll Unique Skills:", unique_skills)

# Enter skill to search: Python
# E103 skill added: PowerBI - Advanced

# Employee Skill Matrix:
# E101 : {'Python': 'Advanced', 'SQL': 'Intermediate'}
# E102 : {'Excel': 'Expert', 'PowerBI': 'Advanced'}
# E103 : {'Python': 'Beginner', 'Excel': 'Intermediate', 'PowerBI': 'Advanced'}

# Employees who know Python : ['E101', 'E103']

# Employees with 3 or more skills: ['E103']