import json

all_skills=[]
py_emp=[]
proj_dict={}
with open("data.json","r")as f:
    data=json.load(f)
    employees=data.get("employees")
    for emp in employees:
        print(emp.get("name"),emp.get("role"))
        for x in emp.get("skills"):
            if x=="Python":
                py_emp.append(emp.get("name"))
            if x not in all_skills:
                all_skills.append(x)
            
                
        
    
    for emp in employees:
        total=0
        for i in emp.get("projects"):
            proj_dict[i.get("name")]=i.get("hours_logged")
            total+=i.get("hours_logged")
        print(emp.get("name"),total)
all_skills.sort()
print(all_skills)
print(py_emp)
print(proj_dict)

with open("project_hours.json","w")as f:
    json.dump(proj_dict,f,indent=2)