# Part 1: Function without arguments and without
# return
# Objective:
# Day 2 1
# When the program starts, it should display a small welcome message for the user.
# This message doesn’t depend on any input from the user — it will always remain
# the same.
# Requirements:
# Create a function that prints a welcome message like:
# “Welcome to UST Employee Work Report System”
# “This program helps HR calculate employee performance easily.”
# The function should not take any parameters.
# It should only display the message and not return anything



# Part 1: Function without arguments and without return
def ustEmployeeWorkSystem():
    print("welcome to ust Employee work Report system")
    print("this program helps HR calculate employee performance easily")

ustEmployeeWorkSystem()


# Part 2: Function with arguments and return value
def efficiency_score(first, second):
    efficiency = (second / first) * 10
    return efficiency

val = efficiency_score(10, 20)


# Part 3: Function with arguments and conditional logic
def calculate_performance(name, dept_name, val):
    if val > 25:
        print(name)
        print(dept_name)
        print("Excellent performance")
    elif val > 15 or val < 25:
        print(name)
        print(dept_name)
        print("Good Performance")
    else:
        print(name)
        print(dept_name)
        print("Needs Improvement")

calculate_performance("Rohit", "SDE", val)


# Part 4: Function without arguments but with return
def active_project():
    return "UST Cloud Migration"

print(active_project())


# Part 5: Function with variable-length arguments
def average_team_efficiency(*team_effeciency):
    sum = 0
    val = len(team_effeciency)
    for x in team_effeciency:
        sum += x

    ans = sum / val
    if ans > 25:
        print("Team Performed above Expectations")
    else:
        print("Team Needs improvement")

average_team_efficiency(26, 20, 14.3)






# =============sample output================
# welcome to ust Employee work Report system
# this program helps HR calculate employee performance easily
# Rohit
# SDE
# Good Performance
# UST Cloud Migration
# Team Needs improvement