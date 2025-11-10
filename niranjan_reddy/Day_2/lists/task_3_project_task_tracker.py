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

# 3. The client requested a review phase after testing.
# Insert "Client Review" after "Testing" .

# 4. Display only the first 3 tasks (use slicing).
# 5. Create a copy of the task list named backup_tasks before you make further
# changes.

# 6. Remove "Deployment" temporarily from the main list but not from the backup.

# 7. Print both lists to show that backup is safe and unchanged



tasks=["Requirement gathering", "Design UI", "Develop Backend", "Testing", "Deployment"]

print("First task:",tasks[0])

print("Last task:",tasks[-1])

tasks.insert(4,"Client Review")

print("First 3 tasks:",tasks[0:3])

backup_tasks=tasks

print("Backup list (unchanged):",backup_tasks)

tasks.remove("Deployment")

print("Main list after removal:",tasks)


# Sample Output


# First task: Requirement gathering

# Last task: Deployment

# First 3 tasks: ['Requirement gathering', 'Design UI', 'Develop Backend']

# Backup list (unchanged): ['Requirement gathering', 'Design UI', 'Develop Backend', 'Testing', 'Client Review', 'Deployment']

# Main list after removal: ['Requirement gathering', 'Design UI', 'Develop Backend', 'Testing', 'Client Review']