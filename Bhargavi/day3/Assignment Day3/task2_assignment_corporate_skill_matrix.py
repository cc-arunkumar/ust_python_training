# Corporate Skill Matrix 
skills_data = [
    ("E101", "Python", "Advanced"),
    ("E101", "SQL", "Intermediate"),
    ("E102", "Excel", "Expert"),
    ("E102", "PowerBI", "Advanced"),
    ("E103", "Python", "Beginner"),
    ("E103", "Excel", "Intermediate")
]

employees = {}
all_skills = set()

for e_id, skill, level in skills_data:
    if e_id not in employees:
        employees[e_id] = {}
    employees[e_id][skill] = level
    all_skills.add(skill)


python_emp = [e for e, skills in employees.items() if "Python" in skills]


three_plus = [e for e, skills in employees.items() if len(skills) >= 3]

print("Employee Skill Matrix:")
for e, skills in employees.items():
    print(e, ":", skills)

print("\nAll unique skills:", all_skills)
print("Employees who know Python:", python_emp)
print("Employees with 3 or more skills:", three_plus)

# Employee Skill Matrix:
# E101 : {'Python': 'Advanced', 'SQL': 'Intermediate'}
# E102 : {'Excel': 'Expert', 'PowerBI': 'Advanced'}
# E103 : {'Python': 'Beginner', 'Excel': 'Intermediate'}

# All unique skills: {'Excel', 'SQL', 'PowerBI', 'Python'}
# Employees who know Python: ['E101', 'E103']
# Employees with 3 or more skills: []