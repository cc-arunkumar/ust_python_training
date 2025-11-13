skills_data = [
 ("E101", "Python", "Advanced"),
 ("E101", "SQL", "Intermediate"),
 ("E102", "Excel", "Expert"),
 ("E102", "PowerBI", "Advanced"),
 ("E103", "Python", "Beginner"),
 ("E103", "Excel", "Intermediate"),
 ("E101", "Java", "Advanced"),
 ("E103", "SQL", "Beginner")
]
unique_skills={}
unique_employees={}
for emp_id,skills,level in skills_data:
    if(emp_id not in unique_skills):
        unique_skills[emp_id]={}
    unique_skills[emp_id][skills]=level

    if(skills not in unique_employees ):
        unique_employees[skills]={}
    unique_employees[skills][emp_id]=level

print("Employees having unique skills: ",unique_skills)
print("Unique Skills align with employees: ",unique_employees)
print("Get all employees with unique skills: ",list(unique_skills.keys()))
print("Employee Id with 3 or more skills",[emp for emp,skills in unique_skills.items() if len(skills)>=3])


#Sample Execution
# Employees having unique skills:  {'E101': {'Python': 'Advanced', 'SQL': 'Intermediate', 'Java': 'Advanced'}, 'E102': {'Excel': 'Expert', 'PowerBI': 'Advanced'}, 'E103': {'Python': 'Beginner', 'Excel': 'Intermediate', 'SQL': 'Beginner'}}
# Unique Skills align with employees:  {'Python': {'E101': 'Advanced', 'E103': 'Beginner'}, 'SQL': {'E101': 'Intermediate', 'E103': 'Beginner'}, 'Excel': {'E102': 'Expert', 'E103': 'Intermediate'}, 'PowerBI': {'E102': 'Advanced'}, 'Java': {'E101': 'Advanced'}}
# Get all employees with unique skills:  ['E101', 'E102', 'E103']
# Employee Id with 3 or more skills ['E101', 'E103']