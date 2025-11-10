# # Function with variable arguments ( args )

# Part 5: Function with variable arguments ( args )
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
# Expected Output Flow:
# When participants run the program step-by-step, the flow should look something
# like this (final combined view):
# Welcome to UST Employee Work Report System
# This program helps HR calculate employee performance easily.
# Current Active Project: UST Cloud Migration
# Employee: Asha | Department: Finance | Efficiency: 26.0
# Excellent performance.
# Employee: Rahul | Department: IT | Efficiency: 20.0
# Good performance.
# Day 2 4
# Employee: Sneha | Department: HR | Efficiency: 14.3
# Needs improvement.
# Average Team Efficiency: 20.1
# Team needs improvement.

#code

def compute_efficiency(tasks, duration):
    return (tasks / duration) * 10

def show_report(emp, dept, score):
    print(f"Employee: {emp} | Department: {dept} | Efficiency: {round(score, 1)}")
    if score > 25:
        print("Excellent performance.")
    elif 15 <= score <= 25:
        print("Good performance.")
    else:
        print("Needs improvement.")

def team_summary(*values):
    if len(values) == 0:
        print("No data available.")
        return
    avg_score = sum(values) / len(values)
    print(f"Average Team Efficiency: {round(avg_score, 1)}")
    if avg_score > 25:
        print("Team performed above expectations.")
    else:
        print("Team needs improvement.")

print("Welcome to UST Employee Work Report System")
print("This program helps HR calculate employee performance easily.")
print("Current Active Project: UST Cloud Migration")

score_asha = compute_efficiency(13, 5)
show_report("Asha", "Finance", score_asha)

score_rahul = compute_efficiency(10, 5)
show_report("Rahul", "IT", score_rahul)

score_sneha = compute_efficiency(10, 7)
show_report("Sneha", "HR", score_sneha)

team_summary(score_asha, score_rahul, score_sneha)

#output
# PS C:\Users\303379\day2_training> & C:/Users/303379/AppData/Local/Microsoft/WindowsApps/python3.13.exe c:/Users/303379/day2_training/task5_functions.py
# Welcome to UST Employee Work Report System
# This program helps HR calculate employee performance easily.
# Current Active Project: UST Cloud Migration
# Employee: Asha | Department: Finance | Efficiency: 26.0
# Excellent performance.
# Employee: Rahul | Department: IT | Efficiency: 20.0
# Good performance.
# Employee: Sneha | Department: HR | Efficiency: 14.3
# Needs improvement.
# Average Team Efficiency: 20.1
# Team needs improvement.
# PS C:\Users\303379\day2_training> 
