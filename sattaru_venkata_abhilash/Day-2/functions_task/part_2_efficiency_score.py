# Part 2: Function with arguments and with return
# Objective:
# Calculate the employee’s efficiency score using:
# Efficiency = (tasks_completed / hours_worked) × 10
# The function accepts two inputs and returns the calculated efficiency.

def efficiency_score(hours_worked, tasks_completed):
    Efficiency = (tasks_completed / hours_worked) * 10
    return Efficiency


# Sample Output:
# >>> efficiency_score(10, 11)
# 11.0
# >>> efficiency_score(8, 9)
# 11.25
# >>> efficiency_score(4, 8)
# 20.0
