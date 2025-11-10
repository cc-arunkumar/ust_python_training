# Task 3: Project Task Tracker
# Scenario:
# You are creating a task list for a new project module in your team.

# Step 1: Create task list
tasks = ["Requirement gathering", "Design UI", "Develop Backend", "Testing", "Deployment"]

# Step 2: Display the first and last task
print("First task:", tasks[0])
print("Last task:", tasks[-1])

# Step 3: Insert "Client Review" after "Testing"
index = tasks.index("Testing")
tasks.insert(index + 1, "Client Review")

# Step 4: Display only the first 3 tasks
print("First 3 tasks:", tasks[0:3])

# Step 5: Create a copy before making further changes
backup_tasks = tasks.copy()

# Step 6: Remove "Deployment" temporarily from the main list
tasks.remove("Deployment")

# Step 7: Print both lists
print("Backup list (unchanged):", backup_tasks)
print("Main list after removal:", tasks)


# Sample Output:
# First task: Requirement gathering
# Last task: Deployment
# First 3 tasks: ['Requirement gathering', 'Design UI', 'Develop Backend']
# Backup list (unchanged): ['Requirement gathering', 'Design UI', 'Develop Backend', 'Testing', 'Client Review', 'Deployment']
# Main list after removal: ['Requirement gathering', 'Design UI', 'Develop Backend', 'Testing', 'Client Review']
