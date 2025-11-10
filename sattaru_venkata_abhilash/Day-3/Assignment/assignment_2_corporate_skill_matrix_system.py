# Assignment 2 — Corporate Skill Matrix System
# Scenario:
# UST’s L&D team wants to maintain a skill matrix for all employees.
# Each employee can have multiple skills with proficiency levels.
# Requirements:
# 1. Store skill data efficiently and prevent duplicates.
# 2. Retrieve employees by specific skill.
# 3. Get all unique skills across the company.
# 4. Find employees with 3 or more skills.
# 5. Add or update skills dynamically.

skills_data = [
    ("E101", "Python", "Advanced"),
    ("E101", "SQL", "Intermediate"),
    ("E102", "Excel", "Expert"),
    ("E102", "PowerBI", "Advanced"),
    ("E103", "Python", "Beginner"),
    ("E103", "Excel", "Intermediate")
]

# Store employee skills (avoid duplicates)
employee_skills = {}
for emp, skill, level in skills_data:
    employee_skills.setdefault(emp, {})[skill] = level

# Find employees who know a given skill
def find_employees_with_skill(skill):
    return [emp for emp, skills in employee_skills.items() if skill in skills]

# Get all unique skills
unique_skills = {s for skills in employee_skills.values() for s in skills}

# Employees with 3 or more skills
multi_skilled = [emp for emp, skills in employee_skills.items() if len(skills) >= 3]

# Add or update new skill dynamically
def add_or_update(emp, skill, level):
    employee_skills.setdefault(emp, {})[skill] = level

# Example update
add_or_update("E101", "Excel", "Intermediate")

# Print results
print("Employee Skills:", employee_skills)
print("Employees who know Python:", find_employees_with_skill("Python"))
print("All unique skills:", unique_skills)
print("Employees with 3+ skills:", multi_skilled)


# Sample Output:
# Employee Skills: {'E101': {'Python': 'Advanced', 'SQL': 'Intermediate', 'Excel': 'Intermediate'},
#                   'E102': {'Excel': 'Expert', 'PowerBI': 'Advanced'},
#                   'E103': {'Python': 'Beginner', 'Excel': 'Intermediate'}}
# Employees who know Python: ['E101', 'E103']
# All unique skills: {'Excel', 'SQL', 'PowerBI', 'Python'}
# Employees with 3+ skills: []
