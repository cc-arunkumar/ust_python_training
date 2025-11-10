
# Task 2: Function with arguments and with return

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

def efficiency(a,b):
    efficiency=(a/b)*10
    return efficiency
a=efficiency(10,10)
print(a)


#Sample output
#10