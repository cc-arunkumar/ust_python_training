from greet import greet
from efficiency_score import efficency_score
from display import display         
from curr import curr_project
tot_score=0
def greet():
    print("Welcome to UST Employee Work Report System")

def efficency_score(tasks_completed, hours_worked):
    if hours_worked == 0:
        return 0
    score = (tasks_completed / hours_worked)*10
    return score
def display(e_name,dep_name,score):
    print(f"Employee Name: {e_name}|Department: {dep_name}|Efficiency Score: {score:.2f}")
    if score >25:
        print("Excellent Performance")
    elif score >15:
        print("Good Performance")
    else:
        print("Needs Improvement")
def curr_project():
    return("Current Project: AI Development")
def consolidated_report(*args):
    n=len(args)
    sum=0
    for report in args:
        sum += report
    average = sum/n
    return average
greet()
curr_project()
for i in range(3):
    name=input("Enter Employee Name: ")
    department=input("Enter Department Name: ")
    tasks=int(input("Enter number of tasks completed: "))
    hours=int(input("Enter number of hours worked: "))
    score=efficency_score(tasks,hours)
    display(name,department,score)
    tot_score += score
avg_score=tot_score/3
print(f"Consolidated Average Efficiency Score: {avg_score:.2f}")
if avg_score <20:
    print("Overall Department Performance Needs Improvement")
else:
    print("Overall Department Performance is Satisfactory")

# Welcome to UST Employee Work Report System
# Enter Employee Name: Arumukesh
# Enter Department Name: IT
# Enter number of tasks completed: 5
# Enter number of hours worked: 15
# Employee Name: Arumukesh|Department: IT|Efficiency Score: 3.33
# Needs Improvement
# Enter Employee Name: hari
# Enter Department Name: AI
# Enter number of tasks completed: 30
# Enter number of hours worked: 40
# Employee Name: hari|Department: AI|Efficiency Score: 7.50
# Needs Improvement
# Enter Employee Name: Akshit
# Enter Department Name: Machine Learning
# Enter number of tasks completed: 50
# Enter number of hours worked: 100
# Employee Name: Akshit|Department: Machine Learning|Efficiency Score: 5.00
# Needs Improvement
# Consolidated Average Efficiency Score: 5.28
# Overall Department Performance Needs Improvement
