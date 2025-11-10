# Task 3: Project Task Tracker
# Scenario:
# You are creating a task list for a new project module in your team.
# Instructions:
# 1. Create a list called tasks containing:
# ["Requirement gathering", "Design UI", "Develop Backend", "Testing", "De
# ployment"]
# 2. Display:
# The first task
# The last task
# (Hint: use indexing — tasks[0] and tasks[-1] )
# 3. The client requested a review phase after testing.
# Insert "Client Review" after "Testing" .
# (Hint: find the index of "Testing" and use insert() )
# 4. Display only the first 3 tasks (use slicing).
# 5. Create a copy of the task list named backup_tasks before you make further
# # changes.
# 6. Remove "Deployment" temporarily from the main list but not from the backup.
# 7. Print both lists to show that backup is safe and unchanged.


tasks=["Requirement gathering", "Design UI", "Develop Backend", "Testing", "Deployment"]
print("first task:",tasks[0])
print("last task:",tasks[-1])
tasks.insert(4,"client review")
print("first 3 tasks:",tasks[:3])
backup_tasks=print("backup_tasks",tasks)
tasks.remove("Deployment")
print("main list after removel:",tasks)


# sample output
# first task: Requirement gathering
# last task: Deployment
# first 3 tasks: ['Requirement gathering', 'Design UI', 'Develop Backend']
# backup_tasks ['Requirement gathering', 'Design UI', 'Develop Backend', 'Testing', 'client review', 'Deployment']
# main list after removel: ['Requirement gathering', 'Design UI', 'Develop Backend', 'Testing', 'client review']