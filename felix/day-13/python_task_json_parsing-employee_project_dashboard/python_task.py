import json

with open("data.json","r") as data:
    employee_data = json.load(data)
    employee = employee_data["employees"]
    
    fields = list(employee[0].keys())
    project_fields = list(employee[0][fields[4]][0].keys())
    for emp in employee:
        print(f"{emp[fields[1]]} -- {emp[fields[2]]}")
        
    print("\n========================\n")
    
    for emp in employee:
        total_hours = 0
        for project in emp[fields[4]]:
            total_hours += project[project_fields[1]]
        print(f"{emp[fields[1]]}: {total_hours} hours")
        
    print("\n========================\n")   
    
    unique_skills = []
    for emp in employee:
        unique_skills.extend(emp[fields[3]])
        
    print("All Skills: ",sorted(set(unique_skills)))
    
    print("\n========================\n")
    
    print("Employees who know python:")
    for emp in employee:
        if "Python" in emp[fields[3]]:
            print(emp[fields[1]])
            
    print("\n========================\n")  
          
    projects_data = {}
    for emp in employee:
        for project in emp[fields[4]]:
            if project[project_fields[0]] in projects_data:
                projects_data[project[project_fields[0]]] += project[project_fields[1]]
            else:
                projects_data[project[project_fields[0]]] = project[project_fields[1]]
    
    with open("project_hours.json","w") as new_json:
        json.dump(projects_data,new_json,indent=2)
        