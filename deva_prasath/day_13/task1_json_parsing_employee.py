#  Python Task: JSON Parsing – Employee 
# Project Dashboard
#  Scenario
#  UST maintains a central JSON file containing details about employees, their skills, 
# and their assigned projects.
#  Your task is to parse this JSON, extract useful insights, and generate a simple 
# Employee Project Dashboard using Python.



import json
with open(r'D:\training\ust_python_training\deva_prasath\day_13\data.json','r') as f1:
    emp=json.load(f1)

#storing list in data
data=emp['employees']
#creating empty sets and dicts
total_hours_emp={}
uniques_skills=set()
python_emp=[]
project_hours={}

#iterating through data
for row in data:
    #printing name and 
    print(f"{row['name']}--{row['role']}")
    total=0
    for i in row['projects']:
        total=total+i['hours_logged']
    total_hours_emp[row['name']]=total
    
    for j in row['skills']:
        if j not in uniques_skills:
            uniques_skills.add(j)
    
    for k in row['skills']:
        if k=="Python":
            python_emp.append(row['name'])
    sumi=0
    for d in row['projects']:
        sumi=sumi+d['hours_logged']
        for g in d['name']:
            project_hours[d['name']]=sumi

print("--------------------")
print(total_hours_emp)
print("---------------------")
print("All Skills:",uniques_skills)
print("---------------------")

print("Python skills employees:",python_emp)
print("---------------------")

print("Project hours of each project:",project_hours)

with open('project_hours.json','w') as f2:
    f2.write(json.dumps(project_hours,indent=2))
    

#Sample output

# Aarav Nair--Software Engineer
# Diya Gupta--Data Engineer
# Sanjay Patil--QA Analyst
# --------------------
# {'Aarav Nair': 205, 'Diya Gupta': 200, 'Sanjay Patil': 0}
# ---------------------
# All Skills: {'ETL', 'Spark', 'Django', 'Python', 'Selenium', 'Postman', 'SQL'}
# ---------------------
# Python skills employees: ['Aarav Nair', 'Diya Gupta']
# ---------------------
# Project hours of each project: {'UST HealthCare Portal': 120, 'UST AI Chatbot': 205, 'UST Cloud Migration': 200}
