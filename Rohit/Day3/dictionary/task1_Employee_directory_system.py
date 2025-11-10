employee = dict(
E101= "Arjun",
E102= "Neha",
E103= "Ravi",
)


employee.update(El04= "priya")
employee.update(El05= "vikram")

employee.update(E103 = "Ravi kumar")
del employee["E102"]
print(employee)
# ============= sample output=============================
# {'E101': 'Arjun', 'E103': 'Ravi kumar', 'El04': 'priya', 'El05': 'vikram'}