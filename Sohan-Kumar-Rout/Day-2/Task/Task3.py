from Task2 import efficiency_score
def report(name,dept_name,eff_score):
    print("=====Employee Details======")
    print("Name of the Employee : ",name)
    print("Name of department : ",dept_name)
    print("Efficiency score : ",eff_score)
    
    if(eff_score>25):
        print("Excellent performance")
    elif(eff_score>=15 and eff_score<=25):
        print("Good Performance")
    else:
        print("Needs Improvement")

name = input("Enter the name of the Employee : ")
dept_name = input("Enter the department name : ")
hours_worked=float(input("Enter the number of hours worked : "))
tasks_completed = float(input("Enter the Task completed : "))
eff_score=efficiency_score(hours_worked,tasks_completed)
report(name,dept_name,eff_score)

