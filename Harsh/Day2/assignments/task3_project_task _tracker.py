# Task 3: Project Task Tracker
# Scenario:
# You are creating a task list for a new project module in your team.

# Initialize a list of project tasks
tasks = ["Requirement gathering", "Design UI", "Develop Backend", "Testing", "Deployment"]

# Print the first task (index 0)
print(" First task:", tasks[0])

# Print the last task (index -1 refers to the last element)
print(" Last task:", tasks[-1])

# Insert a new task "Client Review" at index 3 (before "Testing")
tasks.insert(3, "Client Review")

# Slice the list to get the first 3 tasks (index 0 to 2)
three = tasks[0:3]
print(" First 3 tasks: ", three)

# Create a backup copy of the tasks list
backup_tasks = tasks.copy()

# Remove the "Deployment" task from the main list
tasks.remove("Deployment")

# Print the backup list (unchanged)
print(" Backup list (unchanged):", backup_tasks)

# Print the main list after removal
print(" Main list after removal:", tasks)

# ============Employee Expense System==============
#  First task: Requirement gathering
#  Last task: Deployment
#  First 3 tasks:  ['Requirement gathering', 'Design UI', 'Develop Backend']  
#  Backup list (unchanged): ['Requirement gathering', 'Design UI', 'Develop Backend', 'Client Review', 'Testing', 'Deployment']
#  Main list after removal: ['Requirement gathering', 'Design UI', 'Develop Backend', 'Client Review', 'Testing']