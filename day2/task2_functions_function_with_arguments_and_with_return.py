#Part 2: Function with arguments and with return


def score(task_completed,hours_worked):
    efficiency=(task_completed/hours_worked)*10
    return efficiency
efficiency=score(6,70)
print("efficiency=",efficiency)

#efficiency= 0.8571428571428572