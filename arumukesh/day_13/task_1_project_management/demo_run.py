import json
unique_skills=set() #for storing unique skills 
project_hours={} #for storing total project hours 
python_list=[] #for storing employee name with python skill
emp_project_hours={} #for storing project hours per employee
with open(r"C:\Users\303372\Desktop\ust_python_training\Arumukesh\day_13\task_1_project_management\data.json","r")as file:
    data=json.load(file)
    employees=data["employees"]
    for emp in employees:
        # finding pyhton skill employees and unique skills
        for skill in emp["skills"]:
            if skill=="Python":
                python_list.append(emp["name"])
            unique_skills.add(skill)
        name=emp["name"]
        # calculating the totalhours logged per project and per employee
        
        if not emp["projects"]:
            emp_project_hours[name]=0
        for project in emp["projects"]:
            if name not in emp_project_hours:
                emp_project_hours[name]=0
            emp_project_hours[name]+=project["hours_logged"]
            project_name=project["name"]
            if project_name not in project_hours:
                project_hours[project_name]=0
            project_hours[project_name]+=project["hours_logged"]
    # printing the results 
    print("Unique_skills:",unique_skills)
    print("Project_hours:",project_hours)
    print("emplyees with python skill:",python_list)
    print("Project hours worked per employee",emp_project_hours)
# writing the hours logged per project to the outfile 
with open(r"C:\Users\303372\Desktop\ust_python_training\Arumukesh\day_13\task_1_project_management\project_hours.json","w")as outfile:
    json.dump(project_hours,outfile,indent=2)

# ==================output====================

# demo_run.py
# Unique_skills: {'SQL', 'Selenium', 'Django', 'ETL', 'Spark', 'Python', 'Postman'}
# Project_hours: {'UST HealthCare Portal': 120, 'UST AI Chatbot': 85, 'UST Cloud Migration': 200}
# emplyees with python skill: ['Aarav Nair', 'Diya Gupta']
# Project hours worked per employee {'Aarav Nair': 205, 'Diya Gupta': 200, 'Sanjay Patil': 0}
