import json

field=["id","name","role","skills","projects"]
employees_with_python=[]
project_hours={}
def employees_with_names(employees):
    for row in employees:
        print(f"{row[field[1]]}--{row[field[2]]}")

def emp_total_hours(employees):
    for row in employees:
        my_list=row[field[4]]
        total_hours=0
        for r in my_list:
            project_hours[r["name"]]=r["hours_logged"]
            total_hours+=int(r["hours_logged"])
        print(f"{row[field[1]]}: {total_hours} hours")
def emp_skills(employees):
    my_set=set()
    for row in employees:
        skills=row[field[3]]
        for item in skills:
            my_set.add(item)
        lis=list(my_set)
        lis.sort()
    print(f"All Skills {lis}")
def emp_withpyrhon(employees):
    print("EMployees who know Python")
    for row in employees:
        skills=row[field[3]]
        if "Python" in skills:
            employees_with_python.append(row[field[1]])
    for name in employees_with_python:
        print(name)
def emp_project_hours(employees):
    for row in employees:
        my_list=row[field[4]]
        total_hours=0
        for r in my_list:
            project_hours[r["name"]]=r["hours_logged"]
    print(project_hours)
    with open("project.json","w") as file:
        json.dump(project_hours,file,indent=2)
        
        
with open("day13\data.json","r") as file:
    content=json.load(file)
    employees=content["employees"]
    employees_with_names(employees)
    emp_withpyrhon(employees)
    emp_skills(employees)
    emp_project_hours(employees)
    emp_total_hours(employees)