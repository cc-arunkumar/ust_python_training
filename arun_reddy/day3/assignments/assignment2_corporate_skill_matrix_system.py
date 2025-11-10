skills_data = [
    ("E101", "Python", "Advanced"),
    ("E101", "SQL", "Intermediate"),
    ("E102", "Excel", "Expert"),
    ("E102", "PowerBI", "Advanced"),
    ("E103", "Python", "Beginner"),
    ("E103", "Excel", "Intermediate")
]


employee_skills = {}

for empid, skill, proficiency in skills_data:
    if empid not in employee_skills:
        employee_skills[empid] = set()
    employee_skills[empid].add(skill)

print(employee_skills)



# Find employees with 3 or more skills
my_set = set()
for key, val in employee_skills.items():
    if len(val) >= 3:
        my_set.add(key)

print("Employees with 3 or more skills:", my_set)




# =============Sample Execution==============
# {'E101': {'SQL', 'Python'}, 'E102': {'PowerBI', 'Excel'}, 'E103': {'Excel', 'Python'}}
# Employees with 3 or more skills: set()