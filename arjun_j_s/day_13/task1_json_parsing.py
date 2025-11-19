import json

path = "C:/Users/303391/Desktop/ust_python_training/arjun_j_s/day_13/"

with open(path+"data.json","r") as emp_file:
    emp_data = json.load(emp_file)

emp_list = emp_data["employees"]

python_emp=[]
print("Employee Names along with Roles")
for data in emp_list:
    for x in data["skills"]:
        if(x=="Python" and data["name"] not in python_emp):
            python_emp.append(data["name"])
    print(f"{data["name"]}--{data["role"]}")

unique_skills=[]

project_dict = {}
print("\nEmployee Names along with total hr in all project")
for data in emp_list:
    for x in data["skills"]:
        if(x not in unique_skills):
            unique_skills.append(x)
    for hrs in data["projects"]:
        project_dict[hrs["name"]]=hrs["hours_logged"]
    print(f"{data["name"]}--{sum(x["hours_logged"] for x in data["projects"])}")

unique_skills.sort()
print("\nAll Skills :",unique_skills)

print("\nAll python employees :",python_emp)


with open(path+"project_hours.json","w") as project_file:
    json.dump(project_dict,project_file,indent=2)

#Output
# Employee Names along with Roles
# Aarav Nair--Software Engineer
# Diya Gupta--Data Engineer
# Sanjay Patil--QA Analyst

# Employee Names along with total hr in all project
# Aarav Nair--205
# Diya Gupta--200
# Sanjay Patil--0

# All Skills : ['Django', 'ETL', 'Postman', 'Python', 'SQL', 'Selenium', 'Spark']

# All python employees : ['Aarav Nair', 'Diya Gupta']