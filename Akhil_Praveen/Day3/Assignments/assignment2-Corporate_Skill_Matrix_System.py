
skill_data = {
 "Arjun" : {"Python": "Advanced", "SQL": "Intermediate"},
"Neha" : {"Excel":"Expert", "PowerBI" :"Advanced","Word":"Intermediate"}
}

def add_skill():
    global skill_data
    name = input("Enter the employee name: ")
    if name not in skill_data:
        skill_data[name]={}
       
    skill = input("Enter the Skill: ")
    level = input("Enter the proficiency level: ")
    skill_data[name][skill]=level

def find_emp():
    skill = input("Enter the skill: ")
    f=0
    for i in skill_data:
        if skill in skill_data[i].keys():
            print(i)
            f=1
    if f==0:
        print("None")
def all_skill():
    uniq_skills=set()
    for i in skill_data:
        uniq_skills.update(set(skill_data[i].keys()))
    print(uniq_skills)
def emp_skill_3ormore():
    for i in skill_data:
        if len(skill_data[i])>=3:
            print(i)

def display():
    for i in skill_data:
        print(f"{i} -> {skill_data[i]}")
        print("")



print("=====   Corporate Skill Matrix System =====")
print("1. Add skill for an employee")
print("2. Find employee according to skill")
print("3. All skills across company")
print("4. Employee having 3 or more skills")
print("5. Display all")
print("6. Exit")

while True:
    choice = int(input("Enter your choice: "))
    if(choice==1):
        add_skill()
    elif(choice==2):
        find_emp()
    elif(choice==3):
        all_skill()
    elif(choice==4):
        emp_skill_3ormore()
    elif(choice==5):
        display()
    elif(choice==6):
        print("Thank you!")
        break
    else:
        print("Invalid choice please enter valid choice.")
    print("")

# =====   Corporate Skill Matrix System =====
# 1. Add skill for an employee
# 2. Find employee according to skill
# 3. All skills across company
# 4. Employee having 3 or more skills
# 5. Display all
# 6. Exit
# Enter your choice: 1
# Enter the employee name: Akhil
# Enter the Skill: Python
# Enter the proficiency level: Expert

# Enter your choice: 2 
# Enter the skill: Python
# Arjun
# Akhil

# Enter your choice: 3
# {'PowerBI', 'Python', 'SQL', 'Excel', 'Word'}

# Enter your choice: 4
# Neha

# Enter your choice: 5
# Arjun -> {'Python': 'Advanced', 'SQL': 'Intermediate'}

# Neha -> {'Excel': 'Expert', 'PowerBI': 'Advanced', 'Word': 'Intermediate'}

# Akhil -> {'Python': 'Expert'}


# Enter your choice: 6
# Thank you!
