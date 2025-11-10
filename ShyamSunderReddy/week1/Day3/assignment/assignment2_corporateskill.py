#Assignment 2 — Corporate Skill Matrix System
skills_data = [
 ("E101", "Python", "Advanced"),
 ("E101", "SQL", "Intermediate"),
 ("E102", "Excel", "Expert"),
 ("E102", "PowerBI", "Advanced"),
 ("E103", "Python", "Beginner"),
 ("E103", "Excel", "Intermediate"),
 ("E103", "SQL", "Advanced"),
 ("E103", "PowerBI", "Beginner")
]
employee_skills = {}
skill_data={}

for emp_id,skill,level in skills_data:
    
    if emp_id not in employee_skills:
        employee_skills[emp_id] = []
    employee_skills[emp_id].append((skill, level))

    if skill not in skills_data:
        skill_data[skill]=[]
    skill_data[skill].append(emp_id)

threeplusskills=[]
for emp_id, skills in employee_skills.items():
    if len(skills) > 3:
        threeplusskills.append(emp_id)

print("Employees with more than 3 skills:", threeplusskills)

#Sample output
#Employees with more than 3 skills: ['E103']