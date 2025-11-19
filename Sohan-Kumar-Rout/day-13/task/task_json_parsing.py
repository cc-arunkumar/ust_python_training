#Task : JSON Parsing

#Code 
import json

with open("data.json") as file_data:
    d1=json.load(file_data)
    
    employees=d1["employees"]
    
unique_skills=[]
unique_count=0
project_hours={}

for emp in employees:
    print(f"{emp["name"]} --- {emp["role"]}")


    for skill in emp["skills"]:
        if skill not in unique_skills:
            unique_skills.append(skill)
            unique_skills.sort()
    sum = 0
    for projects in emp["projects"]:
        sum+=projects["hours_logged"]
    print(f"{emp["name"]}--- {sum} hours  ")
        
print("All Skills : ",unique_skills)
        
for emp in employees:
    if "Python" in emp["skills"]:
        print("Name of employee with Python skill : ",emp["name"])

for emp in employees:
    for project in emp["projects"]:
        project_name = project["name"]
        hours = project["hours_logged"]
        
        if project_name in project_hours:
            project_hours[project_name] += hours
        else:
            project_hours[project_name] = hours

print(project_hours)

with open("project_hours.json", "w") as outfile:
    json.dump(project_hours, outfile, indent=4)
    
#Output
# Aarav Nair --- Software Engineer
# Aarav Nair--- 205 hours  
# Diya Gupta --- Data Engineer
# Diya Gupta--- 200 hours
# Sanjay Patil --- QA Analyst
# Sanjay Patil--- 0 hours
# All Skills :  ['Django', 'ETL', 'Postman', 'Python', 'SQL', 'Selenium', 'Spark']
# Name of employee with Python skill :  Aarav Nair
# Name of employee with Python skill :  Diya Gupta
# {'UST HealthCare Portal': 120, 'UST AI Chatbot': 85, 'UST Cloud Migration': 200}


    
