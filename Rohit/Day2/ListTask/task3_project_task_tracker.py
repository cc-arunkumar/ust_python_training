tasks =  ["Requirement gathering", "Design UI", "Develop Backend", "Testing", "Deployment"]
print(tasks[0])
print(tasks[-1])

for x in range(len(tasks)-1):
    print(x)
    if tasks[x]=="Testing":
        tasks.insert(x,"client Review")

print(tasks)
print(tasks[0:3])
backup_tasks = tasks.copy()
tasks.remove("Deployment")
print(tasks)
print(backup_tasks)




# ======================sample output==================
# Requirement gathering
# Deployment
# 1
# 2
# 3
# ['Requirement gathering', 'Design UI', 'Develop Backend', 'client Review', 'Testing', 'Deployment']       
# ['Requirement gathering', 'Design UI', 'Develop Backend']
# ['Requirement gathering', 'Design UI', 'Develop Backend', 'client Review', 'Testing']
# ['Requirement gathering', 'Design UI', 'Develop Backend', 'client Review', 'Testing', 'Deployment'] 