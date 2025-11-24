# JSON Parsing  Employee Project Dashboard


import json

# 1.Load the JSON fil
with open('data.json', 'r') as data_file:
    data = json.load(data_file)

# 2.Display all employee names with their roles
print("Employee Names and Roles:")
for emp in data['employees']:
    name = emp['name']
    role = emp['role']
    print(f"{name}: {role}")

# 3.Print each employee’s total hours spent across all projects
print("\nTotal Hours Spent by Employees:")
for emp in data['employees']:
    name = emp['name']
    total_hours = sum(p['hours_logged'] for p in emp['projects'])
    print(f"{name}: {total_hours} hours")

# 4.Create a list of all unique skills across the organizatio
skills = set()
for emp in data['employees']:
    skills.update(emp['skills'])

sorted_skills = sorted(skills)
print("\nAll Skills:", sorted_skills)

# 5.Identify employees who know Python

print("\nEmployees who know Python:")
for emp in data['employees']:
    if 'Python' in emp['skills']:
        print(emp['name'])

# 6.Create a dictionary mapping each project name to total hours
# contributed by all employees
project_hours = {}
for emp in data['employees']:
    for p in emp['projects']:
        project_name = p['name']
        hours = p['hours_logged']
        if project_name not in project_hours:
            project_hours[project_name] = 0
        project_hours[project_name] += hours

print("\nProject Hours Summary:")
print(project_hours)

# 7.Save the above dictionary as a new JSON file

with open('project_hours.json', 'w') as output_file:
    json.dump(project_hours, output_file, indent=2)

print("\ndata have been saved to 'project_hours.json'.")



# Employee Names and Roles:
# Aarav Nair: Software Engineer
# Diya Gupta: Data Engineer    
# Sanjay Patil: QA Analyst     

# Total Hours Spent by Employees:
# Aarav Nair: 205 hours
# Diya Gupta: 200 hours
# Sanjay Patil: 0 hours

# All Skills: ['Django', 'ETL', 'Postman', 'Python', 'SQL', 'Selenium', 'Spark']

# Employees who know Python:
# Aarav Nair
# Diya Gupta

# Project Hours Summary:
# {'UST HealthCare Portal': 120, 'UST AI Chatbot': 85, 'UST Cloud Migration': 200}