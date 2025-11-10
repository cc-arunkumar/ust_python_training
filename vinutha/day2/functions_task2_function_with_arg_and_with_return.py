# #function with argumnets and with return

# Part 2: Function with arguments and with return
# Objective:
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

# code

def efficency_Score(hours,task):
    Efficiency=(task/hours)*10
    return Efficiency
print(efficency_Score(10,20))

# output
# PS C:\Users\303379\day2_training> & C:/Users/303379/AppData/Local/Microsoft/WindowsApps/python3.13.exe c:/Users/303379/day2_training/task2.py
# 20.0
# PS C:\Users\303379\day2_training> 