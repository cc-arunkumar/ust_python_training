#Task 3: Project Task Tracker

# List of tasks in the project
tasks = ["Requirement gathering", "Design UI", "Develop Backend", "Testing", "Deployment"]

# Printing the first task (index 0)
print("First task: ", tasks[0])

# Printing the last task (using negative indexing)
print("Last task: ", tasks[-1])

# Inserting a new task ("Client Review") at index 4
tasks.insert(4, "Client Review")

# Printing the first 3 tasks using slicing (index 0 to 2)
print("First 3 tasks: ", tasks[0:3])

# Creating a backup copy of the tasks list using copy()
backup_tasks = tasks.copy()

# Removing the "Deployment" task from the main list
tasks.remove("Deployment")

# Printing the main list after removal of "Deployment"
print("Main list after removal: ", tasks)

# Printing the backup list, which remains unchanged
print("Backup list (unchanged): ", backup_tasks)


# #Sample Output
# First task:  Requirement gathering
# Last task:  Deployment
# First 3 tasks:  ['Requirement gathering', 'Design UI', 'Develop Backend']
# Main list after removal:  ['Requirement gathering', 'Design UI', 'Develop Backend', 'Testing', 'Client Review']
# Backup list (unchanged):  ['Requirement gathering', 'Design UI', 'Develop Backend', 'Testing', 'Client Review', 'Deployment']