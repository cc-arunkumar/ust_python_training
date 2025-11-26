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

skills_data = [
 ("E101", "Python", "Advanced"),
 ("E101", "SQL", "Intermediate"),
 ("E102", "Excel", "Expert"),
 ("E102", "PowerBI", "Advanced"),
 ("E103", "Python", "Beginner"),
 ("E103", "Excel", "Intermediate"),
 ("E103","Java","Advance")
]

emp_skills=set()
unique_item_of_emp={}
unique_emp_list={}

for emp_id,emp_skill,level in skills_data:
    emp_skills.add((emp_id,emp_skill))

    if (emp_id,emp_skill) not in unique_item_of_emp:
        unique_item_of_emp[emp_id]=unique_item_of_emp.get(emp_id,0)+1

    if emp_id not in unique_emp_list:
        unique_emp_list[emp_id]={}
    if emp_skill not in unique_emp_list:
        unique_emp_list[emp_id][emp_skill]=level
        

for key, value in unique_item_of_emp.items():
    if value>=3:
        print(f"Employee with more or 3 skills:{key}")


print(emp_skills)
print(unique_item_of_emp)

# EXPECTED OUTPUT:
# Employee with more or 3 skills:E103
# {('E102', 'Excel'), ('E102', 'PowerBI'), ('E101', 'Python'), ('E103', 'Java'), ('E103', 'Excel'), ('E101', 'SQL'), ('E103', 'Python')}
# {'E101': 2, 'E102': 2, 'E103': 3}