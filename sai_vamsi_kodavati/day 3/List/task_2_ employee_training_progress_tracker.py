# TASK 2 - : Employee Training Progress Tracker

completed = ["John", "Priya", "Amit"]
completed.append("Neha")
completed.append("Rahul")
completed.remove("Rahul")

pending = ["Meena", "Vivek", "Sita"]

all_employees = completed + pending
print("All Employees(Completed + Pending):",all_employees)

length = len(all_employees)
print("Total Employees: ",length)

# Sample Output
# All Employees(Completed + Pending): ['John', 'Priya', 'Amit', 'Neha', 'Meena', 'Vivek', 'Sita']
# Total Employees:  7