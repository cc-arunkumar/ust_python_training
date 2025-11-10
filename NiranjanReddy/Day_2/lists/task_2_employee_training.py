# Task 2: Employee Training Progress Tracker
completed=["John", "Priya", "Amit"]
completed.append("Neha")
completed.append("Rahul")
completed.remove("Amit")
pending=["Meena", "Vivek", "Sita"]
completed.extend(pending)
completed.sort()
print("All Employees (Completed + Pending):\n",completed)
print("Total Employees:",len(completed))
# Sample output
# All Employees (Completed + Pending):
#  ['John', 'Meena', 'Neha', 'Priya', 'Rahul', 'Sita', 'Vivek']
# Total Employees: 7