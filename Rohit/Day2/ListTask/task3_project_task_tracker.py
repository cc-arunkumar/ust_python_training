# Task 3: Project Task Tracker
# Scenario:
# You are creating a task list for a new project module in your team.



# step:1 Initialize the list of tasks
tasks = ["Requirement gathering", "Design UI", "Develop Backend", "Testing", "Deployment"]

# step:2 Print the first task in the list
print(tasks[0])

# step:3 Print the last task in the list
print(tasks[-1])

# step:4 Iterate through the list (excluding the last item)
for x in range(len(tasks) - 1):
    print(x)
    # step:5 Insert "client Review" before "Testing" if found
    if tasks[x] == "Testing":
        tasks.insert(x, "client Review")

# step:6 Print the updated list of tasks
print(tasks)

# step:7 Print the first three tasks using slicing
print(tasks[0:3])

# step:7 Create a shallow copy of the tasks list
backup_tasks = tasks.copy()

# step:8 Remove "Deployment" from the original tasks list
tasks.remove("Deployment")

# step:9 Print the modified tasks list
print(tasks)

# step:10 Print the backup list to show it remains unchanged
print(backup_tasks)

# ======================sample output==================
# Requirement gathering
# Deployment
# 1
# 2
# 3
# ['Requirement gathering', 'Design UI', 'Develop Backend', 'client Review', 'Testing', 'Deployment']       
# ['Requirement gathering', 'Design UI', 'Develop Backend']
# ['Requirement gathering', 'Design UI', 'Develop Backend', 'client Review', 'Testing']
# ['Requirement gathering', 'Design UI', 'Develop Backend', 'client Review', 'Testing', 'Deployment'] 