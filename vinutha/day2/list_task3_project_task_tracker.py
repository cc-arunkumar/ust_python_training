# #Task 3: Project Task Tracker
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
# Day 3 3
# 6. Remove "Deployment" temporarily from the main list but not from the backup.
# 7. Print both lists to show that backup is safe and unchanged.
# Expected Output(sample):
# First task: Requirement gathering
# Last task: Deployment
# First 3 tasks: ['Requirement gathering', 'Design UI', 'Develop Backend']
# Backup list (unchanged): ['Requirement gathering', 'Design UI', 'Develop Back
# end', 'Testing', 'Client Review', 'Deployment']
# Main list after removal: ['Requirement gathering', 'Design UI', 'Develop Backen
# d', 'Testing', 'Client Review']


# Create a list of project tasks
tasks = ["Requirement gathering", "Design UI", "Develop Backend", "Testing", "Deployment"]

# Print the first task in the list (index 0)
print("First task:", tasks[0])

# Print the last task in the list (index -1 refers to the last element)
print("Last task:", tasks[-1])

# Insert a new task "Client Review" right after "Testing"
# tasks.index("Testing") → finds the position of "Testing"
# +1 → ensures "Client Review" is added immediately after "Testing"
tasks.insert(tasks.index("Testing") + 1, "Client Review")

# Print the first 3 tasks using slicing [:3]
print("First 3 tasks:", tasks[:3])

# Create a backup copy of the tasks list
backup_tasks = tasks.copy()

# Remove the "Deployment" task from the main list
tasks.remove("Deployment")

# Print the backup list (still contains "Deployment")
print("Backup list:", backup_tasks)

# Print the main list after removal (without "Deployment")
print("Main list after removal:", tasks)


#output
# PS C:\Users\303379\day3_training> & C:/Users/303379/AppData/Local/Microsoft/WindowsApps/python3.13.exe c:/Users/303379/day3_training/task3_project_task_tracker.py
# First task: Requirement gathering
# Last task: Deployment
# First 3 tasks: ['Requirement gathering', 'Design UI', 'Develop Backend']
# Backup list: ['Requirement gathering', 'Design UI', 'Develop Backend', 'Testing', 'Client Review', 'Deployment']
# Main list after removal: ['Requirement gathering', 'Design UI', 'Develop Backend', 'Testing', 'Client Review']
# PS C:\Users\303379\day3_training>
