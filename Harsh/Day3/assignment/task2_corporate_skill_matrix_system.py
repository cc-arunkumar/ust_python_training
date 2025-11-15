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
# Employees having 3 or more skills.
# 4. Be able to add or update new skills dynamically.
# Your Task:
# Design and implement the right data structures so you can:
# 1. Quickly look up an employee’s skills.
# 2. Efficiently search which employees know a specific skill.
# 3. Generate a list of employees with 3+ unique skills.
# 4. Prevent duplicate skill entries for an employee.

# Initialize employee skills data

skills_data = [
    ("E101", "Python", "Advanced"),
    ("E101", "SQL", "Intermediate"),
    ("E102", "Excel", "Expert"),
    ("E102", "PowerBI", "Advanced"),
    ("E103", "Python", "Beginner"),
    ("E103", "Excel", "Intermediate")
]

employee_skills = {}

# Traverse the employee skills dictionary
for eid, skill, level in skills_data:
    
    # Build the employee skills dictionary
    if eid not in employee_skills:
        employee_skills[eid] = {}
    employee_skills[eid][skill] = level

# Identify all unique skills across employees
unique_skills = set()
for skills in employee_skills.values():
    for s in skills:
        unique_skills.add(s)

# Search for employees with a specific skill
search_skill = input("Enter skill to search: ")
knows_skill = []
for eid, skills in employee_skills.items():
    if search_skill in skills:
        knows_skill.append(eid)

# Function to add or update an employee's skill
def add_or_update_skill(eid, skill, level):
    if eid not in employee_skills:
        employee_skills[eid] = {}
    employee_skills[eid][skill] = level
    print(eid, "skill added:", skill, "-", level)

add_or_update_skill("E103", "PowerBI", "Advanced")

# Identify employees with 3 or more skills
multi_skill_emp = []
for eid, skills in employee_skills.items():
    if len(skills) >= 3:
        multi_skill_emp.append(eid)

print("\nEmployee Skill Matrix:")
for eid, skills in employee_skills.items():
    print(eid, ":", skills)

print("\nEmployees who know", search_skill, ":", knows_skill)
print("\nEmployees with 3 or more skills:", multi_skill_emp)
print("\nAll Unique Skills:", unique_skills)

# Enter skill to search: Python
# E103 skill added: PowerBI - Advanced

# Employee Skill Matrix:
# E101 : {'Python': 'Advanced', 'SQL': 'Intermediate'}
# E102 : {'Excel': 'Expert', 'PowerBI': 'Advanced'}
# E103 : {'Python': 'Beginner', 'Excel': 'Intermediate', 'PowerBI': 'Advanced'}

# Employees who know Python : ['E101', 'E103']

# Employees with 3 or more skills: ['E103']