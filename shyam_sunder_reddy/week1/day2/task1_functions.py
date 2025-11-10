# Task: UST Employee DailyWork Report
# Automation
# Background:
# UST managers maintain daily work reports for each employee.
# Every employee records:
# How many hours they worked,
# How many tasks they completed, and
# Their department name.
# The HR department wants a small Python program that helps them automate a
# few daily actions.
# You have been assigned to build this small program step-by-step using different
# kinds of Python functions.
# The goal of this exercise is not only to get the output but also to understand when
# and why we use:
# 1. Functions with arguments and return values
# 2. Functions without arguments but with return values
# 3. Functions with arguments but without return values
# 4. Functions without arguments and without return values
# 5. Functions with variable arguments ( args )

# Part 1: Function without arguments and without
# return
# Objective:
# When the program starts, it should display a small welcome message for the user.
# This message doesn’t depend on any input from the user — it will always remain
# the same.
# Requirements:
# Create a function that prints a welcome message like:
# “Welcome to UST Employee Work Report System”
# “This program helps HR calculate employee performance easily.”
# The function should not take any parameters.
# It should only display the message and not return anything.

def noargsnoreturn():
    print("Welcome to UST Employee Work Report System")
    print("This program helps HR calculate employee performance easily.")

#Part 2: Function with arguments and with return
# #bjective:
# The HR team wants to calculate each employee’s efficiency score.
# They will provide two inputs:
# 1. Hours worked by the employee
# 2. Tasks completed by the employee
# The efficiency formula is:
# Efficiency = (tasks_completed / hours_worked) × 10
# Requirements:
# Create a function that accepts these two inputs as parameters.
# It should calculate the efficiency score using the above formula.
# It should return the calculated value to the main program.
# It should not print inside the function.


def argsandreturn(hours,completed):
    efficiency=(completed/hours)*10
    return efficiency

# # Part3: Function with arguments and without return
# Objective:
# After calculating the efficiency, HR wants to print a formatted report for each
# employee.
# Requirements:
# Create a function that takes 3 inputs:
# Employee Name
# Department Name
# Efficiency Score (calculated from the previous function)
# Inside the function:
# Print the employee’s details in a clean, readable format.
# If efficiency is greater than 25, print:
# “Excellent performance.”
# If efficiency is between 15 and 25, print:
# “Good performance.”
# Otherwise, print:
# “Needs improvement.”
# This function should not return any value — it only displays output
def argsandnoreturn(name,department,efficiency):
    print("Employee: ",name,end="|")
    print("Department: ",department,end="|")
    print("Efficiency: ",efficiency)
    if(efficiency>25):
        print("Excellent performance.")
    elif(efficiency>=15):
        print("Good performance.")
    else:
        print("Needs improvement.")

#Part 4: Function without arguments but with return
# Objective:
# Sometimes we need fixed information that doesn’t come from the user, like a
# default project name.
# Requirements:
# Create a function that returns the current active project name, e.g., "UST Cloud
# Migration" .
# The function should not accept any parameters.
# It should just return the value to the main program.
def noargsandreturn():
    return "UST Cloud Migration"

# #Part 5: Function with variable arguments ( args )
# Objective:
# After collecting data from multiple employees, HR wants to know the average
# efficiency score of the entire team.
# Requirements:
# Create a function that accepts any number of efficiency scores.
# It should calculate and print the average of all the scores.
# Based on the average:
# If average > 25 → “Team performed above expectations.”
# Otherwise → “Team needs improvement.”
# The function should only print the result and not return anything.
def variableargs(*efficiency):
    length=len(efficiency)
    sum=0
    for e in efficiency:
        sum=sum+e
    sum=sum/length
    print("Average Team Efficiency: ",sum)
    if(sum>25):
        print("Team performed above expectations.")
    else:
        print("Team needs improvement.")



noargsnoreturn()
print()
print(noargsandreturn())
print()
eff1=argsandreturn(90,190)
argsandnoreturn("shyam","Finance",eff1)
print()
eff2=argsandreturn(80,100)
argsandnoreturn("Rahul","IT",eff2)
print()
eff3=argsandreturn(60,120)
argsandnoreturn("Sneha","HR",eff3)
print()
variableargs(eff1,eff2,eff3)


#Sample output
# Welcome to UST Employee Work Report System
# This program helps HR calculate employee performance easily.

# UST Cloud Migration

# Employee:  shyam|Department:  Finance|Efficiency:  21.11111111111111
# Good performance.

# Employee:  Rahul|Department:  IT|Efficiency:  12.5
# Needs improvement.

# Employee:  Sneha|Department:  HR|Efficiency:  20.0
# Good performance.

# Average Team Efficiency:  17.87037037037037
# Team needs improvement.