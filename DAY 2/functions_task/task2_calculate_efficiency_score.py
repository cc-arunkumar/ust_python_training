"""
Objective:
The HR team wants to calculate each employee’s efficiency score.
They will provide two inputs:
1. Hours worked by the employee
2. Tasks completed by the employee
The efficiency formula is:
Efficiency = (tasks_completed / hours_worked) × 10
Requirements:
Create a function that accepts these two inputs as parameters.
It should calculate the efficiency score using the above formula.
It should return the calculated value to the main program.
It should not print inside the function.

"""


def calculate_efficiney_score(tasks_completed,hrs_worked):
    Efficiency=(tasks_completed/hrs_worked)*10
    return Efficiency

tasks_completed=int(input("Enter Taks COmpleted: "))
hrs_worked=int(input("Total Hours Worked: "))
print(calculate_efficiney_score(tasks_completed,hrs_worked))


# SAMPLE OUTPUT

"""Enter Taks COmpleted: 10
Total Hours Worked: 5
20.0"""
