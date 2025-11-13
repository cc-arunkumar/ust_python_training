#Task3 Project Task Tracker

tasks=["Requirement gathering", "Design UI", "Develop Backend", "Testing", "Deployment"]
print("First task: ",tasks[0])
print("Last task: ",tasks[1])
tasks.insert(4,"Client Review")
print('The first three tasks: ',tasks[0:3])
backup_task=tasks.copy()
tasks.remove("Deployment")
print("Backup List(unchanged): ",backup_task)
print("main task after removal: ",tasks)

#Sample Execution
# First task:  Requirement gathering
# Last task:  Design UI
# The first three tasks:  ['Requirement gathering', 'Design UI', 'Develop Backend']
# Backup List(unchanged):  ['Requirement gathering', 'Design UI', 'Develop Backend', 'Testing', 'Client Review', 'Deployment']
# main task after removal:  ['Requirement gathering', 'Design UI', 'Develop Backend', 'Testing', 'Client Review']

