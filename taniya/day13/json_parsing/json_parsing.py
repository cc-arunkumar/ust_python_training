import json
with open(r"C:\Users\Administrator\Desktop\Training\ust_python_training\taniya\day13\data.json") as file1:
    data=json.load(file1)
    my_emp=data["employees"]
all_skills=[] 
python_emp=[]
project_hours={}  
for emp in my_emp:
    # displaying all employee
    print(f"Employee name is {emp.get("name")} and their role is {emp.get("role")}")
    # each employee total hours spent
    
    total_hours = sum(project["hours_logged"] for project in emp["projects"])
    print(f"{emp.get("name")}:{total_hours} hours\n")  
    for skill in emp["skills"]:
        
        if skill not in all_skills:
            all_skills.append(skill)
    if "Python" in emp["skills"]:
        python_emp.append(emp.get("name"))
        
    for project in emp["projects"]:
        name=project["name"]
        hours = project["hours_logged"]
        if name in project_hours:
            project_hours[name] += hours
        else:
            project_hours[name] = hours
        
all_skills.sort()
print(f"All Skills: {all_skills}\n")

print("Employees who knows python")
for name in python_emp:
    print(name)

print("\nProject-wise total hours:")
for project, hours in project_hours.items():
    print(f"{project}: {hours}")

with open("project_hours.json", "w") as file:
    json.dump(project_hours, file, indent=4)


    
    
    


            