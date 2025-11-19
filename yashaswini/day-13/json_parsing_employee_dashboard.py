import json

with open("data.json","r") as f:
    data = json.load(f)
    
employees = data[list(data.keys())[0]]

for employee in employees:
    emp_keys = list(employee.keys())
    name = employee[emp_keys[1]]
    role = employee[emp_keys[2]]
    print(name,"-",role)
    
print("<<<<<<<<<< Total hours spent by each employee >>>>>>>>>>")   
for employee in employees:
    emp_keys = list(employee.keys())
    name = employee[emp_keys[1]]
    projects = employee[emp_keys[4]]
    total_hours = 0

    for project in projects:
        project_keys = list(project.keys())
        hours_logged = project[project_keys[1]]
        total_hours = total_hours + hours_logged
    
    print(name + ":", str(total_hours) + " hours")
    
all_skills = []
for employee in employees:
    emp_keys = list(employee.keys())
    skills_list = employee[emp_keys[3]]
    for skill in skills_list:
        if skill not in all_skills:
            all_skills.append(skill)

all_skills.sort()
print("All Skills:",all_skills)
print("<<<<<<<<<< Employees who know python >>>>>>>>>>")
for employee in employees:
    emp_keys = list(employee.keys())
    if "Python" in employee[emp_keys[3]]:
        print(employee[emp_keys[1]])

project_hours = {}
for employee in employees:
    emp_keys = list(employee.keys())
    for project in employee[emp_keys[4]]:
        project_keys = list(project.keys())
        pname = project[project_keys[0]]
        phours = project[project_keys[1]]
        project_hours[pname] = project_hours.get(pname, 0) + phours
print(project_hours)

with open("project_hours.json", "w") as f:
    json.dump(project_hours, f, indent=2)
    

#o/p:
# Aarav Nair - Software Engineer
# Diya Gupta - Data Engineer
# Sanjay Patil - QA Analyst
# <<<<<<<<<< Total hours spent by each employee >>>>>>>>>>
# Aarav Nair: 205 hours
# Diya Gupta: 200 hours
# Sanjay Patil: 0 hours
# All Skills: ['Django', 'ETL', 'Postman', 'Python', 'SQL', 'Selenium', 'Spark']
# <<<<<<<<<< Employees who know python >>>>>>>>>>
# Aarav Nair
# Diya Gupta
# {'UST HealthCare Portal': 120, 'UST AI Chatbot': 85, 'UST Cloud Migration': 200}