import json

# -------------------------------
# Load employee data from JSON file
# -------------------------------
with open(r"C:\Users\Administrator\Desktop\Training\ust_python_training\taniya\day13\data.json") as file1:
    data = json.load(file1)             # Load JSON data
    my_emp = data["employees"]          # Extract list of employees

# -------------------------------
# Initialize containers
# -------------------------------
all_skills = []                         # Collect all unique skills
python_emp = []                         # Collect employees who know Python
project_hours = {}                      # Track total hours per project

# -------------------------------
# Process each employee
# -------------------------------
for emp in my_emp:
    # Display employee name and role
    print(f"Employee name is {emp.get('name')} and their role is {emp.get('role')}")

    # Calculate total hours spent across all projects for this employee
    total_hours = sum(project["hours_logged"] for project in emp["projects"])
    print(f"{emp.get('name')}: {total_hours} hours\n")

    # Collect unique skills
    for skill in emp["skills"]:
        if skill not in all_skills:
            all_skills.append(skill)

    # Identify employees who know Python
    if "Python" in emp["skills"]:
        python_emp.append(emp.get("name"))

    # Aggregate project hours across all employees
    for project in emp["projects"]:
        name = project["name"]
        hours = project["hours_logged"]
        if name in project_hours:
            project_hours[name] += hours
        else:
            project_hours[name] = hours

# -------------------------------
# Final results
# -------------------------------
# Sort skills alphabetically
all_skills.sort()
print(f"All Skills: {all_skills}\n")

# Print employees who know Python
print("Employees who knows python")
for name in python_emp:
    print(name)

# Print project-wise total hours
print("\nProject-wise total hours:")
for project, hours in project_hours.items():
    print(f"{project}: {hours}")

# -------------------------------
# Save project hours summary to JSON file
# -------------------------------
with open("project_hours.json", "w") as file:
    json.dump(project_hours, file, indent=4)