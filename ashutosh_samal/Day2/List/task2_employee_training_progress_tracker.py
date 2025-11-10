#Task 2: Employee Training Progress Tracker

completed = ["John","Priya","Amit"]
completed.append("Neha")
completed.append("Rahul")
completed.remove("Amit")
pending = ["Meena","Vivek","Sita"]
all_employees = completed+pending
all_employees.sort()
print("All Employees (Completed + Pending):",all_employees)
print("Total Employees: ",len(all_employees))

#Sample Output
# All Employees (Completed + Pending): ['John', 'Meena', 'Neha', 'Priya', 'Rahul', 'Sita', 'Vivek']
# Total Employees:  7