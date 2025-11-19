import json

# 1. Load JSON file
with open("data.json", "r") as employee_file:
    json_reader = json.load(employee_file)

# Extract employee list
new_data = json_reader['employees']

# Extract headers dynamically
header = list(new_data[0].keys())

unique_skills = set()          # To store all unique skills
project_dict = {}             # To store project name → total hours

print("\n===== EMPLOYEE NAME — ROLE =====")
for row in new_data:

    # 2. Print employee name and role
    print(f"{row[header[1]]} — {row[header[2]]}")

    project_data = row['projects']
    total = 0

    # 3. Calculate total hours for each employee
    for k in project_data:
        project_header = list(k.keys())

        total += k[project_header[1]]

    print(f"Total Hours by {row[header[1]]}: {total} hours\n")

    # Add project hours to project_dict
    for k in project_data:
        project_header = list(k.keys())

        if k[project_header[0]] in project_dict:
            project_dict[k[project_header[0]]] += k[project_header[1]]
        else:
            project_dict[k[project_header[0]]] = k[project_header[1]]

    # 5. Detect employees who know Python
    skills = row[header[3]]
    if "Python" in skills:
        print(f" Python Developer: {row[header[1]]}")

    # 4. Update unique skill list
    unique_skills.update(row.get(header[3]))

print("\n===== UNIQUE SKILLS (SORTED) =====")
print(sorted(unique_skills))

print("\n===== PROJECT HOURS (ALL EMPLOYEES) =====")
print(project_dict)

# 7. Save project hours to a new JSON file
with open("project_hours.json", "w") as updated_file:
    write = json.dump(project_dict, updated_file, indent=2)

print("\n File 'project_hours.json' created successfully!")



# sample output:
# ===== EMPLOYEE NAME — ROLE =====
# Aarav Nair — Software Engineer
# Total Hours by Aarav Nair: 205 hours
# ✔ Python Developer: Aarav Nair

# Diya Gupta — Data Engineer
# Total Hours by Diya Gupta: 200 hours
# ✔ Python Developer: Diya Gupta

# ===== UNIQUE SKILLS (SORTED) =====
# ['Django', 'ETL', 'Postman', 'Python', 'SQL', 'Selenium', 'Spark']

# ===== PROJECT HOURS (ALL EMPLOYEES) =====
# {'UST HealthCare Portal': 120, 'UST AI Chatbot': 85, 'UST Cloud Migration': 200}

# File 'project_hours.json' created successfully!

