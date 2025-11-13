# Part 2: Function with arguments and with retur
def efficiency_score(tasks_completed,hours_worked):
    efficiency = (tasks_completed / hours_worked) * 10
    return efficiency

score=efficiency_score(25, 5)
print("Efficiency Score:", score)



# sample output
# Efficiency Score: 50.0
