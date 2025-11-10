task = ["Requirement gathering", "Design UI", "Develop Backend", "Testing", "Deployment"]
first = task[0]
print(first)
last = task[-1]
print(last)
for i in range(len(task) - 1):
    if task[i] == "Testing":
        task.insert(i, "Client Review")

print(task)

first_three = task[0 : 3]
print(first_three)

back_task = task.copy()
task.remove("Deployment")
print(task)
print(back_task)


# Requirement gathering
# Deployment
# ['Requirement gathering', 'Design UI', 'Develop Backend', 'Client Review', 'Testing', 'Deployment']
# ['Requirement gathering', 'Design UI', 'Develop Backend']
# ['Requirement gathering', 'Design UI', 'Develop Backend', 'Client Review', 'Testing']
# ['Requirement gathering', 'Design UI', 'Develop Backend', 'Client Review', 'Testing', 'Deployment']