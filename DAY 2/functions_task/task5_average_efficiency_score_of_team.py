"""
Objective:
After collecting data from multiple employees, HR wants to know the average efficiency score of the entire team.

Requirements:
Create a function that accepts any number of efficiency scores.
It should calculate and print the average of all the scores.
Based on the average:
If average > 25 → “Team performed above expectations.”
Otherwise → “Team needs improvement.”
The function should only print the result and not return anything.


"""


def efficiency_score_of_team(team_members,total_team_efficiency):   # Function to calculate team average efficiency
    avg_eff=total_team_efficiency/team_members   # Calculate average efficiency
    print(f"Average Team Efficiency : {avg_eff:.1f}")   # Print average with 1 decimal

    if avg_eff>25:   # Check if average >25
        print("Excellent team performance")   # Print excellent team performance
    elif avg_eff>15:   # Check if average between 15 and 25
        print("Good Team performance")   # Print good team performance
    else : print("Team needs Improvement")   # Print team needs improvement if below 15
    
def calculate_efficiney_score(tasks_completed,hrs_worked):   # Function to calculate individual efficiency
    Efficiency=(tasks_completed/hrs_worked)*10   # Compute efficiency using formula
    return Efficiency   # Return efficiency score

def calculate_efficiency(emp_name,dep_name,eff_score):   # Function to print individual employee report
    print(f"Employee: {emp_name} | Department: {dep_name} | Efficiency: {eff_score:.1f}")   # Display employee info
    if eff_score>25:   # Check individual performance
        print("Excellent Performance")   # Print excellent
    elif eff_score>15:   # Check for good performance
        print("Good Peformance")   # Print good
    else : print("Needs Improvement")   # Print needs improvement

print("Welcome to UST Employee Work Report System")   # Welcome message
print("This program helps HR calculate employee performance easily.")   # Info message
print("Current Active Project: UST Cloud Migration")   # Display current project

team_members=0;total_team_efficiency=0   # Initialize counters

while True:   # Loop to collect multiple employee data
    
    name=input("Enter Your Name : ")   # Input employee name
    team_members+=1   # Increment team member count
    department=input("Enter your Department Name : ")   # Input department
    tasks_completed=int(input("Enter Taks Completed : "))   # Input tasks completed
    hrs_worked=int(input("Total Hours Worked : "))   # Input hours worked
    efficiency=calculate_efficiney_score(tasks_completed,hrs_worked)   # Calculate efficiency
    total_team_efficiency+=efficiency   # Add to team total
    calculate_efficiency(name,department,efficiency)   # Print individual report

    choice=int(input("Press 1 to See Team Performance or Press 0 to Continue"))   # Option to view team performance
    if choice==1:
        print("Thanks for Comming..!")   # Exit message
        break


efficiency_score_of_team(team_members,total_team_efficiency)   # Calculate and display team efficiency
    

# SAMPLE OUTPUT

"""Welcome to UST Employee Work Report System
This program helps HR calculate employee performance easily.
Current Active Project: UST Cloud Migration
Enter Your Name : Gowtham
Enter your Department Name : IT
Enter Taks Completed : 30
Total Hours Worked : 2
Employee: Gowtham | Department: IT | Efficiency: 150.0
Excellent Performance
Press 1 to See Team Performance or Press 0 to Continue0
Enter Your Name : Vijay
Enter your Department Name : IT
Enter Taks Completed : 5
Total Hours Worked : 3
Employee: Vijay | Department: IT | Efficiency: 16.7
Good Peformance
Press 1 to See Team Performance or Press 0 to Continue1
Thanks for Comming..!
Average Team Efficiency : 83.3
Excellent team performance"""
