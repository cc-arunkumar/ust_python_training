#Function with arguments and without return

def score(task_completed, hours_worked):
    return (task_completed / hours_worked) * 10
def formated_report(emp_name, dept_name, eff_score):
    print("Employee Name:", emp_name)
    print("Department Name:", dept_name)
    print("Efficiency Score:", round(eff_score, 2))
    if eff_score > 25:
        print("Excellent performance")
    elif 15 <= eff_score <= 25:
        print("Good performance")
    else:
        print("Needs improvement")
name = input("Enter employee name: ")
dept = input("Enter department name: ")
tasks = int(input("Enter tasks completed: "))
hours = float(input("Enter hours worked: "))
eff = score(tasks, hours)
formated_report(name, dept, eff)
 
# Enter employee name: Bhargavi S
# Enter department name: Devlopment
# Enter tasks completed: 30
# Enter hours worked: 20
# Employee Name: Bhargavi S
# Department Name: Devlopment
# Efficiency Score: 15.0
# Good performance