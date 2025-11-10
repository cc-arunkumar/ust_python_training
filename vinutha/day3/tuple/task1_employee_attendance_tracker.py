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
# Employee with highest attendance: John (5 days

#Code

attendance = (
    ("E101", "John", 5),
    ("E102", "Priya", 3),
    ("E103", "Amit", 4),
    ("E104", "Neha", 2)
)
print("Employee attended more than 4:")
for emp_id, name, days in attendance:
    if days>=4:
        print(name)

count=0
for emp_id, name, days in attendance:
    if days<4:
        count+=1
print("Employee present less than 4 days:",count)

max_days = 0
max_employee = ""
for emp_id, name, days in attendance:
    if days > max_days:
        max_days = days
        max_employee = name
print(f"\nEmployee with highest attendance: {max_employee} ({max_days} days)")

#output
# PS C:\Users\303379\day3_training> & C:/Users/303379/AppData/Local/Microsoft/WindowsApps/python3.13.exe c:/Users/303379/day3_training/task1_Employee_Attendance_Tracker.py
# Employee attended more than 4:
# John
# Amit
# Employee present less than 4 days: 2

# Employee with highest attendance: John (5 days)
# PS C:\Users\303379\day3_training> 