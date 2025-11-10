#Assignment 2 — Corporate Skill Matrix System
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

# Your Task:
# Design and implement the right data structures so you can:
# 1. Quickly look up an employee’s skills.
# 2. Efficiently search which employees know a specific skill.
# 3. Generate a list of employees with 3+ unique skills.
# 4. Prevent duplicate skill entries for an employee.

skills_data = [
 ("E101", "Python", "Advanced"),
 ("E101", "SQL", "Intermediate"),
 ("E102", "Excel", "Expert"),
 ("E102", "PowerBI", "Advanced"),
 ("E103", "Python", "Beginner"),
 ("E103", "Excel", "Intermediate")
]

skills_set = {}
for emp in skills_data:
    if emp[1] not in skills_set:
        skills_set[emp[1]]= set()
        skills_set[emp[1]].add(emp[0])
    else:
        skills_set[emp[1]].add(emp[0])
print("Skills Set:",skills_set)

emp_set ={}
for emp in skills_data:
    if emp[0] not in emp_set:
        emp_set[emp[0]]=set()
        emp_set[emp[0]].add(emp[1])
    else:
        emp_set[emp[0]].add(emp[1])
print("Employees Set:",emp_set)
print("List of Employees with 2+ skills:")
for it in emp_set.items():
    if len(it[1])>=2:
        print(it[0])
        
#Sample Output
# Skills Set: {'Python': {'E101', 'E103'}, 'SQL': {'E101'}, 'Excel': {'E103', 'E102'}, 'PowerBI': {'E102'}}
# Employees Set: {'E101': {'Python', 'SQL'}, 'E102': {'PowerBI', 'Excel'}, 'E103': {'Python', 'Excel'}}
# List of Employees with 2+ skills:
# E101
# E102
# E103
