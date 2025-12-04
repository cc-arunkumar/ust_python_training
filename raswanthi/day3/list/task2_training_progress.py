#Task 2: Employee Training Progress Tracker
completed=["John","Priya","Amit"]
completed.append("Neha")
completed.append("Rahul")
completed.remove("Amit")
pending=["Meena","Vivek","Sita"]
completed.extend(pending)
all_employees=[]
all_employees.extend(completed)
all_employees.sort()
print("All Employees (Completed + Pending):\n",all_employees)
print("Total Employees:",len(all_employees))

#output
'''
All Employees (Completed + Pending):
 ['John', 'Meena', 'Neha', 'Priya', 'Rahul', 'Sita', 'Vivek']
Total Employees: 7
'''
