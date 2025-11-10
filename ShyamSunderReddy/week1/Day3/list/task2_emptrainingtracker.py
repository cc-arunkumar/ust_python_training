#Task 2: Employee Training Progress Tracker
completed=["John", "Priya", "Amit"]
completed.append("Neha")
completed.append("Rahul")
completed.remove("Amit")
pending=["Meena", "Vivek", "Sita"]

completed.extend(pending)
all_employees=completed
all_employees.sort()
print("All Employees (Completed + Pending):")
print(all_employees)

#sample output
# All Employees (Completed + Pending):
# ['John', 'Meena', 'Neha', 'Priya', 'Rahul', 'Sita', 'Vivek']