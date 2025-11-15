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
# Expected Output(sample):
# All Employees (Completed + Pending):
# ['John', 'Meena', 'Neha', 'Priya', 'Rahul', 'Sita', 'Vivek']
# Total Employees: 7

#Code

# Create a list of employees who have completed their tasks
completed = ["John", "Priya", "Amit"]

# Add new employees to the completed list using append()
completed.append("Neha")
completed.append("Rahul")

# Remove an employee from the completed list
completed.remove("Amit")

# Create a list of employees who still have pending tasks
pending = ["Meena", "Vivek", "Sita"]

# Combine both lists (completed + pending) into one list
all_employees = completed + pending

# Sort the combined list alphabetically
all_employees.sort()

# Count the total number of employees in the combined list
count = len(all_employees)

# Print the full list of employees
print("All Employees (Completed + Pending):", all_employees)

# Print the total number of employees
print("Total Employees:", count)

#output
# PS C:\Users\303379\day3_training> & C:/Users/303379/AppData/Local/Microsoft/WindowsApps/python3.13.exe c:/Users/303379/day3_training/task2_training_Process.py
# All Employees (Completed + Pending): ['John', 'Meena', 'Neha', 'Priya', 'Rahul', 'Sita', 'Vivek']
# Total Employees: 7
# PS C:\Users\303379\day3_training> 
