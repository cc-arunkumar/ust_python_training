# TASK: UST Employee Daily Work Report Automation

# TASK 2: Function with arguments and with return

def score(task_completed,hours_worked):
    efficiency = (task_completed / hours_worked) * 10
    return efficiency

task_completed = 120
hours_worked = 50
print(score(task_completed,hours_worked))

# Sample Output
# 4.0