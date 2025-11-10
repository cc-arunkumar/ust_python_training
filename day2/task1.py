# function should not take any parameters or return
def message():
    print("Welcome to UST Employee Work Report System.")
    print("This program helps HR calculate employee performance easily.")
# should not print inside the function
def score(hours, tasks):
    efficiency =(task/hours)*10
    return efficiency

def eff(emp_name,dep_name,efficiency):
    print("Employee name is:",emp_name)
    if(efficiency>25):
        print("Excellent performance.")
    elif(efficiency>=15 and efficiency<=25):
        print("Good performance.")
    else:
        print("Needs improvement.")


message()
emp_name=input("Enter name of employee: ")
dep_name=input("Enter department name: ")
hours=float(input("Enter total hours: "))
task=int(input("Enter total task completed: "))
efficiency=score(hours,task)
employment_detail=eff(emp_name,dep_name,efficiency)


def project():
    project_name="TASK 1"
    print("Project name is",project_name)

def team_avg(*efficiency):
    sum = 0
    count += 0
    for x in team_avg:
        sum += x
        avg = sum/count
    # total = sum(efficiency)
    # num = len(team_avg)
    # avg = sum/len

    if(avg>25):
        print("Team performance over expectation.")
    else:
        print("Teams need improvement.")

team_avg=(34,78,67,88)

project()
# team_avg()





