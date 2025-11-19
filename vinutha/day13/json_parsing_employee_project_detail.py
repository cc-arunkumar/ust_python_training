import json

# load json
with open("data.json", "r") as new_file:
    reader = json.load(new_file)

data = reader["employees"]

total_hours = []
skills = []
project = {}
# display name and role
for row in data:
    print(f"{row['name']} - {row['role']}")

    hour = 0
    for prj in row["projects"]:
        hour += prj["hours_logged"]
        project[prj["name"]] = project.get(prj["name"], 0) + prj["hours_logged"]

    total_hours.append({"name": row["name"], "hours_logged": hour})

    for s in row["skills"]:
        if s not in skills:
            skills.append(s)
        if s == "Python":
            print(row["name"])

with open("project_hours.json", "w") as file:
    json.dump(project, file, indent=2)
