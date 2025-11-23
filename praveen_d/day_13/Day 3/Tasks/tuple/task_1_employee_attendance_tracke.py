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

attendence_tuple=(
    ("E101","John",5),
    ("E102", "Priya", 3),
    ("E103", "Amit", 4),
    ("E104", "Neha", 2)
)

less_than_four_days=0

for emp_id,emp_name,emp_days_present in attendence_tuple:
    if emp_days_present>=4:
        print(f"{emp_name}")
    else:
        less_than_four_days+=1

max=0

for emp_id,emp_name,emp_days_present in attendence_tuple:
    if emp_days_present>max:
        max=emp_days_present
        max_atten_emp=emp_name

print(f"Employee with highest attendance: {max_atten_emp} ({max} days)")


# cke.py"
# John
# Amit
# Employee with highest attendance: John (5 days)



