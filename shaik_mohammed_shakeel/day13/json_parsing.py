import json

#1.Load the JSON file
#Use Python’s json module to load the JSON data.

with open("data.json", "r") as file:
    data = json.load(file)
    # print(data)

# 2.Display all employee names with their roles
# Output format example:
# Aarav Nair — Software Engineer
# Diya Gupta — Data Engineer
# ...

    employees = data["employees"]
for emp in employees:
    print(f"{emp['name']} - {emp['role']}")
print()


# 3.Print each employee’s total hours spent across all projects
# Example:
# Aarav Nair: 205 hours
# Diya Gupta: 200 hours
# Sanjay Patil: 0 hours

for emp in employees:
    total = 0
    for proj in emp["projects"]:
        total += proj["hours_logged"]
    print(emp["name"],total," - " "hours")
print()


# 4.Create a list of all unique skills across the organization
# Sort the list alphabetically.
# Expected output:
# All Skills: ['Django', 'ETL', 'Postman', 'Python', 'SQL', 'Selenium', 'Spark']

skills = []
for emp in employees:
    for skill in emp["skills"]:
        if skill not in skills:
            skills.append(skill)
skills.sort()
print(skills)
print()


# 5.Identify employees who know Python
# Print only names.

for emp in employees:
    for i in emp['skills']:
        if "Python"==i:
            print(emp['name'])
print()


# 6.Create a dictionary mapping each project name to total hours
# contributed by all employees
# Example:
# {
#  "UST HealthCare Portal": 120,
#  "UST AI Chatbot": 85,
#  "UST Cloud Migration": 200
# }

dic={}
for emp in employees:
    for proj in emp['projects']:
        name=proj['name']
        hours=proj['hours_logged']

        if name not in dic:
            dic[name]=hours
        else:
            dic[name]+=hours
print(dic)


#  7.Save the above dictionary as a new JSON file
# File name: project_hours.json

with open("project_hours.json",'w') as file:
    json.dump(dic,file,indent=2)


#Sample Output

# Aarav Nair - Software Engineer
# Diya Gupta - Data Engineer
# Sanjay Patil - QA Analyst

# Aarav Nair 205  - hours
# Diya Gupta 200  - hours
# Sanjay Patil 0  - hours

# ['Django', 'ETL', 'Postman', 'Python', 'SQL', 'Selenium', 'Spark']

# Aarav Nair
# Diya Gupta

# {'UST HealthCare Portal': 120, 'UST AI Chatbot': 85, 'UST Cloud Migration': 200}





