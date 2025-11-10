# Task 1: Employee Attendance Tracker
# Scenario:
# Your HR system stores each employee’s attendance record for a week as a tuple.
# Each tuple contains:
# (employee_id, employee_name, days_present)
# Example data:
# attendance = (
#  ("E101", "John", 5),
#  ("E102", "Priya", 3),
#  ("E103", "Amit", 4),
#  ("E104", "Neha", 2)
# )
# Your Tasks:
# 1. Print all employee names who attended 4 or more days.
# 2. Count how many employees were present less than 4 days.
# 3. Find the employee with maximum attendance using a simple loop.
# 4. Print the result in this format:
# Employee with highest attendance: John (5 days)
# Hints:
# Use tuple unpacking inside the loop:
# Tuple Tasks 1
# for emp_id, name, days in attendance:
#  # your logic here
# Keep track of the highest attendance using variables.


attendance = [
    ("E101", "John", 5),
    ("E102", "Priya", 3),
    ("E103", "Amit", 4),
    ("E104", "Neha", 2)
]
print("Present 4 or more days:")
for emp_id, name, days in attendance:
    if days >= 4:
        print(name)
count = 0
for emp_id, name, days in attendance:
    if days < 4:
        count += 1
print("Less than 4 days:", count)
max_emp = attendance[0]
for emp in attendance:
    if emp[2] > max_emp[2]:
        max_emp = emp
print(f"Employee with highest attendance: {max_emp[1]} ({max_emp[2]} days)")
# sampleoutput
# Present 4 or more days:
# John
# Amit
# Less than 4 days: 2
# Employee with highest attendance: John (5 days)