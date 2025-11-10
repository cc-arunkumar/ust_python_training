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
# changes.
# Day 3 3
# 6. Remove "Deployment" temporarily from the main list but not from the backup.
# 7. Print both lists to show that backup is safe and unchaned

tasks=["Requirement gathering", "Design UI", "Develop Backend", "Testing", "Deployment"]
print("First Task:",tasks[0])
print("Last Task:",tasks[-1])
print("First Three Tasks: ",tasks[:3])
index= tasks.index("Testing")
tasks.insert(index+1,"Client Review")
back_up = tasks.copy()
tasks.remove("Deployment")
print("Back up list: ",back_up)
print("Main List After Removal: ",tasks)

#sample output

# First Task: Requirement gathering
# Last Task: Deployment
# First Three Tasks:  ['Requirement gathering', 'Design UI', 'Develop Backend']
# Back up list:  ['Requirement gathering', 'Design UI', 'Develop Backend', 'Testing', 'Client Review', 'Deployment']
# Main List After Removal:  ['Requirement gathering', 'Design UI', 'Develop Backend', 'Testing', 'Client Review']