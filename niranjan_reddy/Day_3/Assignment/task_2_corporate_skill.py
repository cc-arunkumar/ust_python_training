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


skills_data = [
 ("E101", "Python", "Advanced"),
 ("E101", "SQL", "Intermediate"),
 ("E102", "Excel", "Expert"),
 ("E102", "PowerBI", "Advanced"),
 ("E103", "Python", "Beginner"),
 ("E103", "Excel", "Intermediate")
]

employee_skills={}

for employee_id,skill,level in skills_data:
    employee_skills.setdefault(employee_id,{})[skill]=level

print("Employee's Skills: ", employee_skills)

for key,val in employee_skills.items():
    print(f"{key}-> {employee_skills.get(key,0)}")

name="Python"

for key,val in employee_skills.items():
    if name in val:
        print(f"{name}->{key}")

for key,val in employee_skills.items():
    if len(val)>=3:
        print(key)


# Sample Output

# Employee's Skills:  {'E101': {'Python': 'Advanced', 'SQL': 'Intermediate'}, 
# 'E102': {'Excel': 'Expert', 'PowerBI': 'Advanced'}, 
# 'E103': {'Python': 'Beginner', 'Excel': 'Intermediate'}}


# E101-> {'Python': 'Advanced', 'SQL': 'Intermediate'}
# E102-> {'Excel': 'Expert', 'PowerBI': 'Advanced'}
# E103-> {'Python': 'Beginner', 'Excel': 'Intermediate'}


# Python->E101
# Python->E103