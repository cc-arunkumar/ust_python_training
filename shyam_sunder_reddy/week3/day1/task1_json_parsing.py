# Day 13
# Python Task: JSON Parsing – Employee
# Project Dashboard
# Scenario
# UST maintains a central JSON file containing details about employees, their skills,
# and their assigned projects.
# Your task is to parse this JSON, extract useful insights, and generate a simple 
# Employee Project Dashboard using Python.
import json

with open("data.json","r") as file:
    reader=json.load(file)

data=reader["employees"]

department=[]
total_hours=[]
skills=[]
python=[]
projects={}
for row in data:
    # 2.Display all employee names with their roles
    # Output format example:
    # Aarav Nair — Software Engineer
    # Diya Gupta — Data Engineer
    # ...
    department.append({"name":row["name"],"role":row["role"]})
    total=0
    for t in row["projects"]:
        total+=t["hours_logged"]
        # 6.Create a dictionary mapping each project name to total hours
        # contributed by all employees
        # Example:
        # {
        # "UST HealthCare Portal": 120,
        # "UST AI Chatbot": 85,
        # "UST Cloud Migration": 200
        # }
        projects[t["name"]]=projects.get(t["name"],0)+t["hours_logged"]
        
    # 3.Print each employee’s total hours spent across all projects
    # Example:
    # Aarav Nair: 205 hours
    # Diya Gupta: 200 hours
    # Sanjay Patil: 0 hours
    total_hours.append({"name":row["name"],"hours_logged":total})
    for s in row["skills"]:
       
        # 4.Create a list of all unique skills across the organization
        # Sort the list alphabetically.
        # Expected output:
        # All Skills: ['Django', 'ETL', 'Postman', 'Python', 'SQL', 'Selenium', 'Spark']
        if s not in skills:
            skills.append(s)
        
        # 5.Identify employees who know Python
        # Print only names
        if s.lower()=="python":
            python.append(row["name"])

with open("project_hours.json","w") as file:
    writer=json.dump(projects,file,indent=2)
    
# print(department)
for row in department:
    print(f"{row["name"]}--{row["role"]}")
print("=======================")
# print(total_hours)
for row in total_hours:
    print(f"{row["name"]}:{row["hours_logged"]}hours")
print("=======================")
print("All Skills: ",skills)
print("=======================")
print("People with python as skill: ",python)

#Sample output
# Aarav Nair--Software Engineer
# Diya Gupta--Data Engineer
# Sanjay Patil--QA Analyst
# =======================
# Aarav Nair:205hours
# Diya Gupta:200hours
# Sanjay Patil:0hours
# =======================
# All Skills:  ['Python', 'Django', 'SQL', 'ETL', 'Spark', 'Selenium', 'Postman']
# =======================
# People with python as skill:  ['Aarav Nair', 'Diya Gupta']