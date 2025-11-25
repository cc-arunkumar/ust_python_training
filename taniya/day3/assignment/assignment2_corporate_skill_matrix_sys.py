# Sample skills data: (EmployeeID, Skill, Level)
skills_data = [
    ("E101", "Python", "Advanced"),
    ("E101", "SQL", "Intermediate"),
    ("E102", "Excel", "Expert"),
    ("E102", "PowerBI", "Advanced"),
    ("E103", "Python", "Beginner"),
    ("E103", "Excel", "Intermediate")
]

# Dictionary to store skills grouped by employee
employee_skills = {}

# Dictionary to store employees grouped by skill
skill_employee = {}

# Process each skill record
for emp_id, skills, level in skills_data:
    # Add skill to employee_skills dictionary
    if emp_id not in employee_skills:
        employee_skills[emp_id] = {}
    employee_skills[emp_id][skills] = level
    
    # Add employee to skill_employee dictionary
    if skills not in skill_employee:
        skill_employee[skills] = set()
    skill_employee[skills].add(emp_id)

# Print employee skills data
print("Employee skills data:")
for emp, skillss in employee_skills.items():
    print(emp, ":", skillss)

# Employees who know Python
python_emp = skill_employee.get("Python", set())
print("Employees who know python:", python_emp)

# All unique skills
unique_skills = set(skill_employee.keys())
print("All unique skills are:", unique_skills)

# Employees with 3 or more skills
more_three_skills = [emp for emp, skills in employee_skills.items() if len(skills) >= 3]
print("Employee with 3 or more skills:", more_three_skills)

# -------------------------
# Expected Output:
# Employee skills data:
# E101 : {'Python': 'Advanced', 'SQL': 'Intermediate'}
# E102 : {'Excel': 'Expert', 'PowerBI': 'Advanced'}
# E103 : {'Python': 'Beginner', 'Excel': 'Intermediate'}
# Employees who know python: {'E101', 'E103'}
# All unique skills are: {'Python', 'SQL', 'Excel', 'PowerBI'}
# Employee with 3 or more skills: []