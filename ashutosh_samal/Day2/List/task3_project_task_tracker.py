#Task 3: Project Task Tracker

tasks = ["Requirement gathering", "Design UI", "Develop Backend", "Testing", "Deployment"]
print("First task: ",tasks[0])
print("Last task: ",tasks[-1])
tasks.insert(4,"Client Review")
print("First 3 tasks: ",tasks[0:3])
backup_tasks = tasks.copy()
tasks.remove("Deployment")
print("Main list after removal: ",tasks)
print("Backup list (unchanged): ",backup_tasks)

# #Sample Output
# First task:  Requirement gathering
# Last task:  Deployment
# First 3 tasks:  ['Requirement gathering', 'Design UI', 'Develop Backend']
# Main list after removal:  ['Requirement gathering', 'Design UI', 'Develop Backend', 'Testing', 'Client Review']
# Backup list (unchanged):  ['Requirement gathering', 'Design UI', 'Develop Backend', 'Testing', 'Client Review', 'Deployment']