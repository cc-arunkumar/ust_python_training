# Assignment 2 — Corporate Skill Matrix System
# Scenario:
# UST’s L&D team wants to maintain a skill matrix for all employees.
# Every employee can have multiple skills at different proficiency levels.

skills_data=[
("E101","Python","Advanced"),
("E101","SQL","Intermediate"),
("E102","Excel","Expert"),
("E102","PowerBI","Advanced"),
("E103","Python","Beginner"),
("E103","Excel","Intermediate")
]

skills_by_emp={}

for emp,skill,level in skills_data:
    if emp not in skills_by_emp:
        skills_by_emp[emp]={}
    skills_by_emp[emp][skill]=level

skill_lookup={}

for emp,skills in skills_by_emp.items():
    for skill in skills:
        if skill not in skill_lookup:
            skill_lookup[skill]=[]
        skill_lookup[skill].append(emp)

print("Employees knowing Python:",skill_lookup.get("Python",[]))
all_skills=set()

for s in skill_lookup.keys():
    all_skills.add(s)

print("All Unique Skills:",all_skills)
multi_skill=[emp for emp,skills in skills_by_emp.items() if len(skills)>=3]
print("Employees with 3+ Skills:",multi_skill)

# sample output:

# Employees knowing Python: ['E101', 'E103']
# All Unique Skills: {'SQL', 'PowerBI', 'Python', 'Excel'}
# Employees with 3+ Skills: []