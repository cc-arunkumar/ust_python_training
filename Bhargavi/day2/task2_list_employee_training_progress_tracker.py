#Employee Training Progress Tracker

# Task 2: Employee Training Progress
# Tracker

# Scenario:
# You are tracking the employees who have completed their mandatory “Cyber
# Security Awareness” training.

# Instructions:
# 1. Create a list named completed with employees who have finished training:
# ["John", "Priya", "Amit"]
# 2. New employees completed the training: "Neha" and "Rahul" .
# Add both to the list using append() twice.
# 3. "Amit" left the company. Remove him from the list.
# 4. Create another list named pending with:
# ["Meena", "Vivek", "Sita"]
# 5. Merge both lists into one master list named all_employees .
# 6. Sort the list alphabetically.
# Day 3 2
# 7. Print the list of all employees along with total count.


# List of employees who completed tasks
completed = ["John", "Priya", "Amit"]

# Add new employees to the completed list
completed.append("Neha")
completed.append("Rahul")

# Remove an employee (e.g., Amit) from completed list
completed.remove("Amit")

# List of employees with pending tasks
pending = ["Meena", "Vivek", "Sita"]

# Combine completed and pending employees into one list
all_employees = completed + pending

# Sort the combined list alphabetically
all_employees.sort()

# Print the organized employee list
print("All employees (completed + pending):")
print(all_employees)

# Print total number of employees
print("Total Employees:", len(all_employees))


#  Output:
# All employees (completed + pending):
# ['John', 'Meena', 'Neha', 'Priya', 'Rahul', 'Sita', 'Vivek']
# Total Employees: 7
