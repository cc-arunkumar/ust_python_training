#Task Employee Project Dashboard

import json
with open("data.json","r")as file1:
    json_reader=json.load(file1)
    emp=json_reader["employees"]
    unique_skills=[]
    emp_python=[]
    hours_logged=0
    dict_map={}
    for e in emp:
        print(f"Name: {e["name"]} - Role: {e["role"]}")
        for skill in e["skills"]:
            if skill not in unique_skills:
                unique_skills.append(skill)
            if skill=="Python":
                emp_python.append(e["name"])
        hours_logged=0
        for e2 in e["projects"]:
            hours_logged+=e2["hours_logged"]
            dict_map[e2["name"]]=e2["hours_logged"]
        print(f"Name: {e["name"]}: {hours_logged} hours")
    print("Unique Skills",sorted(unique_skills))
    print("Employee names who knows python",emp_python)


with open("project_hours.json","w")  as file2:
    write_json=json.dump(dict_map,file2,indent=2)


#Sample Execution
# Name: Aarav Nair - Role: Software Engineer
# Name: Aarav Nair: 205 hours
# Name: Diya Gupta - Role: Data Engineer
# Name: Diya Gupta: 200 hours
# Name: Sanjay Patil - Role: QA Analyst
# Name: Sanjay Patil: 0 hours
# Unique Skills ['Django', 'ETL', 'Postman', 'Python', 'SQL', 'Selenium', 'Spark']
# Employee names who knows python ['Aarav Nair', 'Diya Gupta']