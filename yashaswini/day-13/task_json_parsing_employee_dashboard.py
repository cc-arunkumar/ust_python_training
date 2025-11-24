# JSON Parsing – Employee Project Dashboard

# Scenario
# UST maintains a central JSON file containing details about employees, their skills,
# and their assigned projects.
# Your task is to parse this JSON, extract useful insights, and generate a simple 
# Employee Project Dashboard using Python.
# Given JSON Structure
# Students will be provided with a file named data.json:
# {
#  "employees": [
#  {
#  "id": 101,
#  "name": "Aarav Nair",
#  "role": "Software Engineer",
#  "skills": ["Python", "Django", "SQL"],
#  "projects": [
#  {"name": "UST HealthCare Portal", "hours_logged": 120},
#  {"name": "UST AI Chatbot", "hours_logged": 85}
#  ]
#  },
#  {
#  "id": 102,
#  "name": "Diya Gupta",
#  "role": "Data Engineer",
#  "skills": ["Python", "ETL", "Spark"],
# Day 13 1
#  "projects": [
#  {"name": "UST Cloud Migration", "hours_logged": 200}
#  ]
#  },
#  {
#  "id": 103,
#  "name": "Sanjay Patil",
#  "role": "QA Analyst",
#  "skills": ["Selenium", "Postman"],
#  "projects": []
#  }
#  ]
# }
#  Tasks
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
# ➕ 7.Save the above dictionary as a new JSON file
# File name: project_hours.json



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