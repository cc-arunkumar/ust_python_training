import json   # Import JSON module

# Create a set to store unique skills (no duplicates)
unique_skills = set()

# Dictionary to store project hours
dict = {}

# Open and load employee data from JSON file
with open(r'C:\Users\Administrator\Desktop\ust_python_training\Rohit\day13\tasks\data.json', mode="r", encoding="utf-8") as file:
    data = json.load(file)          # Load JSON data into Python dict
    employees = data['employees']   # Extract list of employees
    
    # Iterate through each employee
    for emp in employees:
        print(f"Employee Name: {emp['name']} , employee Role : {emp['role']}")
        
        # Calculate total hours logged across all projects
        projects = emp["projects"]
        val = 0
        for project in projects:
            try:
                val += int(project['hours_logged'])   # Add hours if numeric
            except:
                print(f"Hours logged data is not available for project: {project['name']}")
        
        print(f"Total hours logged by {emp['name']}: {val} hours")
        
        # Collect skills and check for Python
        for skill in emp['skills']:
            if skill == "Python":
                print(f"{emp['name']} has Python skill")
            unique_skills.add(skill)   # Add skill to set (avoids duplicates)
        
        # Collect project hours into dictionary
        if emp.get("projects"):
            for project in emp['projects']:
                dict[project['name']] = project['hours_logged']

# Print dictionary of project hours
print(dict)

# Save project hours dictionary into a new JSON file
with open(r'C:\Users\Administrator\Desktop\ust_python_training\Rohit\day13\tasks\project_hours.json', mode="w", encoding="utf-8") as outfile:
    json.dump(dict, outfile, indent=3)
