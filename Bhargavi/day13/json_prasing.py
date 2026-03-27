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

# 4.Create a list of all unique skills across the organization
# Sort the list alphabetically.
# Expected output:
# All Skills: ['Django', 'ETL', 'Postman', 'Python', 'SQL', 'Selenium', 'Spark']

# 5.Identify employees who know Python
# Print only names.

# 6.Create a dictionary mapping each project name to total hours
# contributed by all employees

# {
#  "UST HealthCare Portal": 120,
#  "UST AI Chatbot": 85,
#  "UST Cloud Migration": 200
# }

import json

#read the json file for data
with open("data.json","r") as f:
    reader = json.load(f)
employees = reader["employees"]
print("total:" , len(employees))

#1st step print employee role an the name
print("employee - role")
for emp in employees:
    print(emp["name"],"-",emp["role"])

print("*************")   

#2nd step hours worked by the employee
print("total hours  per employee")
for emp in employees:
    total = 0
    for project in emp["projects"]:
        total += project["hours_logged"]
    print(f"{emp['name']}: {total} hours")

#unique skills set  
print("unique skill set")
skills_set = set()   

print("*******")
for emp in employees:
    for skill in emp["skills"]:
        skills_set.add(skill) 

skills_list = sorted(skills_set)
print(skills_list)

print("******")

# employeee who knows the python
print("\nEmployees who know Python:")
for emp in employees:
    if "Python" in emp["skills"]:
        print(emp["name"])

print("*******")

#respective projects worked
project_hours = {}

for emp in employees:
    for proj in emp["projects"]:
        name = proj["name"]
        hours = proj["hours_logged"]
        if name in project_hours:
            project_hours[name] += hours
        else:
            project_hours[name] = hours

print(project_hours)

print("************")

#create json file to dump data
with open("project_hours.json", "w") as f:
    json.dump(project_hours, f, indent=2)

print("the project is stroed in  project_hours_json")

#output
# total: 3
# employee - role
# Aarav Nair - Software Engineer
# Diya Gupta - Data Engineer
# Sanjay Patil - QA Analyst
# *************
# total hours  per employee
# Aarav Nair: 205 hours
# Diya Gupta: 200 hours
# Sanjay Patil: 0 hours
# unique skill set
# *******
# ['Django', 'ETL', 'Postman', 'Python', 'SQL', 'Selenium', 'Spark']
# ******

# Employees who know Python:
# Aarav Nair
# Diya Gupta
# *******
# {'UST HealthCare Portal': 120, 'UST AI Chatbot': 85, 'UST Cloud Migration': 200}
# ************
# the project is stroed in  project_hours_json
