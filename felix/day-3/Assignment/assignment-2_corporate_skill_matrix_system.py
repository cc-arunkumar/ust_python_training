# corporate skill matrix


skills_data = [
 ("E101", "Python", "Advanced"),
 ("E101", "SQL", "Intermediate"),
 ("E102", "Excel", "Expert"),
 ("E102", "PowerBI", "Advanced"),
 ("E101", "Python", "Beginner"),
 ("E101", "Excel", "Intermediate")
]

data = {}
for i in skills_data:
    if i[0] not in data:
        data[i[0]] = [(i[1],i[2])]
    else:
        data[i[0]].append((i[1],i[2]))
print("Employees with its skills: ")
print(data)
print("\n")
print("Employees with 3+ unique skills:")
for i in data:
    if len(set(data[i]))>3:
        print(i)

# output

# Employees with its skills: 
# {'E101': [('Python', 'Advanced'), ('SQL', 'Intermediate'), ('Python', 'Beginner'), ('Excel', 'Intermediate')], 'E102': [('Excel', 'Expert'), ('PowerBI', 'Advanced')]}

# Employees with 3+ unique skills:
# E101