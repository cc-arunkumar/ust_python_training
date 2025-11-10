#Functions Task

def welcome_msg():
    print("Welcome to UST Employee Work Report System")
    print("This program helps HR calculate employee performance easily")

def efficiency_score(hours_worked, tasks_completed):
    efficiency = (tasks_completed / hours_worked) * 10
    return efficiency

def formatted_report(emp_name, dept_name, score):
    print(f"\nEmployee: {emp_name}")
    print(f"Department: {dept_name}")
    print(f"Efficiency Score: {score:.2f}")
    if score > 25:
        print("Excellent performance")
    elif 15 <= score <= 25:
        print("Good Performance")
    else:
        print("Needs Improvement")

def active_project():
    return "Current Active Project : UST Cloud Migration"

def avg_efficiency_score(*scores):
    average = sum(scores) / len(scores)
    print(f"\nAverage Team Efficiency Score: {average:.2f}")
    if average > 25:
        print("Team performed above expectations")
    else:
        print("Team needs improvement")

welcome_msg()

hours_worked = int(input("Enter hours worked: "))
tasks_completed = int(input("Enter tasks completed: "))

score = efficiency_score(hours_worked, tasks_completed)
print(active_project())

formatted_report("Amit", "Cloud Services", score)

avg_efficiency_score(28, 22, 18, 30)


'''output:
Welcome to UST Employee Work Report System
This program helps HR calculate employee performance easily
Enter hours worked: 2
Enter tasks completed: 10
Current Active Project : UST Cloud Migration

Employee: Amit
Department: Cloud Services
Efficiency Score: 50.00
Excellent performance

Average Team Efficiency Score: 24.50
Team needs improvement
'''