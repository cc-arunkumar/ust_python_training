# TASK 3 -  Project Task Tracker

tasks = ["Requirement gathering", "Design UI", "Develop Backend", "Testing", "Deployment"]
print("First Task: ",tasks[0])
print("Last Task: ",tasks[-1])

tasks.insert(4,"Client_Review")
print("First 3 Tasks: ",tasks[:3])

backup_tasks = tasks
print("Backup tasks(Unchanged): ",backup_tasks)


tasks.remove("Deployment")
print("Main list after removal: ",tasks)

# Sample Output
# First Task:  Requirement gathering
# Last Task:  Deployment
# First 3 Tasks:  ['Requirement gathering', 'Design UI', 'Develop Backend']
# Backup tasks(Unchanged):  ['Requirement gathering', 'Design UI', 'Develop Backend', 'Testing', 'Client_Review', 'Deployment']
# Main list after removal:  ['Requirement gathering', 'Design UI', 'Develop Backend', 'Testing', 'Client_Review']