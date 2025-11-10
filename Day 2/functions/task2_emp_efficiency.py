# Part 2: Function with arguments and with return
# Objective:
# The HR team wants to calculate each employee’s efficiency score.
# They will provide two inputs:
# 1. Hours worked by the employee
# 2. Tasks completed by the employee
# The efficiency formula is:
# Efficiency = (tasks_completed / hours_worked) × 10

def calculate_efficiency_score(tot_hours,tot_task):
    return (tot_task/tot_hours)*10

tot_hours = int(input("Enter the hours Worked :"))
tot_task = int(input("Enter the Task Completed :"))
res = calculate_efficiency_score(tot_hours,tot_task)
print(f"proficiency Score is:{res}\n")


# sample output

# Enter the hours Worked :9
# Enter the Task Completed :25
# proficiency Score is:27.77777777777778