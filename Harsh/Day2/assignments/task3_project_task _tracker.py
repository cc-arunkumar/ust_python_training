tasks=["Requirement gathering", "Design UI", "Develop Backend", "Testing", "Deployment"]
print(" First task:", tasks[0])
print(" Last task:", tasks[-1])
tasks.insert(3,"Client Review")
three=tasks[0:3]
print(" First 3 tasks: ",three)
backup_tasks=tasks.copy()
tasks.remove("Deployment")
print(" Backup list (unchanged):" , backup_tasks)
print(" Main list after removal:" , tasks)

#  First task: Requirement gathering
#  Last task: Deployment
#  First 3 tasks:  ['Requirement gathering', 'Design UI', 'Develop Backend']  
#  Backup list (unchanged): ['Requirement gathering', 'Design UI', 'Develop Backend', 'Client Review', 'Testing', 'Deployment']
#  Main list after removal: ['Requirement gathering', 'Design UI', 'Develop Backend', 'Client Review', 'Testing']