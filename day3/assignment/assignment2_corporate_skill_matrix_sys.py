skills_data = [
 ("E101", "Python", "Advanced"),
 ("E101", "SQL", "Intermediate"),
 ("E102", "Excel", "Expert"),
 ("E102", "PowerBI", "Advanced"),
 ("E103", "Python", "Beginner"),
 ("E103", "Excel", "Intermediate")
]
employee_skills = {}
skill_employee = {}
for emp_id,skills,level in skills_data:
    if emp_id not in employee_skills:
        employee_skills[emp_id]={}
    employee_skills[emp_id][skills] = level
    if skills not in skill_employee:
        skill_employee[skills]=set()
    skill_employee[skills].add(emp_id)

print("Employee skills data:")
for emp,skillss in employee_skills.items():
    print(emp,":",skillss)

python_emp = skill_employee.get("Python",set())
print("Employees who know python:",python_emp)

unique_skills = set(skill_employee.keys())
print("all unique skills are:",unique_skills)

more_three_skills = [emp for emp, skills in employee_skills.items() if len(skills) >= 3]
print("Employee with 3 or more skills:",more_three_skills)

# output

