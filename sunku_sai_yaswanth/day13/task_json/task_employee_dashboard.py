import json
with open("C:/Users/Administrator/Desktop/sunku_sai_yaswanth/day13/task_json/data.json",'r')as file:
    json_file=json.load(file)
    data=json_file["employees"]
    for emp in data:
        print(f"{emp.get("name")}------{emp.get("role")}")
    for emp in data:
        for project in emp.get("projects",[]):
            print(f"{emp.get("name")}----{project.get("hours_logged")}")
    skills=[]
    for emp in data:
        skills.extend(emp["skills"])
    print(f"skill:{skills}")
    for emp in data:
        if "Python" in emp["skills"]:
            print(f"name:{emp.get("name")} has python skills")
    project_hours_worked={}
    for emp in data:
        for project in emp.get("projects",[]):
            project_name=project.get("name")
            project_hours=project.get("hours_logged")
            if project_name in project_hours_worked:
                project_hours_worked[project_name]+=project_hours
            else:
                project_hours_worked[project_name]=project_hours
with open("project_hours_worked.json",'w',newline="")as file2:
    hours_worked=json.dump(project_hours_worked,file2,indent=2)
    
    
# Aarav Nair------Software Engineer
# Diya Gupta------Data Engineer
# Sanjay Patil------QA Analyst
# Aarav Nair----120
# Aarav Nair----85
# Diya Gupta----200
# skill:['Python', 'Django', 'SQL', 'Python', 'ETL', 'Spark', 'Selenium', 'Postman']
# name:Aarav Nair has python skills
# name:Diya Gupta has python skills


        
