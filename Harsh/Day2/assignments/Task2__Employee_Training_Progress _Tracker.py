# Task 2: Employee Training Progress
# Tracker
# Scenario:
# You are tracking the employees who have completed their mandatory “Cyber
# Security Awareness” training.

# Initialize a list of employees who have completed their tasks
completed = ["John", "Priya", "Amit"]

# Add new employees to the completed list
completed.append("Neha")
completed.append("Rahul")

# Remove an employee from the completed list
completed.remove("Amit")

# Create a list of employees with pending tasks
pending = ["Meena", "Vivek", "Sita"]

# Merge pending employees into the completed list
completed.extend(pending)

# Assign the combined list to all_employees
all_employees = completed

# Sort the list alphabetically
all_employees.sort()

# Print the organized list of all employees
print("All Employees (Completed + Pending):")
print(all_employees)

# Print the total number of employees
print("Total Employees:", len(all_employees))


# All Employees (Completed + Pending):
# ['John', 'Meena', 'Neha', 'Priya', 'Rahul', 'Sita', 'Vivek']
# Total Employees: 7