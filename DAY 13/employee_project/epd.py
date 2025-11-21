import json

input_file="DAY 13\\employee_project\\data.json"
employee_names=[]
unique_skills=set()
only_python_employee=[]
project_hours = {}

with open(input_file,"r") as ip_file:
    data=json.load(ip_file)

for emp in data["employees"]:
    
    #Displaying Employee name
    employee_names.append(f"{emp["name"]} -- {emp["role"]}\n")
    # print((f"{emp["name"]} -- {emp["role"]}\n"))

    #Each Employees working hours across all project
    total_hours=0
    for tot_hrs in emp["projects"]:
        total_hours+=tot_hrs["hours_logged"]
    print(f"{emp["name"]} : {total_hours}")

    #list of all unique skills 
    for skills in emp["skills"]:
        unique_skills.add(skills)

    #Only python knowing Employee
    if emp["skills"]==["Python"]:
        # only_python_employee.append(emp["name"])
        print(f"{emp["name"]} knows only Python")
    
    #Total working hours in project
    for pro in emp["projects"]:
        project_name=pro["name"]
        hrs=pro["hours_logged"]
        if project_name not in project_hours:
            project_hours[project_name]=0
            project_hours[project_name]+=hrs

with open("DAY 13\\employee_project\\project_hours.json","w") as project_hr:
         json.dump(project_hours, project_hr, indent=2)
 

print(employee_names)
print(unique_skills)
print(type(data))