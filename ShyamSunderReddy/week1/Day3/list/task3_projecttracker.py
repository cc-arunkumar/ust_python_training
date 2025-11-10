#Task 3: Project Task Tracker
tasks=["Requirement gathering", "Design UI", "Develop Backend", "Testing", "Deployment"]
print("First task:",tasks[0])
print("Last task:",tasks[len(tasks)-1])
index=tasks.index("Testing")
tasks.insert(index+1,"Client Review")
new=tasks[0:3]
print("First 3 tasks:",new)
backup_tasks=tasks.copy()
tasks.remove("Deployment")
print("Backup list (unchanged): ",backup_tasks)
print("Main list after removal: ",tasks)

#Sample output
# First task: Requirement gathering
# Last task: Deployment
# First 3 tasks: ['Requirement gathering', 'Design UI', 'Develop Backend']    
# Backup list (unchanged):  ['Requirement gathering', 'Design UI', 'Develop Backend', 'Testing', 'Client Review', 'Deployment']
# Main list after removal:  ['Requirement gathering', 'Design UI', 'Develop Backend', 'Testing', 'Client Review']

