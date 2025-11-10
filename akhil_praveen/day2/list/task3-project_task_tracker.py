# project_task_tracker
tasks = ["Requirement gathering", "Design UI", "Develop Backend", "Testing", "Deployment"]
print("First task: ",tasks[0])
print("Last task: ",tasks[-1])
tasks.insert(4,"Client Review")
print("First three tasks: ",tasks[:3])
backup_tasks = tasks.copy()
tasks.remove("Deployment")
print("Backup list: ",backup_tasks)
print("Main list: ",tasks)

# First task:  Requirement gathering
# Last task:  Deployment
# First three tasks:  ['Requirement gathering', 'Design UI', 'Develop Backend']
# Backup list:  ['Requirement gathering', 'Design UI', 'Develop Backend', 'Testing', 'Client Review', 'Deployment']
# Main list:  ['Requirement gathering', 'Design UI', 'Develop Backend', 'Testing', 'Client Review']