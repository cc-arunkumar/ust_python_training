# Corporate Skill Matrix 

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
# Sample Input(understanding only):
# skills_data = [
#  ("E101", "Python", "Advanced"),
#  ("E101", "SQL", "Intermediate"),
#  ("E102", "Excel", "Expert"),
#  ("E102", "PowerBI", "Advanced"),
#  ("E103", "Python", "Beginner"),
#  ("E103", "Excel", "Intermediate")
# ]

# Your Task:
# Design and implement the right data structures so you can:
# 1. Quickly look up an employee’s skills.
# 2. Efficiently search which employees know a specific skill.
# 3. Generate a list of employees with 3+ unique skills.
# 4. Prevent duplicate skill entries for an employee.

# Sample skills data (employee_id, skill, level)
skills_data = [
    ("E101", "Python", "Advanced"),
    ("E101", "SQL", "Intermediate"),
    ("E102", "Excel", "Expert"),
    ("E102", "PowerBI", "Advanced"),
    ("E103", "Python", "Beginner"),
    ("E103", "Excel", "Intermediate")
]

# Dictionary to store employees and their skills
employees = {}

# Set to store all unique skills
all_skills = set()

# Step 1: Build employee skill matrix and collect unique skills
for e_id, skill, level in skills_data:
    if e_id not in employees:
        employees[e_id] = {}              # initialize employee record
    employees[e_id][skill] = level        # add skill with level
    all_skills.add(skill)                 # add skill to unique set

# Step 2: Find employees who know Python
python_emp = [e for e, skills in employees.items() if "Python" in skills]

# Step 3: Find employees with 3 or more skills
three_plus = [e for e, skills in employees.items() if len(skills) >= 3]

# Step 4: Print results
print("Employee Skill Matrix:")
for e, skills in employees.items():
    print(e, ":", skills)

print("\nAll unique skills:", all_skills)
print("Employees who know Python:", python_emp)
print("Employees with 3 or more skills:", three_plus)



# Employee Skill Matrix:
# E101 : {'Python': 'Advanced', 'SQL': 'Intermediate'}
# E102 : {'Excel': 'Expert', 'PowerBI': 'Advanced'}
# E103 : {'Python': 'Beginner', 'Excel': 'Intermediate'}

# All unique skills: {'Excel', 'SQL', 'PowerBI', 'Python'}
# Employees who know Python: ['E101', 'E103']
# Employees with 3 or more skills: []