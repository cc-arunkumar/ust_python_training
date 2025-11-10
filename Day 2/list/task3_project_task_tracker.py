# Task 3: Project Task Tracker
# Scenario:
# You are creating a task list for a new project module in your team.

tasks=["Requirement gathering","Design UI","Develop Backend","Testing","Deployment"]
print("First task:",tasks[0])
print("Last task:",tasks[-1])
index_testing=tasks.index("Testing")
tasks.insert(index_testing+1,"Client Review")
print("First 3 tasks:",tasks[:3])
backup_tasks=tasks.copy()
tasks.remove("Deployment")
print("Backup list (unchanged):",backup_tasks)
print("Main list after removal:",tasks)

# sample output:
# First task: Requirement gathering
# Last task: Deployment
# First 3 tasks: ['Requirement gathering', 'Design UI', 'Develop Backend']
# Backup list (unchanged): ['Requirement gathering', 'Design UI', 'Develop Backend', 'Testing', 'Client Review', 'Deployment']
# Main list after removal: ['Requirement gathering', 'Design UI', 'Develop Backend', 'Testing', 'Client Review']