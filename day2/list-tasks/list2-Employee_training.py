
# Task 2: Employee Training Progress
# Tracker
completed=["John", "Priya", "Amit"]
completed.append("Neha")
completed.append("Rahul")
completed.remove("Amit")
pending=["Meena", "Vivek", "Sita"]
all_employees=completed+pending
print("All Employees completed+pending",sorted(all_employees))
print("Total Employees",len(all_employees))


# /sample output
# All Employees completed+pending ['John', 'Meena', 'Neha', 'Priya', 'Rahul', 'Sita', 'Vivek']
# Total Employees 7