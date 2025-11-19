# Python Task: JSON Parsing – Employee Project Dashboard

# Scenario
# UST maintains a central JSON file containing details about employees, their skills,
# and their assigned projects.
# Your task is to parse this JSON, extract useful insights, and generate a simple 
# Employee Project Dashboard using Python.
import json
#open json file 
with open('data.json','r') as file:
    reader = json.load(file)
    employees_data = reader['employees']

unique_skills = []
python_skilled_emp=[]
projects_dic = {}
#Display all employee names with their roles 
headers = list(employees_data[0].keys())

for emp in employees_data:
    print(f'{emp[headers[1]]} - {emp[headers[2]]}')
print('\n=================================\n')
for emp in employees_data:
    hours = 0
    for skill in emp[headers[3]]:
        if skill.lower() == "python":
            python_skilled_emp.append(emp[headers[1]])
        if skill not in unique_skills:
            unique_skills.append(skill)
    for project in emp[headers[4]]:
        if project['name'] not in projects_dic:
            projects_dic[project['name']] = project['hours_logged']
        
        hours += project['hours_logged']
    # Print each employee’s total hours spent across all projects
    print(f'{emp[headers[1]]}: {hours} Hours ')
print('\n=================================\n')
print(f"\nAll Skills: {unique_skills}")
print('\n=================================\n')
print(f"\nPython Skilled Employees: {python_skilled_emp}")
print('\n=================================\n')
print(f"\nProjects and Total Hours Logged:", projects_dic)
    
with open('project_hours.json','w') as file:
    json.dump(projects_dic,file,indent=2)

#Sample Output
# Aarav Nair - Software Engineer
# Diya Gupta - Data Engineer
# Sanjay Patil - QA Analyst

# =================================

# Aarav Nair: 205 Hours
# Diya Gupta: 200 Hours
# Sanjay Patil: 0 Hours

# =================================


# All Skills: ['Python', 'Django', 'SQL', 'ETL', 'Spark', 'Selenium', 'Postman']

# =================================


# Python Skilled Employees: ['Aarav Nair', 'Diya Gupta']

# =================================

# Projects and Total Hours Logged: {'UST HealthCare Portal': 120, 'UST AI Chatbot': 85, 'UST Cloud Migration': 200}



#project_hours.json 
#     {
#   "UST HealthCare Portal": 120,
#   "UST AI Chatbot": 85,
#   "UST Cloud Migration": 200
#     }