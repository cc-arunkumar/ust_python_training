"""
Scenario:
You are tracking the employees who have completed their mandatory “Cyber Security Awareness” training.
"""

completed=["John","Priya","Amit"]  # Initial list of employees who completed the training

completed.append("Neha")  # Adding a new employee who completed the training
completed.append("Rahul") # Adding another employee who completed the training

completed.remove("Amit")  # Removing an employee from the completed list (maybe error or reassigned)

pending=["Meena","Vivek","Sita"]  # List of employees who are pending training

all_employees=completed+pending  # Combine completed and pending lists into one
all_employees.sort()  # Sort the combined list alphabetically

print("All Employees (Completed + Pending):")  
print(all_employees)  # Print the full sorted list of employees
print("Total Employees:",len(all_employees))  # Print total number of employees


# sample output


"""
All Employees (Completed + Pending):
['John', 'Meena', 'Neha', 'Priya', 'Rahul', 'Sita', 'Vivek']
Total Employees: 7

"""