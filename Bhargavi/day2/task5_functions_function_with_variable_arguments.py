#Function with variable arguments


def score(task_completed, hours_worked):
    return (task_completed / hours_worked) * 10
def formated_report(emp_name, dept_name, eff_score):
    print(f"Employee: {emp_name} | Department: {dept_name} | Efficiency: {round(eff_score, 1)}")
    if eff_score > 25:
        print("Excellent performance.")
    elif 15 <= eff_score <= 25:
        print("Good performance.")
    else:
        print("Needs improvement.")
def team_average(*eff_scores):
    avg = sum(eff_scores) / len(eff_scores)
    print(f"Average Team Efficiency: {round(avg, 1)}")
    if avg > 25:
        print("Team performed above expectations.")
    else:
        print("Team needs improvement.")
print("Welcome to UST Employee Work Report System")
print("This program helps HR calculate employee performance easily.")
print("Current Active Project: UST Cloud Migration")
eff1 = score(13, 5)    
formated_report("Bhargavi", "Finance", eff1)
eff2 = score(10, 5)    
formated_report("Meena", "IT", eff2)
eff3 = score(10, 7)    
formated_report("Shero", "HR", eff3)
team_average(eff1, eff2, eff3)

# Welcome to UST Employee Work Report System
# This program helps HR calculate employee performance easily.
# Current Active Project: UST Cloud Migration
# Employee: Bhargavi | Department: Finance | Efficiency: 26.0
# Excellent performance.
# Employee: Meena | Department: IT | Efficiency: 20.0
# Good performance.
# Employee: Shero | Department: HR | Efficiency: 14.3
# Needs improvement.
# Average Team Efficiency: 20.1
# Team needs improvement.