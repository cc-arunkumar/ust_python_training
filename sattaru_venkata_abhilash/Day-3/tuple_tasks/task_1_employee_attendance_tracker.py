# Task 1: Employee Attendance Tracker
# Scenario:
# Each tuple contains: (employee_id, employee_name, days_present)
# The program will analyze attendance data.

attendance = (
    ("E101", "John", 5),
    ("E102", "Priya", 3),
    ("E103", "Amit", 4),
    ("E104", "Neha", 2)
)

# 1. Print all employee names who attended 4 or more days
print("All employee names who attended 4 or more days:")
for employee_id, employee_name, days_present in attendance:
    if days_present >= 4:
        print(f"- {employee_name}")

# 2. Count how many employees were present less than 4 days
count = 0
for employee_id, employee_name, days_present in attendance:
    if days_present < 4:
        count += 1
print("Employees present less than 4 days:", count)

# 3. Find the employee with maximum attendance
max_days = 0
top_employee = ""
for employee_id, employee_name, days_present in attendance:
    if days_present > max_days:
        max_days = days_present
        top_employee = employee_name

# 4. Print result
print(f"Employee with highest attendance: {top_employee} ({max_days} days)")


# Sample Output:
# All employee names who attended 4 or more days:
# - John
# - Amit
# Employees present less than 4 days: 2
# Employee with highest attendance: John (5 days)
