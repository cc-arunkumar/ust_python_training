# Assignment 2 — Corporate Skill Matrix System

skills_data = [
    ("E101", "Python", "Advanced"),
    ("E101", "SQL", "Intermediate"),
    ("E102", "Excel", "Expert"),
    ("E102", "PowerBI", "Advanced"),
    ("E103", "Python", "Beginner"),
    ("E103", "Excel", "Intermediate")
]

skills = {}        
unique_skills = [] 

for emp, skill, level in skills_data:
    if emp not in skills:
        skills[emp] = {}
    if skill not in skills[emp]:  
        skills[emp][skill] = level
    if skill not in unique_skills:
        unique_skills.append(skill)

print("All Employee Skills:")
for emp in skills:
    print(emp, ":", skills[emp])

search_skill = "Python"
print("\nEmployees who know", search_skill, ":")
for emp in skills:
    if search_skill in skills[emp]:
        print(emp)

print("\nEmployees with 3 or more skills:")
for emp in skills:
    if len(skills[emp]) >= 3:
        print(emp)

print("\nAll unique skills in company:")
print(unique_skills)


#sample output
# All Employee Skills:
# E101 : {'Python': 'Advanced', 'SQL': 'Intermediate'}
# E102 : {'Excel': 'Expert', 'PowerBI': 'Advanced'}
# E103 : {'Python': 'Beginner', 'Excel': 'Intermediate'}

# Employees who know Python :
# E101
# E103

# Employees with 3 or more skills:

# All unique skills in company:
# ['Python', 'SQL', 'Excel', 'PowerBI']
