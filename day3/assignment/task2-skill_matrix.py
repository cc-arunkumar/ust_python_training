# Corporate Skill Matrix 
skills_data = [
 ("E101", "Python", "Advanced"),
 ("E101", "SQL", "Intermediate"),
 ("E102", "Excel", "Expert"),
 ("E102", "PowerBI", "Advanced"),
 ("E103", "Python", "Beginner"),
 ("E103", "Excel", "Intermediate")
]

# 1. Quickly look up an employee’s skills.

employees = {}
all_skills = set()

for emp_id, emp_skill, level in skills_data:
    if emp_id not in employees:
        employees[emp_id] = {}
    employees[emp_id][emp_skill] = level
    all_skills.add(emp_skill)

for e, skills in employees.items():
    print(e, ":", skills)
print("All unique skills:", all_skills)
# 2. Efficiently search which employees know a specific skill.
search_emp = [e for e, skills in employees.items() if "PowerBI" in skills]
print("Employees who know PowerBI:", search_emp)
# 3. Generate a list of employees with 3+ unique skills.
three_plus = [e for e, skills in employees.items() if len(skills) >= 3]
print("Employees with 3 or more skills:", three_plus)
# 4. Prevent duplicate skill entries for an employee.



# output
# E101 : {'Python': 'Advanced', 'SQL': 'Intermediate'}
# E102 : {'Excel': 'Expert', 'PowerBI': 'Advanced'}
# E103 : {'Python': 'Beginner', 'Excel': 'Intermediate'}
# All unique skills: {'PowerBI', 'Excel', 'Python', 'SQL'}
# Employees who know PowerBI: ['E102']
# Employees with 3 or more skills: []
