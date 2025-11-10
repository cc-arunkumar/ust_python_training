# Part 5: Function with variable arguments ( args )
# Objective:
# After collecting data from multiple employees, HR wants to know the average
# efficiency score of the entire team.


def efficiency_score_of_team(team_members,total_team_efficiency):
    avg_eff=total_team_efficiency/team_members
    print(f"Average Team Efficiency : {avg_eff:.1f}")

    if avg_eff>25:
        print("Excellent team performance")
    elif avg_eff>15:
        print("Good Team performance")
    else : print("Team needs Improvement")
    
def calculate_efficiney_score(tasks_completed,hrs_worked):
    Efficiency=(tasks_completed/hrs_worked)*10
    return Efficiency

def calculate_efficiency(emp_name,dep_name,eff_score):
    print(f"Employee: {emp_name} | Department: {dep_name} | Efficiency: {eff_score:.1f}")
    if eff_score>25:
        print("Excellent Performance")
    elif eff_score>15:
        print("Good Peformance")
    else : print("Needs Improvement")

print("Welcome to UST Employee Work Report System")
print("This program helps HR calculate employee performance easily.")
print("Current Active Project: UST Cloud Migration")

team_members=0;total_team_efficiency=0

while True:
    
    name=input("Enter Your Name : ")
    team_members+=1
    department=input("Enter your Department Name : ")
    tasks_completed=int(input("Enter Taks Completed : "))
    hrs_worked=int(input("Total Hours Worked : "))
    efficiency=calculate_efficiney_score(tasks_completed,hrs_worked)
    total_team_efficiency+=efficiency
    calculate_efficiency(name,department,efficiency)

    choice=int(input("Press 1 to See Team Performance or Press 0 to Continue"))
    if choice==1:
        print("Thanks for Comming..!")
        break


efficiency_score_of_team(team_members,total_team_efficiency)

# sample output

# Welcome to UST Employee Work Report System
# This program helps HR calculate employee performance easily.
# Current Active Project: UST Cloud Migration
# Enter Your Name : madhan
# Enter your Department Name : IT
# Enter Taks Completed : 25
# Total Hours Worked : 9
# Employee: madhan | Department: IT | Efficiency: 27.8
# Excellent Performance
# Press 1 to See Team Performance or Press 0 to Continue1
# Thanks for Comming..!
# Average Team Efficiency : 27.8
# Excellent team performance
    

