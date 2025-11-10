#Assignment 2 — Corporate Skill Matrix System
skills_data = {
 "E101": (("Python", "Advanced"),("SQL", "Intermediate")),
 "E102": (("Excel", "Expert"),("PowerBI", "Advanced")),
 "E103": (("Python", "Beginner"),("Excel", "Intermediate")),
}
levels={
    1:"Expert",
    2:"Advanced",
    3:"Intermediate",
    4:"Beginner"   
}
ch='Y'
while(ch=='Y' or ch=='y'):
    print("====== Employee Skill System ======")
    print("1. Add/Update Employee Skill")
    print("2. Find EMP Skill")
    print("3. Display EMP with more than 3 unique skills")
    print("4. Exit")
    n=int(input("Choose choice:"))
    if(n==1):
        emp_id = input("Enter EMP ID: ")
        num = int(input("Enter the no:skills: "))
        L=[]
        for i in range(num):
            skill=input(f"Enter Skill {i+1}: ")
            level=int(input(f"Choose level 1.Expert 2.Advanced 3.Intermediate 4.Beginner :"))
            L.append((skill,levels[level]))
        skills_data[emp_id]=tuple(L)
        print("Successfully Updated")
    elif(n==2):
        emp_id = input("Enter the EMP ID to check : ")
        print(f"Skills for {emp_id} is {skills_data[emp_id]}")
    elif(n==3):
        f=0
        for i in skills_data:
            if(len(skills_data.get(i))>3):
                f=1
                print(f"EMP {i} has {skills_data.get(i)} unique skills")    
        if(f==0):
            print("No employees") 
    elif(n==4):
        print("Thank you! Have a great day.")
        break
    else:
        print("Provide a number within range!!")
    ch=input("\nDo you wish to continue(Y/N)")
#Output
# ====== Employee Skill System ======
# 1. Add/Update Employee Skill
# 2. Find EMP Skill
# 3. Display EMP with more than 3 unique skills
# 4. Exit
# Choose choice:1
# Enter EMP ID: E104
# Enter the no:skills: 4
# Enter Skill 1: Python
# Choose level 1.Expert 2.Advanced 3.Intermediate 4.Beginner :1
# Enter Skill 2: Java
# Choose level 1.Expert 2.Advanced 3.Intermediate 4.Beginner :2
# Enter Skill 3: PHP
# Choose level 1.Expert 2.Advanced 3.Intermediate 4.Beginner :4
# Enter Skill 4: HTML
# Choose level 1.Expert 2.Advanced 3.Intermediate 4.Beginner :2
# Successfully Updated

# Do you wish to continue(Y/N)y
# ====== Employee Skill System ======
# 1. Add/Update Employee Skill
# 2. Find EMP Skill
# 3. Display EMP with more than 3 unique skills
# 4. Exit
# Choose choice:2
# Enter the EMP ID to check : E101
# Skills for E101 is (('Python', 'Advanced'), ('SQL', 'Intermediate'))

# Do you wish to continue(Y/N)y
# ====== Employee Skill System ======
# 1. Add/Update Employee Skill
# 2. Find EMP Skill
# 3. Display EMP with more than 3 unique skills
# 4. Exit
# Choose choice:3
# EMP E104 has (('Python', 'Expert'), ('Java', 'Advanced'), ('PHP', 'Beginner'), ('HTML', 'Advanced')) unique skills

# Do you wish to continue(Y/N)y
# ====== Employee Skill System ======
# 1. Add/Update Employee Skill
# 2. Find EMP Skill
# 3. Display EMP with more than 3 unique skills
# 4. Exit
# Choose choice:4
# Thank you! Have a great day.