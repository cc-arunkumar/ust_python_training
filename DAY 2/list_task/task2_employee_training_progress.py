"""
Scenario:
You are tracking the employees who have completed their mandatory “Cyber Security Awareness” trainin

"""


completed=["John","Priya","Amit"]
completed.append("Neha")
completed.append("Rahul")
completed.remove("Amit")
pending=["Meena","Vivek","Sita"]
all_employees=completed+pending
all_employees.sort()
print("All Employees (Completed + Pending):")
print(all_employees)
print("Total Employees:",len(all_employees))


# sample output


"""
All Employees (Completed + Pending):
['John', 'Meena', 'Neha', 'Priya', 'Rahul', 'Sita', 'Vivek']
Total Employees: 7

"""