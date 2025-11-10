completed = ["John", "Priya", "Amit"]
completed.append("Neha")
completed.append("Rahul")
completed.remove("Amit")

pending = ["Meena", "Vivek", "Sita"]
completed.extend(pending)
allEmployess=completed
print(allEmployess)
allEmployess.sort()
print(allEmployess)


for x in range(len(allEmployess)):
    print(allEmployess[x])
print("Total Employees",len(allEmployess))


# ===========sample output=================
# ['John', 'Priya', 'Neha', 'Rahul', 'Meena', 'Vivek', 'Sita']
# ['John', 'Meena', 'Neha', 'Priya', 'Rahul', 'Sita', 'Vivek']
# John
# Meena
# Neha
# Priya
# Rahul
# Sita
# Vivek
# Total Employees 7
