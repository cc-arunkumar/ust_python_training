# Employee Training Progress Tracker
# You are tracking the employees who have completed their mandatory “Cyber
# Security Awareness” training.

# List of completed employees
completed = ["John", "Priya", "Amit"]

# Add new employees to the completed list
completed.append("Neha")
completed.append("Rahul")

# Remove an employee from the completed list
completed.remove("Amit")

# List of pending employees
pending = ["Meena", "Vivek", "Sita"]

# Combine completed and pending employees into a single list
all_employees = completed + pending

# Sort the combined list of employees
all_employees.sort()

# Print the list of all employees
print("All Employees (Completed + Pending):")
print(all_employees)

# Print the total number of employees
print("Total Employees: ", len(all_employees))



# Sample output

# All Employees (Completed + Pending):
# ['John', 'Meena', 'Neha', 'Priya', 'Rahul', 'Sita', 'Vivek']
# Total Employees:  7