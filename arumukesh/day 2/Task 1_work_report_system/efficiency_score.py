def efficency_score(tasks_completed, hours_worked):
    if hours_worked == 0:
        return 0
    score = (tasks_completed / hours_worked)*10
    return score