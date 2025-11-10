#Task 3: Project Task Tracker

# Scenario:
# You are creating a task list for a new project module in your team.

# Instructions:
    # 1. Create a list called tasks containing:
    # ["Requirement gathering", "Design UI", "Develop Backend", "Testing", "Deployment"]
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

# Expected Output(sample):
# First task: Requirement gathering
# Last task: Deployment
# First 3 tasks: ['Requirement gathering', 'Design UI', 'Develop Backend']
# Backup list (unchanged): ['Requirement gathering', 'Design UI', 'Develop Backend', 'Testing', 'Client Review', 'Deployment']
# Main list after removal: ['Requirement gathering', 'Design UI', 'Develop Backend', 'Testing', 'Client Review']

tasks = ["Requirement gathering", "Design UI", "Develop Backend", "Testing", "Deployment"]
print("First Task: ",tasks[0])
print("Last Task: ",tasks[-1])
idx_testing = tasks.index("Testing")
tasks.insert(idx_testing+1,"Client Review")
print("First Three Tasks: ",tasks[:3])
backup_tasks = tasks 
print("Backup List (unchanged)",backup_tasks)
tasks.remove("Deployment")
print("Main List after removal:",tasks)

#Sample Output
# First Task:  Requirement gathering
# Last Task:  Deployment
# First Three Tasks:  ['Requirement gathering', 'Design UI', 'Develop Backend']
# Backup List (unchanged) ['Requirement gathering', 'Design UI', 'Develop Backend', 'Testing', 'Client Review', 'Deployment']
# Main List after removal: ['Requirement gathering', 'Design UI', 'Develop Backend', 'Testing', 'Client Review']  