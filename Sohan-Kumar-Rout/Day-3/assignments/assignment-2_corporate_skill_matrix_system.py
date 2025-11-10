#Assignment 2 — Corporate Skill Matrix System

#Code
skills_data = [
 ("E101", "Python", "Advanced"),
 ("E101", "SQL", "Intermediate"),
 ("E102", "Excel", "Expert"),
 ("E102", "PowerBI", "Advanced"),
 ("E103", "Python", "Beginner"),
 ("E103", "Excel", "Intermediate")
 ]
emp_skill= {}
skill_emp={}
#Finding duplicates element
for emp_id, skill , level in skills_data:
    if emp_id not in emp_skill:
        emp_skill[emp_id]={}
    if skill not in emp_skill[emp_id]:
        emp_skill[emp_id][skill]=level

        if skill not in skill_emp:
            skill_emp[skill]=[]
        if emp_id not in skill_emp[skill]:
            skill_emp[skill].append(emp_id)  
def get_skill(emp_id):
    return emp_skill.get(emp_id,{})
def get_by_skill(skill):
    return skill_emp.get(skill,[])
def get_unique_skill():
    return list(skill_emp.keys())
def employees_with_3_more_skills():
    res=[]
    for emp_id in emp_skill:
        if(len(emp_skill[emp_id])>=2):
            res.append(emp_id)
    return res
print("Employee with E101 ",get_skill("E101"))
print("Employee who knows Python : ",get_by_skill("Python"))
print("All unique skills across company : ",get_unique_skill())
print("Employees with more than one skills : ",employees_with_3_more_skills())

#Output
# Employee with E101  {'Python': 'Advanced', 'SQL': 'Intermediate'}
# Employee who knows Python :  ['E101', 'E103']
# All unique skills across company :  ['Python', 'SQL', 'Excel', 'PowerBI']
# Employees with more than one skills :  ['E101', 'E102', 'E103']

        

