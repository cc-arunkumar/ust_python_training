#Task : Function task
def greet():
    print("Welcome to UST Employee Work Report System !")
    print("This Program helps HR to calculate the employee performance easily.")

def efficiency(hours, tasks):
    eff = (tasks / hours) * 10
    return eff
val = efficiency(15, 30)



def performance(name, dept_name, efficiency_score):
    print(f"Name : {name}, Depatment : {dept_name}, Eff : {efficiency_score}")
    efficiency_score = val
    if efficiency_score > 25:
        print("Excellent Performance")
    elif efficiency_score > 14 or efficiency_score < 26:
        print("Good Performance")
    else:
        print("Needs Improvement!")

def project():
    return "UST Cloud Migration"

def team(*efficiency):
    sum = 0
    count = 0
    for effi in efficiency:
        sum = sum + effi
        count = count + 1
    average = sum / count
    print("Average team score is : ", round(average, 1))
    if average > 25:
        print("Team performed beyond expectations")
    else: 
        print("Need Improvement!")


greet()
print(project())
performance("Asha", "Developer", 25)
performance("Anil", "Finance", 23)
team(25,23,21,22,30,40,50)

#output
# Welcome to UST Employee Work Report System !
# This Program helps HR to calculate the employee performance easily.
# UST Cloud Migration
# Name : Asha, Depatment : Developer, Eff : 25
# Good Performance
# Name : Anil, Depatment : Finance, Eff : 23
# Good Performance
# Average team score is :  30.1
# Team performed beyond expectations