# Project Task Tracker
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
# changes.
# 6. Remove "Deployment" temporarily from the main list but not from the backup.
# 7. Print both lists to show that backup is safe and unchanged.


tasks = ["Requirement gathering", "Design UI", "Develop Backend", "Testing", "Deployment"]
print("First task:", tasks[0])
print("Last task:", tasks[-1])
index = tasks.index("Testing")
tasks.insert(index + 1, "Client Review")
print("First 3 tasks:", tasks[:3])
backup_tasks = tasks.copy()
tasks.remove("Deployment")
print("Backup list (unchanged):", backup_tasks)
print("Main list after removal:", tasks)
 

#o/p:
#First task: Requirement gathering
#Last task: Deployment
#First 3 tasks: ['Requirement gathering', 'Design UI', 'Develop Backend']
#Backup list (unchanged): ['Requirement gathering', 'Design UI', 'Develop Backend', 'Testing', 'Client Review', 'Deployment']
#Main list after removal: ['Requirement gathering', 'Design UI', 'Develop Backend', 'Testing', 'Client Review']