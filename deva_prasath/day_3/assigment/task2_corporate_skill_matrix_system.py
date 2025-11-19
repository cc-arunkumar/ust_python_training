# Corporate Skill Matrix System

# UST’s L&D team wants to maintain a skill matrix for all employees.
# Every employee can have multiple skills at different proficiency levels.
# Sample data representing employee skills
skills_data = [
    ("E101", "Python", "Advanced"),
    ("E101", "SQL", "Intermediate"),
    ("E102", "Excel", "Expert"),
    ("E102", "PowerBI", "Advanced"),
    ("E103", "Python", "Beginner"),
    ("E103", "Excel", "Intermediate")
]

# Initialize dictionaries to store employee skills and skill-to-employee mapping
employee_skills = {}      # Maps employee ID to a dictionary of their skills
skill_to_employees = {}   # Maps skill to a set of employees who know that skill
unique_skills = set()     # Set of all unique skills in the company

# Process each skill entry in the skills data
for emp_id, skill, level in skills_data:
    
    # Add skill to employee's skills dictionary
    if emp_id not in employee_skills:
        employee_skills[emp_id] = {}
    employee_skills[emp_id][skill] = level

    # Add employee to the skill-to-employees mapping
    if skill not in skill_to_employees:
        skill_to_employees[skill] = set()
    skill_to_employees[skill].add(emp_id)

    # Add the skill to the unique skills set
    unique_skills.add(skill)

# Function to update or add skills for an employee
def update_skill(emp_id, skill, level):
    # Add skill to employee's skills dictionary
    if emp_id not in employee_skills:
        employee_skills[emp_id] = {}
    employee_skills[emp_id][skill] = level
    
    # Add employee to the skill-to-employees mapping
    if skill not in skill_to_employees:
        skill_to_employees[skill] = set()
    skill_to_employees[skill].add(emp_id)

    # Add the skill to the unique skills set
    unique_skills.add(skill)

# Update skills for specific employees
update_skill("E101", "PowerBI", "Intermediate")
update_skill("E103", "Python", "Intermediate")

# Query to find employees who know a specific skill
query_skill = "Python"
print("\nEmployees who know", query_skill, ":")
if query_skill in skill_to_employees:
    for emp in skill_to_employees[query_skill]:
        print(" -", emp)
else:
    print(" None")

# Print all unique skills in the company, sorted alphabetically
print("Unique skills in the company:")
for skill in sorted(unique_skills):
    print(" -", skill)

# Print employees who have 3 or more skills
print("Employees with 3 or more skills:")
found = False
for emp, skills in employee_skills.items():
    if len(skills) >= 3:
        print(" -", emp)
        found = True
if not found:
    print(" None")

# Print all employee skills
print("Employee Skills:")
for emp, skills in employee_skills.items():
    print(" -", emp)
    for skill_name, level in skills.items():
        print(skill_name, level)

#Sample output

# Employees who know Python :
#  - E101
#  - E103
# Unique skills in the company:
#  - Excel
#  - PowerBI
#  - Python
#  - SQL
# Employees with 3 or more skills:
#  - E101
# Employee Skills:
#  - E101
# Python Advanced
# SQL Intermediate
# PowerBI Intermediate
#  - E102
# Excel Expert
# PowerBI Advanced
#  - E103
# Python Intermediate
# Excel Intermediate
