import json

# Load employee data from a JSON file
with open("ashutosh_samal\Day13\json_task1\data.json", "r") as data:
    employee = json.load(data)

employees = employee["employees"]
skills = set()
names = []
project_hrs = {}

# 1. Print employee name and role
for emp in employees:
    print(f"{emp['name']}-----{emp['role']}")  # Fixing string quotes

# 2. Calculate total hours worked by each employee across projects
for emp in employees:
    total_hours = 0
    for i in emp.get("projects", []):  # Using .get() to avoid KeyError
        total_hours += i.get("hours_logged", 0)  # Default to 0 if hours_logged is missing
    print(f"{emp['name']}:{total_hours}")

# 3. Collect all unique skills and people who know Python
for emp in employees:
    for i in emp.get("skills", []):  # Using .get() to avoid KeyError
        skills.add(i)
        if i == "Python":
            names.append(emp.get("name"))

# 4. Calculate project hours summary
for emp in employees:
    summary = 0
    for d in emp.get("projects", []):  # Using .get() to avoid KeyError
        summary += d.get("hours_logged", 0)
        # Accumulate project hours (fixing overwriting issue)
        project_hrs[d["name"]] = project_hrs.get(d["name"], 0) + d.get("hours_logged", 0)

# Convert skills set to a list for easier printing
skills = list(skills)

# Print results
print("All Skills:", skills)
print("People who only know Python:", names)
print(project_hrs)

# Save project hours to a new JSON file
with open("project_hours.json", "w") as file:
    file.write(json.dumps(project_hrs, indent=2))
