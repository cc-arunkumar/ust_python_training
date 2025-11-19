import json 

unique_skills = set()
dict={}

with open(r'C:\Users\Administrator\Desktop\ust_python_training\Rohit\day13\tasks\data.json', mode="r", encoding="utf-8") as file:
    data = json.load(file)
    employees = data['employees']
    
    for emp in employees:
        print(f"Employee Name: {emp['name']} , employee Role : {emp['role']}")
        
        projects = emp["projects"]
        val = 0
        for project in projects:
            try:
                val += int(project['hours_logged'])
            except:
                print(f"Hours logged data is not available for project: {project['name']}")
        
        print(f"Total hours logged by {emp['name']}: {val} hours")
        
        for skill in emp['skills']:
            if skill == "Python":
                print(f"{emp['name']} has Python skill")
            unique_skills.add(skill)
        
        if emp.get("projects"):
            for project in emp['projects']:
                dict[project['name']] = project['hours_logged']

print(dict)

with open(r'C:\Users\Administrator\Desktop\ust_python_training\Rohit\day13\tasks\project_hours.json', mode="w", encoding="utf-8") as outfile:
    json.dump(dict, outfile, indent=3)
