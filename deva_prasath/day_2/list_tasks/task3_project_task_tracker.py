#Project Task Tracker
# You are creating a task list for a new project module in your team.
# List of tasks
tasks = ["Requirement gathering", "Design UI", "Develop Backend", "Testing", "Deployment"]

# Print the first task
print("First task:", tasks[0])

# Print the last task
print("Last task:", tasks[-1])

# Print the first 3 tasks
print("First 3 tasks: ", tasks[:3])

# Create a backup copy of the tasks list
backup_tasks = tasks.copy()

# Remove the "Deployment" task from the main list
tasks.remove("Deployment")

# Print the backup list (unchanged)
print("Backup list (unchanged):", backup_tasks)

# Print the main list after removal of the "Deployment" task
print("Main list after removal:", tasks)


#Sample output

# First task: Requirement gathering
# Last task: Deployment
# First 3 tasks:  ['Requirement gathering', 'Design UI', 'Develop Backend']
# Backup list (unchanged): ['Requirement gathering', 'Design UI', 'Develop Backend', 'Testing', 'Deployment'] 
# Main list after removal: ['Requirement gathering', 'Design UI', 'Develop Backend', 'Testing']
