# task_json_parsing_employee_project_dashboard

# Your Tasks
# 1.Load the JSON file
# Use Python’s json module to load the JSON data.
# 2.Display all employee names with their roles
# Output format example:
# Aarav Nair — Software Engineer
# Diya Gupta — Data Engineer
# ...
# 3.Print each employee’s total hours spent across all projects
# Example:
# Aarav Nair: 205 hours
# Diya Gupta: 200 hours
# Sanjay Patil: 0 hours
# Day 13 2
# 4.Create a list of all unique skills across the organization
# Sort the list alphabetically.
# Expected output:
# All Skills: ['Django', 'ETL', 'Postman', 'Python', 'SQL', 'Selenium', 'Spark']
# 5.Identify employees who know Python
# Print only names.
# 6.Create a dictionary mapping each project name to total hours
# contributed by all employees
# Example:
# {
#  "UST HealthCare Portal": 120,
#  "UST AI Chatbot": 85,
#  "UST Cloud Migration": 200
# }
# 7.Save the above dictionary as a new JSON file
# File name: project_hours.json


# 1.Load the JSON file
# Use Python’s json module to load the JSON data.
import json

with open("employees.json","r") as file:
    json_reader = json.load(file)


# 2.Display all employee names with their roles
# Output format example:
# Aarav Nair — Software Engineer
# Diya Gupta — Data Engineer

employee_data = json_reader["employees"]

for emp in employee_data:
    print(f"{emp['name']} - {emp['role']}")
    print()


# 3.Print each employee’s total hours spent across all projects
# Example:
# Aarav Nair: 205 hours
# Diya Gupta: 200 hours
# Sanjay Patil: 0 hours


for emp in employee_data:
    total = 0
    for p in emp["projects"]:
        total += p['hours_logged']
        print(f"{emp['name']} - {total}hours")


# 4.Create a list of all unique skills across the organization
# Sort the list alphabetically.

all_skills = set()
for emp in employee_data:
    for skill in emp['skills']:
        all_skills.add(skill)
 
all_skills = sorted(all_skills)
print("All Skills:", all_skills)
print()


# 5.Identify employees who know Python
# Print only names.

for emp in employee_data:
    if "Python" in emp["skills"]:
        print(emp["name"])
print()

# 6.Create a dictionary mapping each project name to total hours
# contributed by all employees
    
project_hours = {}

for emp in employee_data:
    for project in emp["projects"]:
        name = project["name"]
        hours = project["hours_logged"]
        if name in project_hours:
            project_hours[name] += hours
        else:
            project_hours[name] = hours

print("Project Hours Dictionary:")
print(project_hours)
print()

# 7.Save the above dictionary as a new JSON file
# File name: project_hours.json

with open("project_hours.json","w") as outfile:
    json.dump(project_hours,outfile,indent=2)

# ---------------------------------------------------------------------------------------------

# Sample Output

# Aarav Nair - Software Engineer

# Diya Gupta - Data Engineer

# Sanjay Patil - QA Analyst

# Aarav Nair - 120hours
# Aarav Nair - 205hours
# Diya Gupta - 200hours
# All Skills: ['Django', 'ETL', 'Postman', 'Python', 'SQL', 'Selenium', 'Spark']

# Aarav Nair
# Diya Gupta

# Project Hours Dictionary:
# {'UST HealthCare Portal': 120, 'UST AI Chatbot': 85, 'UST Cloud Migration': 200}






import json

with open("employees.json","r") as file:
    json_reader = json.load(file)


# 2.Display all employee names with their roles
# Output format example:
# Aarav Nair — Software Engineer
# Diya Gupta — Data Engineer

employee_data = json_reader["employees"]

headers = list(employee_data[0].keys())

for emp in employee_data:
    print(f"{emp[headers[1]]} - {emp[headers[2]]}")
    print()


# 3.Print each employee’s total hours spent across all projects
# Example:
# Aarav Nair: 205 hours
# Diya Gupta: 200 hours
# Sanjay Patil: 0 hours


for emp in employee_data:
    total = 0
    for p in emp[headers[4]]:
        total += p['hours_logged']
        print(f"{emp['name']} - {total}hours")


# 4.Create a list of all unique skills across the organization
# Sort the list alphabetically.

all_skills = set()
for emp in employee_data:
    for skill in emp[headers[3]]:
        all_skills.add(skill)
 
all_skills = sorted(all_skills)
print("All Skills:", all_skills)
print()


# 5.Identify employees who know Python
# Print only names.

for emp in employee_data:
    if "Python" in emp[headers[3]]:
        print(emp[headers[1]])
print()

# 6.Create a dictionary mapping each project name to total hours
# contributed by all employees
    
project_hours = {}

for emp in employee_data:
    for project in emp[headers[4]]:
        name = project["name"]
        hours = project["hours_logged"]
        if name in project_hours:
            project_hours[name] += hours
        else:
            project_hours[name] = hours

print("Project Hours Dictionary:")
print(project_hours)
print()

# 7.Save the above dictionary as a new JSON file
# File name: project_hours.json

with open("project_hours.json","w") as outfile:
    json.dump(project_hours,outfile,indent=2)