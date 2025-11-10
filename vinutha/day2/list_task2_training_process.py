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

completed=["John", "Priya", "Amit"]
completed.append("Neha")
completed.append("Rahul")
completed.remove("Amit")
pending=["Meena", "Vivek", "Sita"]
all_employees=completed+pending
all_employees.sort()
count=len(all_employees)
print("All Employees (Completed + Pending):",all_employees)
print("Total Employees:",count)

#output
# PS C:\Users\303379\day3_training> & C:/Users/303379/AppData/Local/Microsoft/WindowsApps/python3.13.exe c:/Users/303379/day3_training/task2_training_Process.py
# All Employees (Completed + Pending): ['John', 'Meena', 'Neha', 'Priya', 'Rahul', 'Sita', 'Vivek']
# Total Employees: 7
# PS C:\Users\303379\day3_training> 
