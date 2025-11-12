# Assignment 2 — Corporate Skill Matrix Syste

# They want to:
# 1. Store skill information efficiently.
# 2. Ensure no duplicate skill names for the same employee.
# 3. Retrieve:
#   All employees who know a given skill (e.g., “Python”).
#   All unique skills across the company.
#   Employees having 3 or more skills.
# 4. Be able to add or update new skills dynamically.



# Step 1: Initialize the skills dataset
skills_data = [
    ("E101", "Python", "Advanced"),
    ("E101", "SQL", "Intermediate"),
    ("E102", "Excel", "Expert"),
    ("E102", "PowerBI", "Advanced"),
    ("E103", "Python", "Beginner"),
    ("E103", "Excel", "Intermediate")
]

# Step 2: Initialize data structures
employee_skills = {}         # Maps employee ID to their skill-level dictionary
skill_to_employees = {}      # Maps skill name to set of employee IDs
unique_skills = set()        # Tracks all unique skills

# Step 3: Populate employee skill matrix and skill-to-employee mapping
for emp_id, skill, level in skills_data:
    if emp_id not in employee_skills:
        employee_skills[emp_id] = {}
    
    if skill not in employee_skills[emp_id]:
        employee_skills[emp_id][skill] = level
        unique_skills.add(skill)
        
        if skill not in skill_to_employees:
            skill_to_employees[skill] = set()
        skill_to_employees[skill].add(emp_id)

# Step 4: Define function to get employees by skill
def get_employees_with_a_skill(skill_name):
    return skill_to_employees.get(skill_name, set())

# Step 5: Define function to add or update a skill for an employee
def add_or_update_skill(emp_id, skill, level):
    if emp_id not in employee_skills:
        employee_skills[emp_id] = {}
    
    is_new_skill = skill not in employee_skills[emp_id]
    employee_skills[emp_id][skill] = level
    
    if is_new_skill:
        unique_skills.add(skill)
        if skill not in skill_to_employees:
            skill_to_employees[skill] = set()
        skill_to_employees[skill].add(emp_id)

# Step 6: Update skill data
add_or_update_skill("E103", "PowerBI", "Intermediate")  # New skill for E103
add_or_update_skill("E101", "Python", "Expert")         # Update skill level for E101

# Step 7: Display employee skill matrix
print("Employee Skill Matrix:")
for emp_id, skills in employee_skills.items():
    print(f"{emp_id}: {skills}")

# Step 8: Display employees who know Python
print("\nEmployees who know Python:")
print(get_employees_with_a_skill("Python"))

# Step 9: Identify employees with 3 or more skills
employees_with_3plus_skills = [emp_id for emp_id, skills in employee_skills.items() if len(skills) >= 3]
print("\nEmployees with 3 or more skills:")
print(employees_with_3plus_skills)

# Step 10: Display all unique skills
print("\nAll unique skills across the company:")
print(unique_skills)


# ========Sample output============
# Employee Skill Matrix:
# E101: {'Python': 'Expert', 'SQL': 'Intermediate'}
# E102: {'Excel': 'Expert', 'PowerBI': 'Advanced'}
# E103: {'Python': 'Beginner', 'Excel': 'Intermediate', 'PowerBI': 'Intermediate'}

# Employees who know Python:
# {'E103', 'E101'}

# Employees with 3 or more skills:
# ['E103']

# All unique skills across the company:
# {'Excel', 'SQL', 'Python', 'PowerBI'}