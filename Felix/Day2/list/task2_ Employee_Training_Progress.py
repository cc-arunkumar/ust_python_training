completed = ["John", "Priya", "Amit"]
completed.append("Neha")
completed.append("Rahul")
completed.remove("Amit")

pending = ["Meena", "Vivek", "Sita"]
all_employees = completed + pending

all_employees.sort()
print("All employees (completed + pending)")
print(all_employees)
print("total Employees: ",len(all_employees))

# output

# All employees (completed + pending)
# ['John', 'Meena', 'Neha', 'Priya', 'Rahul', 'Sita', 'Vivek']
# total Employees:  7