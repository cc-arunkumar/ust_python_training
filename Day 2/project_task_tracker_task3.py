tasks = ["Requirement gathering", "Design UI", "Develop Backend", "Testing", "Deployment"]
first = tasks[0]
print(first)
last = tasks[-1]
print(last)
for i in range(len(tasks) - 1):
    if tasks[i] == "Testing":
        tasks.insert(i, "Client Review")

print(tasks)

first_three = tasks[0 : 3]
print(first_three)

backup_tasks = tasks.copy()
tasks.remove("Deployment")
print(tasks)
print(backup_tasks)


