"""
Scenario:
You are creating a task list for a new project module in your team.

"""

# List of tasks for the project module
tasks=["Requirement gathering","Design UI","Develop Backend","Testing","Deployment"]

# Print the first task in the list
print("First task:",tasks[0])

# Print the last task in the list
print("Last task:",tasks[-1])

# Find the index of the "Testing" task
index_testing=tasks.index("Testing")

# Insert "Client Review" task right after "Testing"
tasks.insert(index_testing+1,"Client Review")

# Print the first 3 tasks from the updated list
print("First 3 tasks:",tasks[:3])

# Create a backup copy of the current tasks list
backup_tasks=tasks.copy()

# Remove the "Deployment" task from the main list
tasks.remove("Deployment")

# Print the backup list which remains unchanged
print("Backup list (unchanged):",backup_tasks)

# Print the main list after removing "Deployment"
print("Main list after removal:",tasks)


# sample output


"""
First task: Requirement gathering
Last task: Deployment
First 3 tasks: ['Requirement gathering', 'Design UI', 'Develop Backend']
Backup list (unchanged): ['Requirement gathering', 'Design UI', 'Develop Backend', 'Testing', 'Client Review', 'Deployment']
Main list after removal: ['Requirement gathering', 'Design UI', 'Develop Backend', 'Testing', 'Client Review']

"""
