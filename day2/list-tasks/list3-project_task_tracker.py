# Task 3: Project Task Tracker

tasks=["Requirement gathering", "Design UI", "Develop Backend", "Testing", "Deployment"]
print("first task:",tasks[0])
print("last task:",tasks[-1])
tasks.insert(4,"client review")
print("first 3 tasks:",tasks[:3])
backup_tasks=print("backup_tasks",tasks)
tasks.remove("Deployment")
print("main list after removel:",tasks)


# sample output
# first task: Requirement gathering
# last task: Deployment
# first 3 tasks: ['Requirement gathering', 'Design UI', 'Develop Backend']
# backup_tasks ['Requirement gathering', 'Design UI', 'Develop Backend', 'Testing', 'client review', 'Deployment']
# main list after removel: ['Requirement gathering', 'Design UI', 'Develop Backend', 'Testing', 'client review']