#Task 3: Project Task Tracker

#Code 
tasks= ["Requirement gathering", "Design UI", "Develop Backend", "Testing", "Deployment"]
print("First Task : ",tasks[0])
print("Last Task : ",tasks[-1])
tasks.insert(4,"Client Review")
print("First 3 task : ",tasks[0:3])
backup_task=tasks.copy()
tasks.remove("Deployment")
print("Backup List (unchanged) : ",backup_task)
print("Main list after removal : ",tasks)

#Sample Output
# First Task :  Requirement gathering
# Last Task :  Deployment
# First 3 task :  ['Requirement gathering', 'Design UI', 'Develop Backend']
# Backup List (unchanged) :  ['Requirement gathering', 'Design UI', 'Develop Backend', 'Testing', 'Client Review', 'Deployment']
# Main list after removal :  ['Requirement gathering', 'Design UI', 'Develop Backend', 'Testing', 'Client Review']