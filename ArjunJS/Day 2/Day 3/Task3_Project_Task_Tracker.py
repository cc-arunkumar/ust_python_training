#Task 3: Project Task Tracker
tasks = ["Requirement gathering", "Design UI", "Develop Backend", "Testing", "Deployment"]
print(f"First Task : {tasks[0]}")
print(f"Last Task : {tasks[len(tasks)-1]}")
for i in range(0,len(tasks)):
    if(tasks[i]=="Testing"):
        tasks.insert(i+1,"Client Review")
print(f"First 3 Tasks : {tasks[:3]}")
backup_tasks=tasks.copy()
tasks.remove("Deployment")
print(f"Backup list (unchanged): {backup_tasks}")
print(f"Main list after removal: {tasks}")
#Output
# First Task : Requirement gathering
# Last Task : Deployment
# First 3 Tasks : ['Requirement gathering', 'Design UI', 'Develop Backend']
# Backup list (unchanged): ['Requirement gathering', 'Design UI', 'Develop Backend', 'Testing', 'Client Review', 'Deployment']
# Main list after removal: ['Requirement gathering', 'Design UI', 'Develop Backend', 'Testing', 'Client Review']