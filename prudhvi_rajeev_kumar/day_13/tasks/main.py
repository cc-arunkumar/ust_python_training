import json

file_path = r"C:\Users\Administrator\Desktop\Prudhvi_Rajeev\ust_python_training\prudhvi_rajeev_kumar\day_13\tasks\data.json"


with open(file_path, mode='r') as outfile:
    json_loader = json.load(outfile)

project_hours = {}
unique_skills = set()
employee_with_python = []
employees = json_loader["employees"]

for emp in employees:
    print(f"Employee name : {emp['name']} ---- Employee role : {emp['role']}")
    
for emp in employees:
    total_hours = 0
    for emp_pro in emp["projects"]:
        if emp_pro["hours_logged"] == 0:
            total_hours = 0
        elif emp_pro["hours_logged"] > 0:
            total_hours += emp_pro["hours_logged"]
    print(f"Name : {emp['name']} and hours logged in is : {total_hours}")

for emp in employees:
    unique_skills.update(emp["skills"])
print(f"Unique_skills : {list(unique_skills)}")

for emp in employees:
    for skills in emp["skills"]:
        if skills == "Python" or skills == "python":
            employee_with_python.append(emp["name"])
print(f"Employees with python : {employee_with_python}")

for emp in employees:
    for proj in emp["projects"]:
        name = proj["name"]
        hours = proj["hours_logged"]
        project_hours[name] = project_hours.get(name, 0) + hours
        
with open("project_hours.json", mode='w') as output:
    json.dump(project_hours, output, indent=4)



#Output:
# Employee name : Aarav Nair ---- Employee role : Software Engineer
# Employee name : Diya Gupta ---- Employee role : Data Engineer
# Employee name : Sanjay Patil ---- Employee role : QA Analyst
# Name : Aarav Nair and hours logged in is : 205
# Name : Diya Gupta and hours logged in is : 200
# Name : Sanjay Patil and hours logged in is : 0
# Unique_skills : ['Spark', 'Django', 'SQL', 'Postman', 'Selenium', 'ETL', 'Python']       
# Employees with python : ['Aarav Nair', 'Diya Gupta']
    
    

