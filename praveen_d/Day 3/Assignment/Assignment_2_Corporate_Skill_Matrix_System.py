# Assignment 2 — Corporate Skill Matrix System


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