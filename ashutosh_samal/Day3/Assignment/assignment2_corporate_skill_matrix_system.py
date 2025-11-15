#Assignment 2 — Corporate Skill Matrix System
# List of employee skills with their proficiency levels
skills_data = [
    ("E101", "Python", "Advanced"),
    ("E101", "SQL", "Intermediate"),
    ("E102", "Excel", "Expert"),
    ("E102", "PowerBI", "Advanced"),
    ("E103", "Python", "Beginner"),
    ("E103", "Excel", "Intermediate")
]

# Dictionary to store employee skills, where each employee is a key and the skills are stored as a set
employee_skills = {}

# Processing the skills data
for empid, skill, proficiency in skills_data:
    # If the employee is not in the dictionary, add them with an empty set for skills
    if empid not in employee_skills:
        employee_skills[empid] = set()
    
    # Add the skill to the employee's set (sets automatically handle duplicates)
    employee_skills[empid].add(skill)

# Printing the dictionary that shows which skills each employee has
print(employee_skills)

# Set to store employees with 3 or more skills
my_set = set()

# Iterating through the employee skills dictionary
for key, val in employee_skills.items():
    # If the employee has 3 or more unique skills, add them to my_set
    if len(val) >= 3:
        my_set.add(key)

# Printing the employees with 3 or more skills
print("Employees with 3 or more skills:", my_set)




# Sample Execution
# {'E101': {'SQL', 'Python'}, 'E102': {'PowerBI', 'Excel'}, 'E103': {'Excel', 'Python'}}
# Employees with 3 or more skills: set()

