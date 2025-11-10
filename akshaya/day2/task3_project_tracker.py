# Task 3: Project Task Tracker


tasks = ["Requirement gathering", "Design UI", "Develop Backend", "Testing", "Deployment"]


print("First task:", tasks[0])
print("Last task:", tasks[-1])


index = tasks.index("Testing")
tasks.insert(index + 1, "Client Review")


print("First 3 tasks:", tasks[:3])


backup_tasks = tasks.copy()


tasks.remove("Deployment")


print("Backup list (unchanged):", backup_tasks)
print("Main list after removal:", tasks)

#sample output
# PS C:\Users\303375\Downloads\Tasks> python task3_project_tracker.py
# First task: Requirement gathering
# Last task: Deployment
# First 3 tasks: ['Requirement gathering', 'Design UI', 'Develop Backend']
# Backup list (unchanged): ['Requirement gathering', 'Design UI', 'Develop Backend', 'Testing', 'Client Review', 'Deployment']
# Main list after removal: ['Requirement gathering', 'Design UI', 'Develop Backend', 'Testing', 'Client Review'] 