# Part 1 : FUnction without argumennts and without return

def ustEmployeeWorkSystem():
    print("welcome to ust Employee work Report system")
    print("this program helps HR calculate employee performance easily")

ustEmployeeWorkSystem()

#part4
def active_project():
    return "UST Cloud Migration"

print(active_project())



# Part2
def efficiency_score(first , second):
    efficiency = (second/first)*10
    return efficiency

val = efficiency_score(10,20)



def calculate_performance(name, dept_name, val):
    if val>25:
        print(name)
        print(dept_name)
        print("Excellent performance")
    elif val>15 or val< 25:
        print(name)
        print(dept_name)
        print("Good Performance")
    else:
        print(name)
        print(dept_name)
        print("Needs Improvement")


# part 3
calculate_performance("Rohit", "SDE",val)


def average_team_efficiency(*team_effeciency):
    sum=0
    val = len(team_effeciency)
    for x in team_effeciency:
        sum+=x


    ans = sum/val
    if ans>25:
        print("Team Performed above Expectations")
    else:
        print("Team Needs improvement")

average_team_efficiency(26,20,14.3)

















