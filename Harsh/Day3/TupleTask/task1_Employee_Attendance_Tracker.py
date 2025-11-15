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


tuple1 = (
    ("E101", "John", 5),
    ("E102", "Priya", 3),
    ("E103", "Amit", 4),
    ("E104", "Neha", 2)
)

# Print employee names with 4 or more days present
for emp_id, emp_name, days_present in tuple1:
   if days_present>=4:
       print(emp_name)


# Count employees with less than 4 days present
count=0
for emp_id, emp_name, days_present in tuple1:
    if days_present<4:
        count+=1
print(count,"employees were present less than 4 days.")

# Find employee with maximum attendance
max_day=0
emp=""
for emp_id, emp_name, days_present in tuple1:
    if days_present>max_day:
        max_day=days_present
        emp=emp_name
        print(emp_name,"has the max attendance")


# John
# Amit
# 2 employees were present less than 4 days.
# John has the max attendance

