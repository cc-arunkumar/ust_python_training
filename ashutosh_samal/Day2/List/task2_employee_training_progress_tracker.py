#Task 2: Employee Training Progress Tracker

# List of completed employees
completed = ["John", "Priya", "Amit"]

# Adding new employees to the completed list using append()
completed.append("Neha")
completed.append("Rahul")

# Removing an employee (Amit) from the completed list
completed.remove("Amit")

# List of pending employees
pending = ["Meena", "Vivek", "Sita"]

# Combining the completed and pending lists into a single list (all employees)
all_employees = completed + pending

# Sorting the combined list of all employees in alphabetical order
all_employees.sort()

# Printing the list of all employees (completed + pending)
print("All Employees (Completed + Pending):", all_employees)

# Printing the total number of employees
print("Total Employees: ", len(all_employees))


#Sample Output
# All Employees (Completed + Pending): ['John', 'Meena', 'Neha', 'Priya', 'Rahul', 'Sita', 'Vivek']
# Total Employees:  7