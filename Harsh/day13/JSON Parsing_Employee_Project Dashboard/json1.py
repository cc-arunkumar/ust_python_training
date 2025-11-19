import json
with open(r"C:\Users\Administrator\Desktop\Training\ust_python_training\harsh\day13\JSON Parsing_Employee_Project Dashboard\data.json") as json_data_file:
    j1 = json.load(json_data_file)
    employees = j1["employees"]
    
for emp in employees:
    print(f"{emp['name']} -- {emp['role']}")
    
print("\n")
total=0
for emp in employees:    
    for p in emp["projects"]:
        total+=(p["hours_logged"])
        print(f"{emp["name"]} --- {total}:hours")
        
print("\n")
        
skills = set()  
for emp in employees:
    skills.update(emp["skills"])
sorted_skills = sorted(skills)
print("All Skills:", sorted_skills)

print("\n")
for emp in employees:
    if "Python" in emp["skills"]:
        print(f"Names who knows Python: {emp["name"]}")

project_hours = {}
for emp in employees:
    for proj in emp["projects"]:
        project_hours[proj["name"]] = project_hours.get(proj["name"], 0) + proj["hours_logged"]
print("\n")

print("Project Hours Dictionary:")
print(project_hours)

with open("project_hours.json", "w") as f:
    json.dump(project_hours, f, indent=2)


# Aarav Nair -- Software Engineer
# Diya Gupta -- Data Engineer
# Sanjay Patil -- QA Analyst 


# Aarav Nair --- 120:hours   
# Aarav Nair --- 205:hours   
# Diya Gupta --- 405:hours   


# All Skills: ['Django', 'ETL', 'Postman', 'Python', 'SQL', 'Selenium', 'Spark']


# Names who knows Python: Aarav Nair
# Names who knows Python: Diya Gupta


# Project Hours Dictionary:
# {'UST HealthCare Portal': 120, 'UST AI Chatbot': 85, 'UST Cloud Migration': 200}