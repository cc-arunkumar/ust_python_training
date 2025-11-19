# Python Task: JSON Parsing – Employee Project Dashboard
# Scenario
# UST maintains a central JSON file containing details about employees, their skills,
# and their assigned projects.
# Your task is to parse this JSON, extract useful insights, and generate a simple 
# Employee Project Dashboard using Python.

import json      

# Open the JSON file in read mode
with open("data.json", "r") as file:
    json_reader = json.load(file)   

# Extract the list of employees
new_data = json_reader["employees"]

header = list(new_data[0].keys())

# Create an empty set to store unique skills
unique_skills = set()

# Create an empty dictionary to store project hours
project_dict = {}

for val in new_data:

    print(f"{val[header[1]]}-{val[header[2]]}")
print("\n--------------------\n")

for row in new_data:
    # Extract the list of projects for this employee
    project_data = row["projects"]

    # Variable to store total hours for all project
    total = 0  

    for k in project_data:

        project_header = list(k.keys())

        total += k[project_header[1]]

        project_dict[k[project_header[0]]] = k[project_header[1]]

    skills = row[header[3]]

    unique_skills.update(row.get(header[3]))

    if "Python" in skills:
        print(row[header[1]])

print("-----------------------\n")

for row in new_data:
    print(f"{row[header[1]]}-{total} hours")

print("-----------------------\n")

print(f"All Skills: {list(unique_skills)}")

print("-----------------------\n")

print(f"New Project Dict: {project_dict}")

with open("project_hours.json", "w") as updated_file:
    json.dump(project_dict, updated_file, indent=2)  


# Sample Output

# Aarav Nair-Software Engineer
# Diya Gupta-Data Engineer
# Sanjay Patil-QA Analyst

# --------------------

# Aarav Nair
# Diya Gupta
# -----------------------

# Aarav Nair-0 hours
# Diya Gupta-0 hours
# Sanjay Patil-0 hours
# -----------------------

# All Skills: ['SQL', 'Django', 'Spark', 'ETL', 'Postman', 'Python', 'Selenium']
# -----------------------

# New Project Dict: {'UST HealthCare Portal': 120, 'UST AI Chatbot': 85, 'UST Cloud Migration': 200}