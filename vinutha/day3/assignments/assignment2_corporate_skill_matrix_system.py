# Assignment 2 — Corporate Skill Matrix System
# Scenario:
# UST’s L&D team wants to maintain a skill matrix for all employees.
# Every employee can have multiple skills at different proficiency levels.
# For example:
# Arjun → Python (Advanced), SQL (Intermediate)
# Neha → Excel (Expert), PowerBI (Advanced)
# They want to:
# 1. Store skill information efficiently.
# 2. Ensure no duplicate skill names for the same employee.
# 3. Retrieve:
# All employees who know a given skill (e.g., “Python”).
# All unique skills across the company.
# Assignment 2
# Employees having 3 or more skills.
# 4. Be able to add or update new skills dynamically.

#Code

# Initial dataset: each tuple contains (Employee ID, Skill, Skill Level)
data = [
    ("E101", "Python", "Advanced"),
    ("E101", "SQL", "Intermediate"),
    ("E102", "Excel", "Expert"),
    ("E102", "PowerBI", "Advanced"),
    ("E103", "Python", "Beginner"),
    ("E103", "Excel", "Intermediate")
]

# Dictionary to store skills grouped by employee
employee_skills = {}
for emp_id, skills, level in data:
    # If employee not in dictionary, initialize with empty dict
    if emp_id not in employee_skills:
        employee_skills[emp_id] = {}
    # Add skill and its level for the employee
    employee_skills[emp_id][skills] = level

# Dictionary to store employees grouped by skill
skill_employees = {}
for emp_id, skill_dict in employee_skills.items():
    for skills in skill_dict:
        # If skill not in dictionary, initialize with empty list
        if skills not in skill_employees:
            skill_employees[skills] = []
        # Add employee to the skill list
        skill_employees[skills].append(emp_id)

# Set to store all unique skills
unique = set()
for skill_dict in employee_skills.values():
    for skills in skill_dict:
        unique.add(skills)

# Find employees who have 3 or more skills
three_skills = []
for emp_id, skill_dict in employee_skills.items():
    if len(skill_dict) >= 3:
        three_skills.append(emp_id)

# Print results
print("Employees by skill:", skill_employees)
print("Unique skills:", unique)
print("Employees with 3 or more skills:", three_skills)

# Add a new skill record for employee E202
new_skill = ("E202", "Python", "Intermediate")
emp_id, skills, level = new_skill

# Update employee_skills dictionary
if emp_id not in employee_skills:
    employee_skills[emp_id] = {}
employee_skills[emp_id][skills] = level

# Update skill_employees dictionary
if skills not in skill_employees:
    skill_employees[skills] = []
if emp_id not in skill_employees[skills]:
    skill_employees[skills].append(emp_id)

# Recalculate unique skills after update
unique = set()
for skill_dict in employee_skills.values():
    for skills in skill_dict:
        unique.add(skills)

# Print updated results
print("\nAfter adding/updating new skill:")
print("Employees by skill:", skill_employees)
print("Unique skills:", unique)

#output
# PS C:\Users\303379\day3_training> & C:/Users/303379/AppData/Local/Microsoft/WindowsApps/python3.13.exe c:/Users/303379/day3_training/Assignment2_Corporate_SkillMatrix_System.py
# Employees by skill: {'Python': ['E101', 'E103'], 'SQL': ['E101'], 'Excel': ['E102', 'E103'], 'PowerBI': ['E102']}
# Unique skills: {'Python', 'Excel', 'SQL', 'PowerBI'}
# Employees with 3 or more skills: []

# After adding/updating new skill:
# Employees by skill: {'Python': ['E101', 'E103', 'E202'], 'SQL': ['E101'], 'Excel': ['E102', 'E103'], 'PowerBI': ['E102']}
# Unique skills: {'Python', 'Excel', 'SQL', 'PowerBI'}
# PS C:\Users\303379\day3_training> 