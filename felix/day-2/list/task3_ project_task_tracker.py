# projrct task tracker

tasks = ["Requirement gathering", "Design UI", "Develop Backend", "Testing", "Deployment"]
print("First Task: ",tasks[0])
print("Last Task: ",tasks[-1])

tasks.insert(tasks.index("Testing")+1,"Client Review")

print("First 3 tasks: ",tasks[:3])

backup_tasks = list(tasks)
tasks.remove("Deployment")

print("Backup list (unchanged): ",backup_tasks)
print("Main list after removal: ",tasks)

# output

# First Task:  Requirement gathering
# Last Task:  Deployment
# First 3 tasks:  ['Requirement gathering', 'Design UI', 'Develop Backend']
# Backup list (unchanged):  ['Requirement gathering', 'Design UI', 'Develop Backend', 'Testing', 'Client Review', 'Deployment']
# Main list after removal:  ['Requirement gathering', 'Design UI', 'Develop Backend', 'Testing', 'Client Review']