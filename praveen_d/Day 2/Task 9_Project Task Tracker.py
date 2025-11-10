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
# Day 3 3
# 6. Remove "Deployment" temporarily from the main list but not from the backup.
# 7. Print both lists to show that backup is safe and unchanged.

tasks=["Requirement gathering", "Design UI", "Develop Backend", "Testing", "Deployment"]

print(tasks[0])
print(tasks[len(tasks)-1])

tasks.insert(4,"Client Review")

print(tasks[0:3])
backup_tasks=tasks
print(backup_tasks)

tasks.remove("Deployment")
print(tasks)
print(backup_tasks)